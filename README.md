# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

## Data Storage
- Folder Structure:
  - data/raw/: stores unmodified or minimally processed CSV exports for inspection and reproducibility.
  - data/processed/: stores cleaned and structured datasets in Parquet format for efficient analysis.
- Formats used: CSV for simplicity and human readability; Parquet for compact size and faster I/O in downstream analysis
- Read/write Access: files are configured via environment variables (DATA_DIR_RAW, DATA_DIR_PROCESSED) in a .env file. The notebook loads these variables with python-dotenv
