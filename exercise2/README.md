# File Processor

A Python class implementation for handling various file processing tasks including folder exploration, CSV analysis, and DICOM file processing.

## Requirements

```bash
pip install pandas numpy pydicom pillow
```

## Usage

```python
# Initialize the processor
processor = FileProcessor(base_path="./data", log_file="processor.log")

# List folder contents
processor.list_folder_contents("test_folder", details=True)

# Analyze CSV file
processor.read_csv(
    filename="sample-02-csv.csv",
    report_path="./reports",
    summary=True
)

# Process DICOM file
processor.read_dicom(
    filename="sample-02-dicom.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
    extract_image=True
)
```

## Features

### List Folder Contents

- Lists all files and folders in a specified directory
- Optional detailed view including file sizes and modification times

### CSV Processing

- Reads and analyzes CSV files
- Calculates statistics for numeric columns
- Optional summary for non-numeric columns
- Can generate detailed reports

### DICOM Processing

- Extracts basic DICOM file information
- Supports custom tag reading
- Optional image extraction to PNG format

## Error Handling

All operations are logged to the specified log file, including:

- File/folder not found errors
- Invalid file formats
- Processing errors
