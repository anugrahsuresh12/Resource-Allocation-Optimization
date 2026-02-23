<div align="center">

# 🏥 SmartStaff: Resource Allocation Optimization in Healthcare

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/en-us/microsoft-365/excel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*A comprehensive healthcare analytics system that optimizes patient flow and physician utilization to reduce operational costs while maintaining high-quality care delivery.*

[Overview](#overview) · [Project Structure](#project-structure) · [Key Features](#key-features) · [Methodology](#methodology) · [Key Findings](#key-findings--recommendations) · [Getting Started](#getting-started) · [Dashboard](#tableau-dashboard) · [Author](#author)

</div>

---

## Overview

**SmartStaff** transforms raw healthcare operational data into actionable recommendations for strategic resource allocation and staffing decisions. By combining exploratory data analysis, time-series forecasting, and interactive visualization, this project provides hospital administrators with data-driven insights to optimize physician scheduling, predict demand fluctuations, and maximize revenue streams.

The project analyzes patient visit data covering consultation duration, doctor availability, timestamped patient progression, and financial metrics across medication, consultation, and laboratory services.

---

## Project Structure

```
Resource-Allocation-Optimization/
│
├── Data files/                        # Raw and processed healthcare datasets
│
├── EDA/                               # Exploratory Data Analysis
│   └── ...                            # Correlation heatmaps, distribution plots,
│                                      # patient flow & workload analysis
│
├── PythonCode/                        # Core Python analytics scripts
│   └── ...                            # Data cleaning, feature engineering,
│                                      # statistical analysis
│
├── Time Series Analysis/              # Time-series decomposition
│   └── ...                            # Trend, seasonality & residual analysis
│
├── Time Series Forecasting/           # ARIMA forecasting models
│   └── ...                            # 30-day forward-looking predictions
│
├── Group Write up.pdf                 # Collaborative project documentation
├── Project Report.pdf                 # Detailed final project report
├── Resource Allocation Optimization   # Project presentation
│   in Healthcare.pptx
├── Tableau Dashboard Image.pdf        # Dashboard screenshot/export
├── dashboard.twb                      # Tableau workbook file
└── README.md
```

---

## Key Features

### 📊 Data Analytics & Visualization
- Interactive **Tableau dashboard** capturing doctor utilization metrics, revenue streams by time and service type, and temporal patterns in consultation earnings
- Exploratory data analysis examining patient flow patterns, physician workload distribution, and revenue sources across medication, consultations, and laboratory services
- Correlation heatmaps and distribution plots identifying financial impact drivers and service utilization patterns

### 📈 Predictive Modeling
- **ARIMA time-series forecasting** model built in Python to predict consultation revenue and identify peak-demand periods
- 30-day forward-looking forecasts supporting short-term operational planning
- Time-series decomposition analyzing trend, seasonality, and residual components to understand underlying demand patterns

### 🗃️ Data Management & Feature Engineering
- Cleaned and standardized patient visit data (sourced from Kaggle) including consultation duration, doctor availability, and timestamped patient progression
- Engineered features including **consultation duration** and **post-consultation time** metrics
- Validated and normalized categorical variables (Doctor Type, Financial Class, Patient Type) ensuring data integrity

---

## Methodology

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Data Intake    │────▶│   Data Cleaning  │────▶│     EDA &       │
│  (Kaggle Data)   │     │  & Engineering   │     │  Visualization  │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                        ┌─────────────────┐     ┌────────▼────────┐
                        │  Recommendations │◀────│  Time Series    │
                        │  & Reporting     │     │  Forecasting    │
                        └─────────────────┘     └─────────────────┘
```

**1. Data Collection & Preparation**
   Patient visit records were sourced from Kaggle and cleaned to handle missing values, standardize timestamps, and normalize categorical variables across doctor types, financial classes, and patient types.

**2. Feature Engineering**
   New metrics were derived including consultation duration (time from start to end of visit) and post-consultation time, enabling deeper analysis of physician efficiency and patient throughput.

**3. Exploratory Data Analysis**
   Statistical analysis and visualization were used to uncover patterns in patient flow, physician workload balance, and revenue distribution across service lines (medication, consultations, lab services).

**4. Time-Series Analysis & Forecasting**
   ARIMA models were applied to consultation revenue data after decomposing the time series into trend, seasonality, and residual components. The model generates 30-day rolling forecasts to support short-term staffing decisions.

**5. Dashboard Development**
   An interactive Tableau dashboard was built to present KPIs including doctor utilization rates, revenue breakdowns, and temporal demand patterns for use by hospital administrators.

---

## Key Findings & Recommendations

| Area | Finding | Recommendation |
|------|---------|----------------|
| **Seasonal Staffing** | Demand peaks in Feb-Apr, drops in Jun-Jul and Nov-Dec | Increase capacity during high-demand months; scale down during low-demand periods |
| **Revenue Optimization** | Certain high-revenue medications and underutilized physicians identified | Prioritize inventory management for top medications; increase visibility of high-performing physicians |
| **Preventive Care** | Low-demand months present underutilized capacity | Implement wellness initiatives during historically low-demand months to stabilize revenue |
| **Data-Driven Planning** | ARIMA forecasts reliably predict 30-day demand trends | Maintain baseline staffing with continuous monitoring using rolling forecasts |

---

## Getting Started

### Prerequisites
- Python 3.8+
- Tableau Desktop or Tableau Public (to view `dashboard.twb`)

### Installation

```bash
# Clone the repository
git clone https://github.com/anugrahsuresh12/Resource-Allocation-Optimization.git
cd Resource-Allocation-Optimization

# Install Python dependencies
pip install pandas numpy matplotlib seaborn statsmodels scipy
```

### Usage

```bash
# Run the EDA scripts
python PythonCode/<script_name>.py

# Run Time Series Analysis
python "Time Series Analysis/<script_name>.py"

# Run ARIMA Forecasting
python "Time Series Forecasting/<script_name>.py"
```

> Open `dashboard.twb` in Tableau Desktop to explore the interactive dashboard.

---

## Tableau Dashboard

<p align="center">
  <em>Interactive dashboard showcasing doctor utilization, revenue streams, and temporal demand patterns.</em>
</p>

> View the exported dashboard in [`Tableau Dashboard Image.pdf`](Tableau%20Dashboard%20Image.pdf)

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Statistical analysis, ARIMA modeling, correlation analysis, predictive analytics |
| **Tableau** | Interactive visualization and dashboard development |
| **Excel** | Data aggregation and summary statistics |
| **Pandas / NumPy** | Data manipulation and numerical computing |
| **Matplotlib / Seaborn** | Statistical visualization, heatmaps, distribution plots |
| **Statsmodels** | ARIMA time-series modeling and decomposition |

---

## Documentation

- 📄 [`Project Report.pdf`](Project%20Report.pdf) - Detailed final project report with methodology and results
- 📝 [`Group Write up.pdf`](Group%20Write%20up.pdf) - Collaborative project documentation
- 📊 [`Tableau Dashboard Image.pdf`](Tableau%20Dashboard%20Image.pdf) - Dashboard export
- 🎤 [`Resource Allocation Optimization in Healthcare.pptx`](Resource%20Allocation%20Optimization%20in%20Healthcare.pptx) - Project presentation

---

## Author

**Anugrah Suresh Kumar Nair**
- 🎓 MS in Health Informatics, Northeastern University
- 🦷 Licensed Dental Surgeon | 1,000+ patients treated across India

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/anugrah-nair-1833a7328)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/anugrahsuresh12)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:anugrahsuresh12@gmail.com)

---

<div align="center">

⭐ If you found this project useful, please consider giving it a star!

</div>
