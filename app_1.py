# app_2.py
# BIG DATA STYLE AQI DASHBOARD WITHOUT JAVA / PYSPARK
# Uses Dask (Parallel Big Data Processing)

import streamlit as st
import pandas as pd
import numpy as np
import dask.dataframe as dd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌍 AQI Big Data Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🌍 AQI Big Data Analytics Dashboard")
st.markdown("### Big Data AQI Analysis using Dask + Machine Learning")

# ---------------- LOAD DATA USING DASK ----------------
@st.cache_data
def load_data():
    df = dd.read_csv(
        "aqi_data.csv",
        dtype={
            "AQI_Bucket": "object"
        }
    )
    return df.compute()

df = load_data()

# ---------------- DATA CLEANING ----------------
numeric_cols = [
    "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3", "AQI"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.fillna(df.mean(numeric_only=True), inplace=True)

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔍 Filters")

cities = sorted(df["City"].dropna().unique())

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

filtered_df = df[df["City"] == selected_city]

# ---------------- AQI CATEGORY ----------------
def aqi_category(aqi):
    if aqi <= 50:
        return "🟢 Good"
    elif aqi <= 100:
        return "🟡 Satisfactory"
    elif aqi <= 200:
        return "🟠 Moderate"
    elif aqi <= 300:
        return "🔴 Poor"
    elif aqi <= 400:
        return "🟣 Very Poor"
    else:
        return "⚫ Severe"

# ---------------- HEALTH ADVICE ----------------
def health_advice(aqi):
    if aqi <= 50:
        return "Air quality is excellent and safe."
    elif aqi <= 100:
        return "Air quality is acceptable."
    elif aqi <= 200:
        return "Sensitive groups should reduce outdoor activity."
    elif aqi <= 300:
        return "Wear masks outdoors."
    elif aqi <= 400:
        return "Avoid outdoor activities."
    else:
        return "Health emergency condition."

# ---------------- CURRENT AQI ----------------
latest = filtered_df.iloc[-1]

aqi_value = latest["AQI"]

st.subheader(f"📍 Current AQI Status - {selected_city}")

col1, col2, col3 = st.columns(3)

col1.metric("AQI", round(aqi_value, 2))
col2.metric("Category", aqi_category(aqi_value))
col3.metric("PM2.5", round(latest["PM2.5"], 2))

# ---------------- HEALTH ADVISORY ----------------
st.subheader("🩺 Health Advisory")

st.info(health_advice(aqi_value))

# ---------------- AQI TREND ----------------
st.subheader("📈 AQI Trend Analysis")

fig1 = px.line(
    filtered_df,
    x="Date",
    y="AQI",
    title=f"AQI Trend - {selected_city}",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- POLLUTANT ANALYSIS ----------------
st.subheader("🧪 Pollutant Analysis")

pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

avg_pollution = filtered_df[pollutants].mean()

fig2 = px.bar(
    x=avg_pollution.index,
    y=avg_pollution.values,
    labels={"x": "Pollutants", "y": "Average Value"},
    title="Average Pollutant Levels"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- CORRELATION HEATMAP ----------------
st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[numeric_cols].corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- AQI DISTRIBUTION ----------------
st.subheader("📊 AQI Distribution")

fig4 = px.histogram(
    filtered_df,
    x="AQI",
    nbins=30,
    title="AQI Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------- BIG DATA ANALYTICS ----------------
st.subheader("⚡ Big Data Analytics")

summary_df = df.groupby("City")["AQI"].agg(
    ["mean", "max", "min"]
).reset_index()

summary_df.columns = [
    "City",
    "Average AQI",
    "Maximum AQI",
    "Minimum AQI"
]

st.dataframe(summary_df)

# ---------------- MACHINE LEARNING ----------------
st.subheader("🤖 AQI Prediction using Random Forest")

ml_df = filtered_df.dropna()

features = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

X = ml_df[features]
y = ml_df["AQI"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = r2_score(y_test, predictions)

st.success(f"✅ Model Accuracy: {round(accuracy * 100, 2)}%")

# ---------------- FEATURE IMPORTANCE ----------------
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

fig5 = px.bar(
    importance,
    x="Feature",
    y="Importance",
    title="Feature Importance"
)

st.plotly_chart(fig5, use_container_width=True)

# ---------------- AQI PREDICTION ----------------
st.subheader("🔮 Predict AQI")

pm25 = st.slider("PM2.5", 0.0, 500.0, 80.0)
pm10 = st.slider("PM10", 0.0, 500.0, 100.0)
no2 = st.slider("NO2", 0.0, 300.0, 40.0)
so2 = st.slider("SO2", 0.0, 300.0, 20.0)
co = st.slider("CO", 0.0, 200.0, 10.0)
o3 = st.slider("O3", 0.0, 300.0, 50.0)

future_data = np.array([[
    pm25,
    pm10,
    no2,
    so2,
    co,
    o3
]])

predicted_aqi = model.predict(future_data)[0]

st.metric("Predicted AQI", round(predicted_aqi, 2))

st.write("Category:", aqi_category(predicted_aqi))

st.warning(health_advice(predicted_aqi))

# ---------------- DOWNLOAD DATA ----------------
st.subheader("📥 Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    file_name="aqi_processed_data.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
### 🌟 Features

✅ Big Data Processing using Dask  
✅ AQI Monitoring  
✅ Health Advisory  
✅ Machine Learning Prediction  
✅ Interactive Graphs  
✅ Correlation Analysis  
✅ Download Reports  

### 🛠 Technologies Used

- Python
- Streamlit
- Dask
- Pandas
- Plotly
- Scikit-learn

### 📌 Outcome

This system analyzes AQI trends, predicts pollution levels,
and provides health recommendations using Big Data Analytics.
""")