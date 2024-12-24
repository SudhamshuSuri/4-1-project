# Sensor Data and APRS/SSTV Integration

## Introduction

This project integrates multiple sensors with a Python and Shell script workflow to capture, process, and transmit data in the APRS (Automatic Packet Reporting System) format. It also supports generating SSTV (Slow Scan Television) signals using images captured with a camera. The project is designed to collect data from various sensors, log it in a text file, and create SSTV audio waveforms for transmission.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Features

- **Sensor Integration**: Supports BME 680 (environmental data), MPU 9250 (IMU), GPS, magnetometer, and UV sensor.
- **APRS Packet Generation**: Combines sensor readings into APRS-compatible packets.
- **SSTV Signal Creation**: Captures an image with a timestamp and generates Scottie-2 SSTV waveforms.
- **Logging**: Logs sensor data and APRS packets in a text file.
- **Extensibility**: Modular design allows adding new sensors or modifying functionality easily.

## Directory Structure

```plaintext
project/
├── bme680/          # Code and configurations for the BME 680 sensor
├── mpu9250/         # Code and configurations for the MPU 9250 sensor
├── gps/             # Code for GPS data retrieval
├── magnetometer/    # Magnetometer sensor code
├── uv_sensor/       # UV sensor code
├── sstv/            # SSTV image capture and waveform generation
├── aprs.sh          # Shell script for APRS packet generation and logging
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sensor-aprs-sstv.git
   cd sensor-aprs-sstv
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Grant execution permissions to the Shell script:
   ```bash
   chmod +x aprs.sh
   ```

4. Install any required libraries for the sensors (refer to the sensor-specific folders for details).

## Usage

1. **Run the APRS Script**: 
   Execute the Shell script to collect sensor data and generate APRS packets:
   ```bash
   ./aprs.sh
   ```

2. **Generate SSTV Waveforms**:
   Use the SSTV routine to capture an image and create a waveform:
   ```bash
    sstv/sstroutine.sh
   ```

3. **View Logs**:
   Sensor readings and APRS packets are logged in `logs/sensor_data.log`.

## Dependencies

- **Python Libraries**:
  - Sensor-specific libraries (e.g., `Adafruit libraries`)

- **Hardware Requirements**:
  - Sensors: BME 680, MPU 9250, GPS module, magnetometer, UV sensor
  - Camera (for SSTV)

## Examples

- **Sample APRS Packet**:
  ```plaintext
  WIDE2-1>APRS,TCPIP*:!4903.50N/07201.75W_000/000g005t090r000p000h50b10150
  ```

- **Generated SSTV Waveform**:
  - The generated `.wav` file will be saved in the project root as `sstv_<timestamp>.wav`.


## Contributors

- Sudhamshu Suri
- Bhanu Sankar Moturu
