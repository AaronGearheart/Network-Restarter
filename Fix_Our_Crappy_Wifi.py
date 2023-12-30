#!/usr/bin/python3


import requests
import RPi.GPIO as GPIO
import time

timeout = 10
server_address = "http://192.168.68.151:5000"  # Use http:// or https:// based on your server

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)

voltage_sent = False

try:
    while True:
        try:
            response = requests.get(server_address, timeout=timeout)

            if response.status_code:
                GPIO.output(21, 1)
                print(f"Server responded. Waiting for 60 seconds. \n Status Code: {response.status_code} \n Response: {response.text}")
                voltage_sent = False
            time.sleep(60)

        except requests.RequestException as e:
            print("Wi-Fi down attempting to send voltage if not sent already")
            if not voltage_sent:
                print("Triggering Relay")
                GPIO.output(21, 0)
                time.sleep(10)
                GPIO.output(21, 1)
                voltage_sent = True
            print("Waiting 60 seconds to test again")
            time.sleep(60)
 
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Cleaning Up and Closing")
