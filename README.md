2. Set Up the Environment
Ensure you have Python 3.8+ and R (version ≥ 4.0). Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install R packages: tidyverse, ggplot2, dplyr, broom.

3. Add Raw Data
Download the dataset (smmh_1.csv) from Kaggle and place it into:

bash
Copy
Edit
data/raw/
4. Run the Cleaning Script
Process the raw data:

bash
Copy
Edit
python src/data/make_dataset.py data/raw/smmh_1.csv data/processed/clean.csv
5. Run Analysis and Generate Visuals
Use the notebooks in notebooks/ or R scripts in src/visualization/ to:

Perform EDA

Conduct hypothesis testing

Generate boxplots, histograms, and scatterplots

Project Structure
data/
raw/: Original data from Kaggle

interim/: Cleaned but intermediate data

processed/: Final dataset used for analysis

notebooks/
Jupyter and R notebooks for EDA, regression modeling, and visualization

src/
data/: Scripts for data loading and cleaning

features/: Scripts for feature engineering (e.g., usage tiers)

models/: Model training and evaluation

visualization/: R scripts for generating publication-ready plots

reports/
Final figures, charts, and result tables

references/
Research papers cited in the literature review (PDFs or BibTeX)

tests/
Unit tests for cleaning functions and model evaluation

Analytical Overview
Cleaned dataset of 950 records from initial 1,000 responses

Depression scores measured on a 1–5 Likert scale

Time spent on social media categorized into tiers: 0–2, 2–4, 4–6, 6+ hours

Controlled for age, gender, sleep disturbance, and relationship status

Used multiple regression models (linear and logistic) and visualizations to explore trends

Theoretical Background
This research supports:

Displacement theory: excessive screen time displaces healthy offline behaviors

Social comparison theory: passive users are more prone to low self-esteem and depressive symptoms

Previous literature, including:

Riehm et al. (2019)

Mir et al. (2020)

Karim et al. (2020)

Future Work
Use longitudinal data for causal analysis

Incorporate objective screen-time logs

Explore machine learning models to detect risky usage patterns

Stratify analysis by race, gender, and socioeconomic background

Author
Arafat Bhuiyan
INST414 – Spring 2025
University of Maryland
