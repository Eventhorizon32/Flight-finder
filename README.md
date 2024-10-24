# Air Quality and Flight Cancellations Tracker

This Python project is a real-time tracking tool that retrieves live data on air quality and flight cancellations at specific locations globally. The program uses the **WAQI (World Air Quality Index)** API for air pollution data and the **AeroDataBox** API for flight status updates, including cancellations.

## Features
- Air Quality Monitoring:
  - Get the current Air Quality Index (AQI) for any location in the world based on geographic coordinates.
  - Detailed information on pollutants like PM2.5, NO2, CO, and more.
  
- Flight Cancellations Tracking:
  - Retrieve real-time data on canceled flights from a specified airport using its ICAO code.
  - Detailed information on canceled flights, including flight number, airline, and scheduled departure times.

## Technologies Used
- Python 
- APIs:
  - [World Air Quality Index (WAQI)](https://waqi.info/) API for air quality data.
  - [AeroDataBox API](https://rapidapi.com/aerodatabox/api/aerodatabox) for flight cancellation data.

## Getting Started

### **Prerequisites**
- Python 3.x installed on your machine.
- API keys:
  - WAQI API Key: You can get one by signing up at [WAQI](https://aqicn.org/data-platform/token/).
  - AeroDataBox API Key: You can get one by signing up on [RapidAPI](https://rapidapi.com/aerodatabox/api/aerodatabox).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/air-quality-flight-cancellations-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd air-quality-flight-cancellations-tracker
   ```
3. Install the required Python packages:
   ```bash
   pip install requests
   ```

### Usage
1. Replace the placeholders `'your_waqi_api_key'` and `'your_aerodatabox_api_key'` with your actual API keys in the `main()` function.

2. Run the program:
   ```bash
   python air_quality_flight_cancellations.py
   ```

3. Follow the on-screen prompts to:
   - Input geographic coordinates (latitude and longitude) to retrieve air quality data.
   - Input an ICAO airport code (e.g., KDFW for Dallas/Fort Worth International Airport) to track flight cancellations.

### Example
1. **Air Quality Input**:
   ```text
   Enter latitude for air quality data (e.g., 32.7767 for Dallas): 32.7767
   Enter longitude for air quality data (e.g., -96.7970 for Dallas): -96.7970
   ```

2. Flight Cancellation Input:
   ```text
   Enter ICAO code for the airport (e.g., KDFW for Dallas/Fort Worth International Airport): KDFW
   ```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to contact me:
- Email: karamimohammadamin754@gmail.com
- GitHub: github.com/Eventhorizon32

