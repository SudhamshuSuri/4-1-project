import time
import smbus
import math
import board
import adafruit_bme680
from aprs import APRSPacket

# Create I2C objects for the sensors
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# HMC5883L Magnetometer setup
HMC5883L_ADDRESS = 0x1E
HMC5883L_CONFIG_A = 0x00
HMC5883L_CONFIG_B = 0x01
HMC5883L_MODE = 0x02
HMC5883L_X_MSB = 0x03
HMC5883L_Y_MSB = 0x07
HMC5883L_Z_MSB = 0x05

bus = smbus.SMBus(1)

# BME680 setup
bme680.sea_level_pressure = 1013.25
temperature_offset = -5

# HMC5883L setup function
def hmc5883l_setup():
    bus.write_byte_data(HMC5883L_ADDRESS, HMC5883L_CONFIG_A, 0x70)  # 8 samples @ 15Hz
    bus.write_byte_data(HMC5883L_ADDRESS, HMC5883L_CONFIG_B, 0x20)  # 1.3 gain (LSb/Gauss)
    bus.write_byte_data(HMC5883L_ADDRESS, HMC5883L_MODE, 0x00)  # Continuous mode

def hmc5883l_read_raw_data(addr):
    high = bus.read_byte_data(HMC5883L_ADDRESS, addr)
    low = bus.read_byte_data(HMC5883L_ADDRESS, addr+1)
    value = (high << 8) + low
    if value > 32768:
        value = value - 65536
    return value

def hmc5883l_compute_heading(x, y):
    heading_rad = math.atan2(y, x)
    declination_angle = 0.22  # Adjust based on location
    heading_rad += declination_angle
    
    if heading_rad < 0:
        heading_rad += 2 * math.pi
    if heading_rad > 2 * math.pi:
        heading_rad -= 2 * math.pi
        
    heading_deg = heading_rad * (180.0 / math.pi)
    return heading_deg

# BME680 sensor data read function
def read_bme680_data():
    temperature = bme680.temperature + temperature_offset
    gas = bme680.gas
    humidity = bme680.relative_humidity
    pressure = bme680.pressure
    altitude = bme680.altitude
    return temperature, gas, humidity, pressure, altitude

# Function to create and print APRS packet
def create_aprs_packet(temperature, gas, humidity, pressure, altitude, heading):
    aprs_data = f"Temperature:{temperature}C Gas:{gas} Humidity:{humidity}% Pressure:{pressure}hPa Altitude:{altitude}m Heading:{heading:.2f}°"
    
    # APRS Packet creation with your callsign and position (can be changed)
    packet = APRSPacket(
        callsign='YOURCALL',  # Replace with your APRS callsign
        symbol='/O',          # Replace with your symbol for objects (can be '/O' or others)
        latitude=37.7749,     # Example: latitude (should be your actual position)
        longitude=-122.4194,  # Example: longitude (should be your actual position)
        comment=aprs_data     # This is the sensor data you want to send
    )
    
    # Print the APRS packet in the terminal
    print("APRS Packet:")
    print(packet)

# Main function to run every 10 seconds
def main():
    hmc5883l_setup()
    while True:
        # Read BME680 sensor data
        bme_temperature, gas, humidity, pressure, altitude = read_bme680_data()

        # Read HMC5883L magnetometer data
        x = hmc5883l_read_raw_data(HMC5883L_X_MSB)
        y = hmc5883l_read_raw_data(HMC5883L_Y_MSB)
        z = hmc5883l_read_raw_data(HMC5883L_Z_MSB)
        heading = hmc5883l_compute_heading(x, y)

        # Create and print APRS packet
        create_aprs_packet(bme_temperature, gas, humidity, pressure, altitude, heading)

        # Wait for 10 seconds before reading data again
        time.sleep(10)

if __name__ == "__main__":
    main()
