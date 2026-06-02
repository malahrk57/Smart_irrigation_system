import serial
import csv
from datetime import datetime

ser = serial.Serial('COM4', 115200)   # Change COM port

with open(r'D:\Final_year_Project\Dataset\sensor_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    # Header (only first time)
    writer.writerow([
        "Timestamp",
        "Temperature",
        "Humidity",
        "Soil Moisture",
        "Rain Status",
        "Pump Status"
    ])

    while True:
        try:
            line = ser.readline().decode().strip()

            data = line.split(',')

            if len(data) == 5:
                writer.writerow([
                    datetime.now(),
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4]
                ])
                file.flush()
                print("Saved:", data)

        except Exception as e:
            print(e)