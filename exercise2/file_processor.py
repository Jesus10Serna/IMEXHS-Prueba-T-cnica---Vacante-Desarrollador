import os
import logging
from typing import Optional, List, Tuple
import pandas as pd
import pydicom
import numpy as np
from datetime import datetime
from PIL import Image

class FileProcessor:
    def __init__(self, base_path: str, log_file: str):
        """
        Initialize FileProcessor with base path and logging configuration
        """
        self.base_path = base_path
        
        # Configure logging
        self.logger = logging.getLogger('FileProcessor')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(fh)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        """
        List contents of specified folder with optional detailed information
        """
        try:
            folder_path = os.path.join(self.base_path, folder_name)
            if not os.path.exists(folder_path):
                raise FileNotFoundError(f"Folder {folder_path} does not exist")

            items = os.listdir(folder_path)
            print(f"\nFolder: {folder_path}")
            print(f"Number of elements: {len(items)}")

            files = []
            folders = []

            for item in items:
                item_path = os.path.join(folder_path, item)
                if details:
                    mod_time = datetime.fromtimestamp(os.path.getmtime(item_path))
                    if os.path.isfile(item_path):
                        size_mb = os.path.getsize(item_path) / (1024 * 1024)
                        files.append(f"- {item} ({size_mb:.1f} MB, Last Modified: {mod_time})")
                    else:
                        folders.append(f"- {item} (Last Modified: {mod_time})")
                else:
                    if os.path.isfile(item_path):
                        files.append(f"- {item}")
                    else:
                        folders.append(f"- {item}")

            if files:
                print("\nFiles:")
                print("\n".join(files))
            if folders:
                print("\nFolders:")
                print("\n".join(folders))

        except Exception as e:
            self.logger.error(f"Error listing folder contents: {str(e)}")
            raise

    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        """
        Read and analyze CSV file with optional reporting and summary
        """
        try:
            file_path = os.path.join(self.base_path, filename)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} does not exist")

            df = pd.read_csv(file_path)
            
            print("\nCSV Analysis:")
            print(f"Columns: {list(df.columns)}")
            print(f"Rows: {len(df)}")

            # Analyze numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            analysis_results = []
            
            print("\nNumeric Columns:")
            for col in numeric_cols:
                mean = df[col].mean()
                std = df[col].std()
                print(f"- {col}: Average = {mean:.1f}, Std Dev = {std:.1f}")
                analysis_results.append(f"{col}: Average = {mean:.1f}, Std Dev = {std:.1f}")

            # Optional summary for non-numeric columns
            if summary:
                print("\nNon-Numeric Summary:")
                non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns
                for col in non_numeric_cols:
                    unique_count = df[col].nunique()
                    print(f"- {col}: Unique Values = {unique_count}")

            # Save report if path provided
            if report_path:
                os.makedirs(report_path, exist_ok=True)
                report_file = os.path.join(report_path, f"{os.path.splitext(filename)[0]}_analysis.txt")
                with open(report_file, 'w') as f:
                    f.write("CSV Analysis Report\n\n")
                    f.write(f"File: {filename}\n")
                    f.write(f"Total Rows: {len(df)}\n")
                    f.write(f"Total Columns: {len(df.columns)}\n\n")
                    f.write("Numeric Column Analysis:\n")
                    f.write("\n".join(analysis_results))
                print(f"\nSaved summary report to {report_path}")

        except Exception as e:
            self.logger.error(f"Error processing CSV file: {str(e)}")
            raise

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, 
                  extract_image: bool = False) -> None:
        """
        Read and analyze DICOM file with optional tag extraction and image saving
        """
        try:
            file_path = os.path.join(self.base_path, filename)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} does not exist")

            dcm = pydicom.dcmread(file_path)
            
            print("\nDICOM Analysis:")
            print(f"Patient Name: {dcm.PatientName}")
            print(f"Study Date: {dcm.StudyDate}")
            print(f"Modality: {dcm.Modality}")

            # Print requested tags
            if tags:
                for tag in tags:
                    try:
                        value = dcm[tag].value
                        print(f"Tag {hex(tag[0])}, {hex(tag[1])}: {value}")
                    except Exception as e:
                        self.logger.warning(f"Could not read tag {tag}: {str(e)}")

            # Extract and save image if requested
            if extract_image:
                try:
                    img_array = dcm.pixel_array
                    img = Image.fromarray(img_array)
                    output_path = os.path.join(self.base_path, 
                                             f"{os.path.splitext(filename)[0]}.png")
                    img.save(output_path)
                    print(f"Extracted image saved to {output_path}")
                except Exception as e:
                    self.logger.error(f"Error extracting image: {str(e)}")
                    raise

        except Exception as e:
            self.logger.error(f"Error processing DICOM file: {str(e)}")
            raise