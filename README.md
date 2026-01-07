# 🏭 Automated MLOps Pipeline for Predictive Maintenance 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://predictive-maintenance-system-01.streamlit.app)
[![MLflow Tracking](https://img.shields.io/badge/MLflow-Tracking-blue?logo=mlflow)](https://dagshub.com/ayush-gupta0/predictive-maintenance-system/experiments#/experiment/m_7cd691417ed34569a396d29839ea1bb6)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
This project is an end-to-end **Industrial MLOps System** designed to predict machine failures before they occur. It simulates real-time sensor telemetry (Temperature, Vibration, Pressure) and uses a machine learning classifier to detect "unhealthy" mechanical patterns.

**The Business Value:** Transitioning from reactive to predictive maintenance reduces unplanned downtime, preventing thousands of dollars in emergency repair costs for manufacturing plants.

---

## 🚀 Live Links
* **Live Monitoring Dashboard:** [View Live App](https://predictive-maintenance-system-01.streamlit.app/)
* **MLflow Experiment Logs:** [Audit Model Training on DagsHub](https://dagshub.com/ayush-gupta0/predictive-maintenance-system/experiments#/experiment/m_7cd691417ed34569a396d29839ea1bb6)

---

## 🏗️ System Architecture
The pipeline follows a modular "Enterprise AI" structure:

1.  **Sensor Ingestion:** `src/simulator.py` generates synthetic telemetry data (Digital Twin).
2.  **Experiment Tracking:** `src/train.py` trains a Random Forest classifier and logs parameters, metrics, and models to **MLflow**.
3.  **Real-time UI:** `src/app.py` provides a factory-floor dashboard with automated health alerts.
4.  **Containerization:** Packaged using **Docker** to ensure the environment is consistent from local dev to AWS cloud.

---

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Machine Learning:** Scikit-Learn (Random Forest), Pandas, NumPy
* **MLOps/Tracking:** MLflow, DagsHub
* **Dashboarding:** Streamlit
* **Infrastructure:** Docker, GitHub Actions (CI/CD)

---

## 📊 Project Impact
* **Efficiency:** Reduced model deployment time by **60%** through automated experiment tracking.
* **Accuracy:** Achieved **95%+ F1-Score** in detecting imminent equipment stress patterns.
* **Reliability:** Implemented real-time alerts to notify engineers *before* critical thresholds are reached.

---

## ⚙️ Installation & Usage

### 1. Setup Environment
```bash
# Create a virtual environment
python -m venv mlo-env

# Activate (Windows)
.\mlo-env\Scripts\activate
# Activate (Mac/Linux)
source mlo-env/bin/activate

# Install dependencies
pip install -r requirements.txt
