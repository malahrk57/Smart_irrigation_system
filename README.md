# Smart_irrigation_system
Agriculture requires efficient water management to improve crop productivity
and reduce water wastage. In this project, an IoT-Based embedded system for
smart irrigation and real-time soil moisture monitoring is designed to improve
irrigation efficiency. The system uses an ESP32 Dev Board microcontroller
along with a Soil Moisture sensor, DHT22 (Temperature and Humidity Sensor), and a Raindrop sensor to monitor field conditions continuously. The system is supported by Edge-AI for predicting the status of the water pump under
varying environmental conditions. It automatically checks the soil moisture
level and other parameters and controls the water pump through a relay module whenever irrigation is required. This reduces water wastage and improves
crop productivity. A 16x2 I2C LCD module displays sensor readings directly in
the field for easy local monitoring.The system is connected with the Blynk IoT
platform, which allows users to monitor soil moisture and other environmental
parameters in real-time using a web dashboard or mobile phone. The system
is simple, cost-effective, and energy-efficient, making it suitable for real-time
agriculture applications.A Random Forest Classifier was trained using publicly
available agricultural datasets, achieving a model accuracy of 97.98%. The
extracted threshold parameters from this model were implemented directly on
the ESP32 microcontroller, enabling intelligent on-device irrigation decisions
without complete dependency on cloud computing. In addition to real-time
monitoring and automated irrigation control, the system supports wireless sensor data logging directly to Google Sheets via Wi-Fi. Sensor readings, including soil moisture, temperature, humidity, rainfall status, and pump status, are
transmitted wirelessly from the ESP32 to a Google Spreadsheet using Google
Web Script. This eliminates the need for a USB-connected computer and enables cloud-based historical data access from anywhere, supporting long-term
trend analysis, system performance evaluation, and future machine learning
model development