from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import numpy as np
from .. import models, schemas
from ..database import get_db

router = APIRouter()

def process_data(data_list: List[str]) -> tuple:
    # Convert string lists to numeric arrays
    numbers = []
    for row in data_list:
        try:
            row_numbers = [float(x) for x in row.split()]
            numbers.extend(row_numbers)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid numeric data")
    
    numbers = np.array(numbers)
    avg_before = float(np.mean(numbers))
    
    # Normalize data
    max_val = np.max(numbers)
    normalized = numbers / max_val if max_val != 0 else numbers
    avg_after = float(np.mean(normalized))
    
    return avg_before, avg_after, len(numbers)

@router.post("/elements/", response_model=List[schemas.Element])
def create_elements(
    payload: schemas.ElementCreate,
    db: Session = Depends(get_db)
):
    results = []
    for key, element_data in payload.elements.items():
        # Process device
        device = db.query(models.Device).filter(
            models.Device.device_name == element_data.deviceName
        ).first()
        if not device:
            device = models.Device(device_name=element_data.deviceName)
            db.add(device)
            db.commit()
            db.refresh(device)
        
        # Process data
        avg_before, avg_after, data_size = process_data(element_data.data)
        
        # Create element
        db_element = models.Element(
            id=element_data.id,
            device_id=device.id,
            avg_before_norm=avg_before,
            avg_after_norm=avg_after,
            data_size=data_size
        )
        db.add(db_element)
        results.append(db_element)
    
    db.commit()
    for result in results:
        db.refresh(result)
    
    return results

@router.get("/elements/", response_model=List[schemas.Element])
def read_elements(
    db: Session = Depends(get_db),
    created_after: Optional[datetime] = None,
    created_before: Optional[datetime] = None,
    avg_before_min: Optional[float] = None,
    avg_before_max: Optional[float] = None,
    avg_after_min: Optional[float] = None,
    avg_after_max: Optional[float] = None,
    data_size_min: Optional[int] = None,
    data_size_max: Optional[int] = None,
):
    query = db.query(models.Element)
    
    if created_after:
        query = query.filter(models.Element.created_date >= created_after)
    if created_before:
        query = query.filter(models.Element.created_date <= created_before)
    if avg_before_min:
        query = query.filter(models.Element.avg_before_norm >= avg_before_min)
    if avg_before_max:
        query = query.filter(models.Element.avg_before_norm <= avg_before_max)
    if avg_after_min:
        query = query.filter(models.Element.avg_after_norm >= avg_after_min)
    if avg_after_max:
        query = query.filter(models.Element.avg_after_norm <= avg_after_max)
    if data_size_min:
        query = query.filter(models.Element.data_size >= data_size_min)
    if data_size_max:
        query = query.filter(models.Element.data_size <= data_size_max)
    
    return query.all()

@router.get("/elements/{element_id}", response_model=schemas.Element)
def read_element(element_id: str, db: Session = Depends(get_db)):
    element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if element is None:
        raise HTTPException(status_code=404, detail="Element not found")
    return element

@router.put("/elements/{element_id}", response_model=schemas.Element)
def update_element(
    element_id: str,
    element_update: schemas.ElementUpdate,
    db: Session = Depends(get_db)
):
    element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if element is None:
        raise HTTPException(status_code=404, detail="Element not found")
    
    if element_update.device_name:
        device = db.query(models.Device).filter(
            models.Device.device_name == element_update.device_name
        ).first()
        if not device:
            device = models.Device(device_name=element_update.device_name)
            db.add(device)
            db.commit()
            db.refresh(device)
        element.device_id = device.id
    
    if element_update.id:
        element.id = element_update.id
    
    db.commit()
    db.refresh(element)
    return element

@router.delete("/elements/{element_id}")
def delete_element(element_id: str, db: Session = Depends(get_db)):
    element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if element is None:
        raise HTTPException(status_code=404, detail="Element not found")
    
    db.delete(element)
    db.commit()
    return {"message": "Element deleted successfully"}