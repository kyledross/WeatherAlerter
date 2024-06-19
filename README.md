# WeatherAlerter  
A Python-based weather alert utility.  
Copyright 2024 Kyle D. Ross  
See LICENSE.md for licensing information

## Warning  

This program is for demonstration and learning purposes only, and is not intended to be your sole source of inclement weather information.

**_DO NOT RELY UPON THIS PROGRAM FOR THE SAFETY OF ANYONE OR ANYTHING!_**

### Purpose  

The purpose of this program is to:
- be a personal learning platform for Python,
- be a practical utility for myself,
- be a reference or starting point for others with the same interests

### Requirements
- Python 3.11 or later
- An internet connection

### Optional
- Raspberry Pi Sense HAT

### Setup
```commandline
sudo apt install python3-dateutil
sudo apt install python3-requests
git clone https://github.com/kyledross/WeatherAlerter
cd WeatherAlerter
```



#### Additional Setup for Raspberry Pi Sense HAT
Enable the I2C interface on the Raspberry Pi using 
```commandline
sudo raspi-config
sudo apt install python3-sense-hat
```

#### Additional Setup for Raspberry Pi Sense HAT Emulator
```commandline
sudo apt install python3-sense-emu
sudo apt install python3-PyGObject
```

### Usage
For usage information:
```commandline
python3 main.py --help
```

### Credits
#### Zone-County Correlation File (./Data/bp05mr24.dbx.txt)
This file contains the zone-county correlation data for the US, and was obtained from:  
US Dept of Commerce  
National Oceanic and Atmospheric Administration  
National Weather Service  
GIS  
https://www.weather.gov/gis/ZoneCounty
