import streamlit as st
import pandas as pd

st.set_page_config(page_title="Industrial Health Monitor")
st.title("🏭 Real-Time Maintenance Dashboard")

df = pd.read_csv('data/sensor_data.csv').tail(50)
st.metric("Current Vibration", f"{df['vibration'].iloc[-1]:.2f} g")

st.subheader("Telemetry Analysis")
st.line_chart(df[['temp', 'vibration']])

if df['vibration'].iloc[-1] > 0.8:
    st.error("⚠️ Maintenance Required Immediately!")
else:
    st.success("✅ System Operating Normally")