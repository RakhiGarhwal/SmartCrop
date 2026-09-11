# SmartCrop

A data-centric repository for the Smart Farming Assistant project.

This repository documents dataset research, selection, data preparation, machine learning models, and data pipelines for crop health monitoring.

## Project Focus

The SmartCrop system aims to support field-level crop monitoring using:

- Crop disease detection
- Pest identification
- Nutrient deficiency detection
- Environmental and sensor-based risk analysis
- Historical agricultural data analytics
- Edge-first and offline-first intelligence

## Dataset Research

Datasets were researched and evaluated based on:

- Crop relevance
- Disease and pest coverage
- Indian or field-based data availability
- Image quality and dataset size
- Annotation availability
- Suitability for model training
- Storage constraints

The current dataset inventory covers:

- Wheat
- Rice / Paddy
- Pearl Millet
- Maize
- Soybean
- Chickpea
- Multi-crop datasets

See the complete inventory:

`data/dataset_inventory.csv`

## Data Engineering Workflow

```text
Dataset Research
       ↓
Dataset Selection
       ↓
Data Collection
       ↓
Data Cleaning & Validation
       ↓
Preprocessing
       ↓
Model Training
       ↓
AI Predictions
       ↓
Structured Data
       ↓
Historical Analytics
       ↓
Farmer Advisory / Dashboard