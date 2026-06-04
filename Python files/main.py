import network
import time
from machine import Pin, ADC,SoftI2C
import dht
import BlynkLib
from i2c_lcd import I2cLcd
import urequests

#I2C LCD setup
i2c = SoftI2C(scl=Pin(22), sda = Pin(21))
lcd = I2cLcd(i2c, 0x27, 2,16)

# WiFi Credentials
WIFI_SSID = "GalaxyM55"
WIFI_PASS = "12345678"

# Blynk Auth Token
BLYNK_AUTH = "PiE7CYRuLPgVNKiVj2BkD7B7yGmTn_9n"

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(False)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
print("Connecting to WiFi...", end="")


while not wifi.isconnected():
    print(".", end="")
    time.sleep(1)
print("\nWiFi Connected:", wifi.ifconfig())


# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)


# Sensors Setup
dht_sensor = dht.DHT22(Pin(15))
soil_sensor = ADC(Pin(34))
soil_sensor.atten(ADC.ATTN_11DB)
rain_sensor = Pin(35, Pin.IN)
relay = Pin(23, Pin.OUT)

# Main Loop
while True:
    blynk.run()
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        soil_value = soil_sensor.read()
        rain_value = rain_sensor.value()
        relay_status = relay.value()
        soil_percent = ((4095-soil_value)/4095) * 100
        
        # control logic
        if rain_value == 1:
            rain_status = "No"
            if soil_percent >= 63.50 :
                if temperature <= 29.9 or humidity >= 45.5 :
                    relay.value(0)
                    pump_status = "OFF"
                else:
                    if soil_percent >= 70:
                        relay.value(0)
                        pump_status = "OFF"
            else:
                relay.value(1)
                pump_status = "ON"
        else:
            rain_status = "Yes"
            relay.value(0)
            pump_status = "OFF"

        # Send to Blynk
        blynk.virtual_write(0, soil_percent)
        blynk.virtual_write(1, temperature)
        blynk.virtual_write(2, humidity)
        blynk.virtual_write(3, rain_status)
        blynk.virtual_write(4, pump_status)
       
        #Display on LCD
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("T:{:.1f}C H:{:.1f}%".format(temperature, humidity))
        lcd.move_to(0,1)
        lcd.putstr("S:{:.1f}% P:{}".format(soil_percent,pump_status))
        
        
        # Send data to spreadsheet
        url = "https://script.google.com/macros/s/AKfycbwNKdx8CWydvWqR33dxl9PQ96BkUR86gc7Z40FbP3QmUMQKNMR3wLZnNAjcnZH772o91Q/exec?soil={}&temp={}&hum={}&rainfall={}&pumpstatus={}".format(
    soil_percent,
    temperature,
    humidity,
    rain_status,
    pump_status
)

        response = urequests.get(url)
        print(response.text)
        response.close()
        
    except Exception as e:
        print("Sensor error:",e)

time.sleep(10)






