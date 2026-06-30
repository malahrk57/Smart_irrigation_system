# WiFi Credentials
WIFI_SSID = "vivo T2x 5G"
WIFI_PASS = "ROHIT@7898"


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
