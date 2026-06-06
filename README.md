# 🌱 IoT-Based Smart Irrigation System with Edge AI

> **Design and Development of an IoT-Based Embedded System for Smart Irrigation and Real-Time Soil Moisture Monitoring**

![Web Dashboard](Images/web%201.png)
![Mobile Dashboard](Images/Mobile%201.jpeg)
![Local Dashboard](Images/local%202.jpeg)
![Google Sheet](Images/Sheet%20Updating.png)

---

## 📌 Overview

This project presents an intelligent, cost-effective, and fully automated **Smart Irrigation System** that integrates **Internet of Things (IoT)**, **Edge Artificial Intelligence (Edge AI)**, and **Machine Learning** to optimize water usage in agriculture.

The system continuously monitors soil moisture, temperature, humidity, and rainfall using multiple sensors connected to an **ESP32 microcontroller**. A **Random Forest Classifier** (97.98% accuracy) was trained on agricultural data, and the extracted threshold parameters were deployed directly on the ESP32 for on-device intelligent irrigation decisions — without complete dependency on cloud computing.

Real-time data is visualized locally on a **16×2 I2C LCD**, remotely via the **Blynk IoT platform**, and permanently logged to **Google Sheets** via Wi-Fi.

---

## 🏗️ System Architecture

The system is organized into five layers:

```
┌─────────────────────────────────────────┐
│         1. SENSING LAYER                │
│  Soil Moisture | DHT22 | Raindrop       │
├─────────────────────────────────────────┤
│         2. PROCESSING LAYER             │
│        ESP32 Microcontroller            │
│   (Edge AI + Threshold Decision Logic)  │
├─────────────────────────────────────────┤
│         3. OUTPUT LAYER                 │
│      Relay Module → Water Pump          │
├─────────────────────────────────────────┤
│         4. VISUALIZATION LAYER          │
│    Blynk IoT Dashboard | 16×2 LCD       │
├─────────────────────────────────────────┤
│      5. DATA LOGGING LAYER              │
│   Google Sheets via Google Web Script   │
└─────────────────────────────────────────┘
```

---

## ✨ Features

- ✅ **Automated Irrigation** — Pump turns ON/OFF based on real-time sensor data and ML-derived thresholds
- ✅ **Edge AI Decision Making** — Random Forest model thresholds deployed directly on ESP32 (no cloud dependency)
- ✅ **Multi-Sensor Monitoring** — Soil moisture, temperature, humidity, and rainfall detection
- ✅ **Remote Monitoring** — Real-time dashboard via Blynk IoT (mobile + web)
- ✅ **Local Display** — 16×2 I2C LCD for field-level monitoring without internet
- ✅ **Wireless Data Logging** — Automatic logging to Google Sheets via HTTP GET requests
- ✅ **97.98% ML Accuracy** — Trained on government open-data agricultural datasets

---

## 🛠️ Hardware Components

| Component | Description |
|-----------|-------------|
| ESP32 Dev Board | Main microcontroller (Dual-core, Wi-Fi + Bluetooth) |
| Resistive Soil Moisture Sensor | Measures soil water content via resistance change |
| DHT22 Sensor | Measures temperature and humidity |
| Raindrop Sensor | Detects presence and intensity of rainfall |
| Relay Module | Electrically switches the water pump ON/OFF |
| Mini Water Pump | Supplies water to the field/plant |
| 16×2 I2C LCD Display | Local real-time display of sensor readings |
| Breadboard + Jumper Wires | Circuit connections |

---

## 📌 Circuit Connections (ESP32 GPIO Pin Mapping)

| Sensor / Component | ESP32 GPIO Pin |
|--------------------|---------------|
| Soil Moisture Sensor | GPIO 34 (ADC Input-only) |
| DHT22 Sensor | GPIO 15 |
| Raindrop Sensor | GPIO 35 (ADC Input-only) |
| Relay Module | GPIO 23 |
| LCD SDA (I2C) | GPIO 21 |
| LCD SCL (I2C) | GPIO 22 |

---

## 💻 Software & Tools

| Tool | Purpose |
|------|---------|
| MicroPython | ESP32 programming language |
| Thonny IDE | Code writing, uploading, and serial monitor |
| Google Colab | ML model training and threshold extraction |
| Python (scikit-learn) | Random Forest Classifier training |
| Blynk IoT Platform | Remote monitoring dashboard |
| Google Sheets + Web Script | Wireless cloud-based data logging |

---

## 🤖 Machine Learning Model

