# INST414_Final_Project

# Social Media & Mental Health in Young Adults  
**Research Question**: Does increased social media usage correlate with higher depressive symptoms?  

## **Key Findings**  
- **Pearson Correlation**: `r = 0.102` (p = 0.054), suggesting a weak but near-significant positive relationship.  
- **Visual Trends**: Histograms show moderate-to-severe depressive symptoms among heavy users (5+ hrs/day).  
- **Model Performance**: Linear Regression (RMSE=1.32) slightly outperformed Decision Trees (RMSE=1.33).  

## **Reproduce Results**  
1. Run data pipeline:  
   ```bash
   python src/data/make_dataset.py data/raw/social_health_raw.csv data/processed/clean.csv

# Project Structure Overview

## Directory Structure and Purpose

### 1. `data/`
**Contents**:
- `raw/`: Original immutable datasets (CSV/Excel from Kaggle, surveys)
- `interim/`: Partially processed data (cleaned but not final)
- `processed/`: Final analysis-ready datasets (950 cleaned records)

**Relationships**:
- `raw/` → Input for `src/data/make_dataset.py`
- `interim/` → Used by notebooks for EDA
- `processed/` → Fed into models and visualizations

**Benefits**:
- Ensures raw data preservation for reproducibility
- Tracks data transformation stages (IQR cleaning → imputation)
- Matches the documented cleaning pipeline from the research

---

### 2. `notebooks/`
**Contents**:
- Exploratory Data Analysis (EDA) notebooks
- Hypothesis testing notebooks (Pearson correlation analysis)
- Model comparison notebooks (Linear vs. Decision Tree)

**Relationships**:
- Depends on `data/processed/`
- Informs code development in `src/`

**Benefits**:
- Keeps experimental code separate from production pipelines
- Preserves the analysis narrative
- Allows safe iteration without breaking main scripts

---

### 3. `src/` (Core Processing Code)

#### `data/`
**Contents**:
- Data loading/cleaning scripts
- Train/test split utilities

**Relationships**:
- Processes `data/raw/` → outputs to `data/interim/` or `processed/`

**Benefits**:
- Automates reproducible data cleaning
- Encapsulates data processing methods

#### `features/`
**Contents**:
- Feature engineering scripts
- Normalization/scaling code

**Relationships**:
- Transforms `data/processed/` → feeds `models/`

**Benefits**:
- Isolates feature logic for maintainability
- Ensures consistent transformations

#### `models/`
**Contents**:
- Model training scripts
- Evaluation metrics calculation

**Relationships**:
- Uses features → outputs to `reports/figures/`

**Benefits**:
- Modular architecture for model comparisons
- Preserves model implementation details

#### `visualization/`
**Contents**:
- Plot generation scripts
- Chart customization code

**Relationships**:
- Depends on processed data and model outputs
- Outputs to `reports/figures/`

**Benefits**:
- Centralized visualization management
- Automated figure regeneration

---

### 4. `reports/`
**Contents**:
- Final figures (PNG/PDF)
- Statistical results tables

**Relationships**:
- Receives outputs from visualization and notebooks

**Benefits**:
- Clean separation of results from code
- Publication-ready outputs

---

### 5. `references/`
**Contents**:
- Cited papers (PDFs)
- Bibliography files

**Relationships**:
- Supports all research stages

**Benefits**:
- Centralized literature management
- Meets academic standards

---

### 6. `tests/`
**Contents**:
- Data cleaning validation tests
- Feature engineering tests

**Relationships**:
- Validates `src/` code functionality

**Benefits**:
- Ensures statistical methods work as intended
- Catches pipeline errors early

## Workflow
1. Add raw data to `data/raw/`
2. Process through `src/data/` scripts
3. Explore in `notebooks/`
4. Generate final outputs in `reports/`
