# Data

This directory contains dataset metadata and processed data artifacts used by the SmartCrop project.

## Dataset Inventory

`dataset_inventory.csv` contains the crop-wise dataset research performed for the project.

It records:

- Dataset name
- Source
- Location
- Image count
- Disease / class coverage
- Dataset size
- Selection status
- Relevance to the Smart Farming Assistant

## Data Policy

Large raw datasets are **not stored in this GitHub repository**.

Instead, the repository maintains:

- Dataset source links
- Dataset metadata
- Selection rationale
- Preprocessing scripts
- Validation and cleaning reports

This avoids unnecessarily storing large datasets in Git while keeping the data workflow reproducible.

## Data Pipeline

```text
Raw Dataset
    ↓
Validation
    ↓
Cleaning
    ↓
Duplicate Detection
    ↓
Metadata Extraction
    ↓
Processed / Analytics-Ready Data