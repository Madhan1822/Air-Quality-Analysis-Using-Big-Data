# 🌍 Real-Time Air Quality Monitoring and Big Data Analytics System

An intelligent Air Quality Index (AQI) monitoring and prediction system developed using Streamlit, Machine Learning, REST APIs, and Big Data Analytics.

---

# 📌 Project Overview

Air pollution is one of the major environmental challenges affecting human health and climate conditions. This project aims to monitor, analyze, and predict Air Quality Index (AQI) levels using real-time API data and historical pollution datasets.

The system integrates:

* Real-time AQI monitoring using OpenWeatherMap API
* Big Data processing using Dask
* Machine Learning prediction using Random Forest Regression
* Interactive dashboards and visualizations
* Health advisory generation based on AQI levels

The application helps users understand pollution conditions and promotes environmental awareness through data-driven insights.

---

# 🚀 Features

## 🌐 Real-Time AQI Monitoring

* Fetches live AQI data using OpenWeatherMap Air Pollution API
* Displays AQI category and pollutant concentrations
* Shows live location map

## 📊 Interactive Dashboard

* Streamlit-based responsive dashboard
* Interactive charts and visualizations
* AQI trend analysis

## 🤖 Machine Learning Prediction

* AQI prediction using Random Forest Regression
* Feature importance analysis
* Future AQI prediction

## ⚡ Big Data Analytics

* Large-scale CSV processing using Dask
* Correlation analysis
* Pollutant distribution analysis

## 🩺 Health Advisory System

* AQI-based health recommendations
* Safety alerts for sensitive groups

## 📥 Downloadable Reports

* Export AQI session history
* Download processed pollution data

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Frontend / UI

* Streamlit

## Big Data Tools

* Dask

## Machine Learning

* Scikit-learn

## Data Visualization

* Plotly
* Streamlit Charts

## APIs

* OpenWeatherMap Air Pollution API

## Libraries

* Pandas
* NumPy
* Requests

---

# 📂 Project Structure

```bash
AQI_BIGDATA_SYSTEM/
│
├── app.py                  # Real-time AQI Dashboard
├── app_1.py                # Big Data AQI Analytics Dashboard
├── aqi_data.csv            # AQI Dataset
├── requirements.txt        # Project Dependencies
├── README.md               # Project Documentation
│
├── static/
│   └── plots/
│
└── outputs/
    └── reports/
```

---

# ⚙️ Installation Steps

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd AQI_BIGDATA_SYSTEM
```

---

## 3️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Applications

## 🌍 Run Real-Time AQI Dashboard

```bash
streamlit run app.py
```

---

## ⚡ Run Big Data AQI Analytics Dashboard

```bash
streamlit run app_1.py
```

---

# 🌐 Application URL

After running the project, Streamlit will automatically open:

```bash
http://localhost:8501
```

---

# 📊 Dataset

The project uses:

## 1️⃣ Real-Time API Data

* OpenWeatherMap Air Pollution API

## 2️⃣ Historical AQI Dataset

File:

```bash
aqi_data.csv
```

### Dataset Columns

* City
* Date
* PM2.5
* PM10
* NO
* NO2
* NOx
* NH3
* CO
* SO2
* O3
* Benzene
* Toluene
* Xylene
* AQI
* AQI_Bucket

---

# 📈 Functional Modules

## 🌍 Real-Time AQI Monitoring

Displays:

* AQI Index
* AQI Category
* Pollutant Concentrations
* Location Map
* Session Trend Analysis

---

## 📊 Big Data Analytics Module

Performs:

* AQI Trend Analysis
* Correlation Heatmap
* Pollution Distribution Analysis
* City-wise AQI Summary

---

## 🤖 Machine Learning Module

### Model Used

* Random Forest Regressor

### Features Used

* PM2.5
* PM10
* NO2
* SO2
* CO
* O3

### Output

* AQI Prediction
* Model Accuracy
* Feature Importance Graph

---

# 🩺 AQI Health Advisory

| AQI Range | Category     | Health Advisory                         |
| --------- | ------------ | --------------------------------------- |
| 0 - 50    | Good         | Safe for all                            |
| 51 - 100  | Satisfactory | Acceptable air quality                  |
| 101 - 200 | Moderate     | Sensitive groups should reduce exposure |
| 201 - 300 | Poor         | Wear masks outdoors                     |
| 301 - 400 | Very Poor    | Avoid outdoor activities                |
| 401+      | Severe       | Health emergency                        |

---

# 📷 Dashboard Features

## app.py

* Live AQI Dashboard
* Pollutant Bar Charts
* AQI Trend Analysis
* AQI Prediction
* Download Session Data

## app_1.py

* Big Data AQI Dashboard
* Dask-based Processing
* Correlation Heatmap
* Random Forest Prediction
* AQI Distribution Analysis
* Feature Importance Visualization

---

# 🤖 Machine Learning Workflow

## Steps:

1. Load AQI dataset
2. Clean missing values
3. Select pollution features
4. Train Random Forest model
5. Predict AQI
6. Evaluate accuracy using R² Score

---

# 📌 Sample Output

The system provides:

✅ Live AQI Monitoring
✅ Health Advisory
✅ AQI Prediction
✅ Pollution Trend Analysis
✅ Interactive Graphs
✅ Correlation Heatmaps
✅ Big Data Analytics
✅ Downloadable Reports

---

# 📊 Results

* Successfully monitored live AQI data
* Implemented machine learning prediction
* Processed large AQI datasets using Dask
* Generated health recommendations
* Visualized pollution trends interactively

---

# 📌 Conclusion

This project demonstrates how Machine Learning, Big Data Analytics, APIs, and Interactive Dashboards can be combined to create an efficient Air Quality Monitoring System.

The system enables:

* Real-time pollution monitoring
* AQI prediction
* Health risk awareness
* Environmental data analysis

By integrating live API data with big data processing and machine learning, the project provides a scalable and intelligent environmental monitoring solution.

---





