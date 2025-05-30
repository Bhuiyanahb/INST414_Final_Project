# INST414_Final_Project

# Social Media & Mental Health in Young Adults  
**Research Question**: Does increased social media usage correlate with higher depressive symptoms?  

## **Key Findings**  
- **Regression Analysis**: Each additional hour of social media use was associated with a 0.15-point increase in depression score (p = 0.03).
- **Pearson Correlation**: `r = 0.102` (p = 0.054), suggesting a weak but near-significant positive relationship.
- **Visual Trends**: Histograms and boxplots show moderate-to-severe depressive symptoms among heavy users (6+ hrs/day), with a clear dose-response trend.
- **Age Insights**: Teens and individuals in their 20s reported more distraction, compulsive behavior, and social comparison distress.
- **Model Performance**: Linear Regression (RMSE = 1.32) slightly outperformed Decision Trees (RMSE = 1.33).

## **Reproduce Results**  
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/INST414_Final_Project.git
   cd INST414_Final_Project


2. Set Up the Environment
Ensure you have Python 3.8+ and R (version ≥ 4.0). Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   Install R packages: tidyverse, ggplot2, dplyr, broom.


3. Run the Cleaning Script
Process the raw data:

   ```bash
   python src/data/make_dataset.py data/raw/smmh_1.csv data/processed/clean.csv
5. Run Analysis and Generate Visuals
Use the notebooks in notebooks/ or R scripts in src/visualization/ to:

- Perform EDA

- Conduct hypothesis testing

- Generate boxplots, histograms, and scatterplots

## **Project Structure**
### Directory Structure and Purpose
1. data/
#### Contents: 
- raw/: Original data from Kaggle
- interim/: Cleaned but intermediate data
- processed/: Final dataset used for analysis

#### notebooks/
- Jupyter and R notebooks for EDA, regression modeling, and visualization

#### src/
- data/: Scripts for data loading and cleaning
- features/: Scripts for feature engineering (e.g., usage tiers)
- models/: Model training and evaluation
- visualization/: R scripts for generating publication-ready plots

#### reports/
- Final figures, charts, and result tables

#### references/
- Research papers cited in the literature review (PDFs or BibTeX)

#### tests/
- Unit tests for cleaning functions and model evaluation

### Analytical Overview
- Cleaned dataset of 950 records from initial 1,000 responses
- Depression scores measured on a 1–5 Likert scale
- Time spent on social media categorized into tiers: 0–2, 2–4, 4–6, 6+ hours
- Controlled for age, gender, sleep disturbance, and relationship status
- Used multiple regression models (linear and logistic) and visualizations to explore trends
### Theoretical Background
This research supports:
- Displacement theory: excessive screen time displaces healthy offline behavior
- Social comparison theory: passive users are more prone to low self-esteem and depressive symptoms
- Previous literature, including:
--Riehm et al. (2019)
--Mir et al. (2020)
--Karim et al. (2020)
### Future Work
- Use longitudinal data for causal analysis
- Incorporate objective screen-time logs
- Explore machine learning models to detect risky usage patterns
- Stratify analysis by race, gender, and socioeconomic background
### Author
Arafat Bhuiyan
INST414 – Spring 2025
University of Maryland
