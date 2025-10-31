# skeleton code from: https://randomnerdtutorials.com/raspberry-pi-bme280-python/

import RPi.GPIO as GPIO
import time
import smbus2
import bme280

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.out, initial=GPIO.LOW)   # RED
GPIO.setup(10, GPIO.out, initial=GPIO.LOW)  # BLUE

# BME280 sensor address (default address)
address = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)

        # Extract temperature, pressure, and humidity
        temperature_celsius = data.temperature
        pressure = data.pressure
        humidity = data.humidity

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)

        # Print the readings
        print("Temperature: {:.2f} °C, {:.2f} °F".format(temperature_celsius, temperature_fahrenheit))
        print("Pressure: {:.2f} hPa".format(pressure))
        print("Humidity: {:.2f} %".format(humidity))

        if (temperature_celsius > 20):
            print("It is hot.")
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
        else:
            print("It is cold.")
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.HIGH)

        
        # Wait for a few seconds before the next reading
        time.sleep(2)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break