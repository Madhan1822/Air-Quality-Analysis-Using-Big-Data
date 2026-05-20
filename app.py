import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌍 Real-Time AQI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------- API KEY ----------------
API_KEY = "99baf05a5fecf569035d37467ff88ea3"  # Replace with your active AQI API key

# ---------------- TITLE ----------------
st.title("🌍 Real-Time Air Quality Index (AQI) Dashboard")
st.markdown("Live AQI monitoring using OpenWeatherMap Air Pollution API")
st.caption("Enter a CITY name (example: Delhi, Chennai, Coimbatore)")

# ---------------- CITY INPUT ----------------
city = st.text_input("🏙️ Enter City Name", "Coimbatore")

# ---------------- FUNCTIONS ----------------
def get_coordinates(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city},IN&limit=1&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None
    data = response.json()
    if not data or len(data) == 0:
        return None, None
    return data[0]["lat"], data[0]["lon"]

def get_aqi(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def aqi_category(aqi):
    return {
        1: "🟢 Good",
        2: "🟡 Fair",
        3: "🟠 Moderate",
        4: "🔴 Poor",
        5: "🟣 Very Poor"
    }.get(aqi, "Unknown")

def health_advice(aqi):
    if aqi <= 2:
        return "Air quality is safe for all age groups."
    elif aqi == 3:
        return "Children and elderly should limit prolonged outdoor activity."
    else:
        return "Unhealthy air quality. Avoid outdoor exercise and use masks."

# ---------------- FETCH DATA ----------------
lat, lon = get_coordinates(city)
if lat is None:
    st.error("❌ City not found or API issue. Try another CITY.")
    st.stop()

data = get_aqi(lat, lon)
if not data or "list" not in data or not data["list"]:
    st.error("❌ AQI data unavailable at the moment.")
    st.stop()

aqi_value = data["list"][0]["main"].get("aqi")
components = data["list"][0].get("components")
timestamp = datetime.fromtimestamp(data["list"][0]["dt"])

if components is None:
    st.error("❌ Pollutant data unavailable at the moment.")
    st.stop()

# ---------------- KPI METRICS ----------------
st.subheader(f"📍 Live AQI Summary – {city}")
col1, col2, col3 = st.columns(3)
col1.metric("AQI Index", aqi_value)
col2.metric("AQI Category", aqi_category(aqi_value))
col3.metric("Last Updated", timestamp.strftime("%Y-%m-%d %H:%M:%S"))

# ---------------- HEALTH ADVISORY ----------------
st.subheader("🩺 Health Advisory")
st.info(health_advice(aqi_value))

# ---------------- POLLUTANTS ----------------
st.subheader("🧪 Pollutant Concentrations (µg/m³)")
pollutant_colors = {}
for pollutant, value in components.items():
    color = "🟢"
    if value > 150:
        color = "🔴"
    elif value > 50:
        color = "🟠"
    pollutant_colors[pollutant.upper()] = color
    st.write(f"**{pollutant.upper()}**: {value} {color}")

st.bar_chart(pd.DataFrame.from_dict(components, orient="index", columns=["Value"]))

# ---------------- MAP ----------------
st.subheader("🗺️ Location Map")
st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

# ---------------- SESSION TREND ----------------
if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append({"Time": timestamp, "AQI": aqi_value})
history_df = pd.DataFrame(st.session_state.history)

st.subheader("📈 AQI Trend (Current Session)")
st.line_chart(history_df.set_index("Time")["AQI"])

# ---------------- SIMPLE TREND PREDICTION ----------------
if len(history_df) > 2:
    X = np.arange(len(history_df)).reshape(-1, 1)
    y = history_df["AQI"].values
    model = LinearRegression().fit(X, y)
    future_idx = np.arange(len(history_df), len(history_df)+3).reshape(-1, 1)
    predictions = model.predict(future_idx)
    future_df = pd.DataFrame({
        "Time": ["T+1", "T+2", "T+3"],
        "Predicted AQI": predictions
    })
    st.subheader("🔮 AQI Predictions (Next 3 Points)")
    st.line_chart(future_df.set_index("Time"))

# ---------------- DOWNLOAD SESSION DATA ----------------
csv = history_df.to_csv(index=False)
st.download_button("📥 Download Session AQI Data", csv, "aqi_history.csv")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
**Project:** Real-Time Air Quality Monitoring System  

**Technologies Used:**  
Python, Streamlit, REST API, Pandas, Scikit-learn  

**Outcome:**  
• Live AQI monitoring  
• Health impact analysis  
• Pollution trend identification  
• Session-based prediction  
• Data-driven environmental awareness  

**Data Source:** OpenWeatherMap Air Pollution API
""")