- **Algorithm:** Random Forest Classifier (`n_estimators=50`)
- **Dataset:** Agricultural data from [data.gov.in](https://www.data.gov.in/)
- **Features Used:** Soil Moisture, Temperature, Humidity
- **Target:** Pump Status (ON / OFF)
- **Model Accuracy:** **97.98%**
- **Train/Test Split:** 80% / 20%

### Extracted Threshold Values (for Pump OFF condition):
```
soil_moisture  >= 63.5 %
temperature    <= 29.5 °C
humidity       >= 45.5 %
```
These thresholds are implemented directly in the ESP32 firmware for on-device decisions.

---

## ⚙️ Irrigation Control Logic

```
IF rainfall detected:
    → Turn Pump OFF  (avoid unnecessary irrigation)

ELSE IF soil_moisture < 63.5%:
    → Turn Pump ON   (soil is dry, irrigation needed)

ELSE IF soil_moisture >= 63.5% AND (temperature <= 29.9 OR humidity >= 45.5):
    → Turn Pump OFF  (conditions are adequate)

ELSE IF soil_moisture >= 70%:
    → Turn Pump OFF  (sufficient moisture)

ELSE:
    → Turn Pump ON
```

---

## 📁 Repository Structure

```
Smart_Irrigation_System/
│
├── main.py                  # Main ESP32 MicroPython firmware
├── BlynkLib.py              # Blynk library for MicroPython
├── i2c_lcd.py               # I2C LCD driver library
│
├── ML_Model/
│   ├── model_training.py    # Random Forest training script
│   ├── threshold_extraction.py  # Threshold parameter extraction
│   └── Trained_model.pkl    # Saved trained model
│
├── Google_Script/
│   └── google_web_script.js # Google Apps Script for Sheets logging
│
├── Dataset/
│   └── Processed_data.csv   # Preprocessed agricultural dataset
│
├── Circuit_Diagram/
│   └── connections.png      # Complete circuit diagram
│
├── Results/
│   ├── lcd_monitoring.jpg
│   ├── blynk_dashboard.jpg
│   └── google_sheets_log.jpg
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Flash MicroPython on ESP32
Download MicroPython firmware from [micropython.org](https://micropython.org/download/esp32/) and flash it using `esptool`.

### 2. Install Thonny IDE
Download from [thonny.org](https://thonny.org/) and configure it for MicroPython on ESP32.

### 3. Upload Required Files
Upload the following files to the ESP32 root directory using Thonny:
- `main.py`
- `BlynkLib.py`
- `i2c_lcd.py`

### 4. Configure Credentials in `main.py`
```python
WIFI_SSID = "your_wifi_name"
WIFI_PASS = "your_wifi_password"
BLYNK_AUTH = "your_blynk_auth_token"
```

### 5. Set Up Blynk Dashboard
- Create a free account at [blynk.cloud](https://blynk.cloud)
- Add Virtual Pin widgets: V0 (Soil Moisture), V1 (Temperature), V2 (Humidity), V3 (Rainfall), V4 (Pump Status)

### 6. Set Up Google Sheets Logging
- Create a Google Spreadsheet with sheet named `sensor_data`
- Open Apps Script, paste the code from `Google_Script/google_web_script.js`
- Deploy as a Web App (access: Anyone) and copy the deployment URL into `main.py`

### 7. Train the ML Model (Optional)
Run `ML_Model/model_training.py` on Google Colab with your dataset, then run `threshold_extraction.py` to get threshold values.

---

## 📊 Results Summary

| Parameter | Result |
|-----------|--------|
| ML Model Accuracy | 97.98% |
| Temperature Range Tested | 27°C – 43°C |
| Humidity Range Tested | 21% – 55% |
| Soil Moisture Threshold | 63.5% |
| Data Logging | Wireless (Google Sheets) |
| Monitoring | Local (LCD) + Remote (Blynk) |

---

## 📱 Screenshots

| Local LCD Monitoring | Blynk Mobile Dashboard | Blynk Web Dashboard | Google Sheets Log |
|---|---|---|---|
| *(See Results folder)* | *(See Results folder)* | *(See Results folder)* | *(See Results folder)* |

---

## 🔮 Future Scope

- Integration of soil pH, nutrient, and light intensity sensors
- Weather forecast API integration for predictive irrigation
- Solar-powered operation for remote areas
- Dedicated mobile application with push notifications
- Expansion to large-scale commercial farming with LoRa communication
- Adaptive/self-learning irrigation models

---

## 📄 Publication / Academic Details

| Field | Details |
|-------|---------|
| Author | Rohit Kumar Malah (Y24273022) |
| Supervisor | Prof. Ashish Verma |
| Degree | M.Sc. Physics (2024–26) |
| Department | Department of Physics |
| University | Dr. Hari Singh Gour Vishwavidyalaya, Sagar (M.P.) — A Central University |

---

## 📚 References

Key references used in this project:

1. Nikita Jaiswal et al. (2025) — Smart drip irrigation using IoT & ML — *Springer Nature*
2. Arafat Islam et al. (2026) — Sensor-driven ML framework for sustainable agriculture — *Atlantis Press*
3. Upendra Roy B.P et al. (2024) — Smart irrigation with IoT & Random Forest — *Journal of Smart IoT*
4. G.S. Prasanna Lakshmi et al. (2023) — IoT sensor coupled precision irrigation model — *Measurement: Sensors*

---

## 📬 Contact

**Rohit Kumar Malah**<br>
M.Sc. Physics Student<br>
Dr. Hari Singh Gour Vishwavidyalaya, Sagar (M.P.)<br>
GitHub: [@malahrk57](https://github.com/malahrk57)<br>

---

> ⭐ *If you found this project helpful, please give it a star!*