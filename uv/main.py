import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

# Initialize I2C bus and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Define gain for reading (adjust as necessary)
GAIN = 1

# Set up analog inputs for sensors
uv_sensor = AnalogIn(ads, ADS.P0)  # UV sensor connected to A0
thermistor1 = AnalogIn(ads, ADS.P1)  # Thermistor 1 connected to A1
thermistor2 = AnalogIn(ads, ADS.P2)  # Thermistor 2 connected to A2

while True:
    # Read values from sensors
    uv_value = uv_sensor.voltage  # Read UV sensor voltage
    thermistor1_value = thermistor1.voltage  # Read first thermistor voltage
    thermistor2_value = thermistor2.voltage  # Read second thermistor voltage
    
    # Print readings
    print(f"UV Sensor Voltage: {uv_value:.2f} V")
    print(f"Thermistor 1 Voltage: {thermistor1_value:.2f} V")
    print(f"Thermistor 2 Voltage: {thermistor2_value:.2f} V")

    time.sleep(1)  # Delay for a second before next reading

