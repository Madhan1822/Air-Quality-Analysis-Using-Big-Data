import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Real-Time AQI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------- API KEY ----------------
API_KEY = "99baf05a5fecf569035d37467ff88ea3"   # ACTIVE KEY ONLY

# ---------------- TITLE ----------------
st.title("🌍 Real-Time Air Quality Index (AQI) Dashboard")
st.markdown("Live AQI monitoring using OpenWeatherMap Air Pollution API")

st.info("Enter a **valid CITY name** (example: Delhi, Chennai, Coimbatore)")

# ---------------- CITY INPUT ----------------
city = st.text_input("🏙️ Enter City Name", "Coimbatore").strip()

# ---------------- FUNCTIONS ----------------
def get_coordinates(city):
    # Reject very short or invalid inputs early
    if len(city) < 3:
        return None, None, None

    url = (
        f"https://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}&limit=1&appid={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None, None, None

    data = response.json()

    # No results
    if not data:
        return None, None, None

    result = data[0]

    # Strict city validation
    if "name" not in result:
        return None, None, None

    if result["name"].lower() != city.lower():
        return None, None, None

    return result["lat"], result["lon"], result["name"]


def get_aqi(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

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


def health_advisory(aqi):
    if aqi <= 2:
        return "✅ Air quality is acceptable. Enjoy outdoor activities."
    elif aqi == 3:
        return "⚠️ Sensitive groups should limit prolonged outdoor exposure."
    else:
        return "❌ Unhealthy air quality. Avoid outdoor exercise and wear masks."


# ---------------- FETCH DATA ----------------
lat, lon, valid_city = get_coordinates(city)

if lat is None:
    st.error("❌ Invalid city name. Please enter a REAL city (e.g., Delhi, Chennai).")
    st.stop()

data = get_aqi(lat, lon)

if not data or "list" not in data:
    st.error("❌ AQI data unavailable at the moment.")
    st.stop()

aqi_value = data["list"][0]["main"]["aqi"]
components = data["list"][0]["components"]
timestamp = datetime.fromtimestamp(data["list"][0]["dt"])

# ---------------- KPI METRICS ----------------
st.subheader(f"📍 Live AQI Summary – {valid_city}")

col1, col2, col3 = st.columns(3)
col1.metric("AQI Index", aqi_value)
col2.metric("AQI Category", aqi_category(aqi_value))
col3.metric("Last Updated", timestamp.strftime("%Y-%m-%d %H:%M:%S"))

# ---------------- HEALTH ADVISORY ----------------
st.subheader("🩺 Health Advisory")
st.write(health_advisory(aqi_value))

# ---------------- POLLUTANTS ----------------
st.subheader("🧪 Pollutant Concentrations (µg/m³)")

pollutants_df = pd.DataFrame.from_dict(
    components, orient="index", columns=["Concentration"]
)

st.bar_chart(pollutants_df)

# ---------------- SESSION TREND ----------------
st.subheader("📈 AQI Trend (Current Session)")

if "aqi_history" not in st.session_state:
    st.session_state["aqi_history"] = []

st.session_state["aqi_history"].append({
    "Time": timestamp,
    "AQI": aqi_value
})

history_df = pd.DataFrame(st.session_state["aqi_history"])
st.line_chart(history_df.set_index("Time"))

# ---------------- RAW DATA ----------------
with st.expander("📄 View AQI History Data"):
    st.dataframe(history_df)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
**Project:** Real-Time Air Quality Monitoring System  

**Technologies Used:**  
Python, Streamlit, REST API, Pandas  

**Outcome:**  
• Live AQI monitoring  
• Health impact analysis  
• Pollution trend identification  
• Data-driven environmental awareness  

**Data Source:** OpenWeatherMap Air Pollution API
""")
