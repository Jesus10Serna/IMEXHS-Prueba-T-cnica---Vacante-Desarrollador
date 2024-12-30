import { Injectable, signal } from '@angular/core';
import { StainResult } from '../models/stain-result.model';

@Injectable({
  providedIn: 'root'
})
export class StainService {
  // Using signals for state management
  private results = signal<StainResult[]>([]);
  
  // Expose the results as readonly
  public readonly stainResults = this.results.asReadonly();
  
  constructor() {}

  calculateStainArea(image: HTMLImageElement, numPoints: number): StainResult {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = image.width;
    canvas.height = image.height;
    ctx?.drawImage(image, 0, 0);
    
    let pointsInside = 0;
    const points: [number, number][] = [];
    
    // Generate random points and check if they're inside the stain
    for (let i = 0; i < numPoints; i++) {
      const x = Math.floor(Math.random() * image.width);
      const y = Math.floor(Math.random() * image.height);
      points.push([x, y]);
      
      const pixel = ctx?.getImageData(x, y, 1, 1).data;
      // Check if pixel is white (stain)
      if (pixel && pixel[0] === 255 && pixel[1] === 255 && pixel[2] === 255) {
        pointsInside++;
      }
    }
    
    const totalArea = image.width * image.height;
    const estimatedArea = (totalArea * pointsInside) / numPoints;
    
    const result: StainResult = {
      id: Date.now(),
      imageUrl: image.src,
      totalPoints: numPoints,
      pointsInside,
      estimatedArea,
      timestamp: new Date(),
      imageDimensions: {
        width: image.width,
        height: image.height
      }
    };
    
    // Update results using signals
    this.results.update(current => [...current, result]);
    
    return result;
  }

  clearResults() {
    this.results.set([]);
  }
}