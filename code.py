import requests

# Function to get live air quality data from WAQI API using coordinates
def get_air_quality_waqi_by_coordinates(api_key, lat, lon):
    url = f"http://api.waqi.info/feed/geo:{lat};{lon}/?token={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            air_quality = data['data']
            if isinstance(air_quality, dict):  # Ensure air_quality is a dictionary
                return {
                    "Location": f"Coordinates ({lat}, {lon})",
                    "AQI": air_quality.get('aqi', 'N/A'),
                    "Dominant Pollutant": air_quality.get('dominentpol', 'N/A'),
                    "Pollutants": air_quality.get('iaqi', {})
                }
            else:
                return f"Unexpected response format: {air_quality}"
        else:
            return f"Invalid response format from WAQI API: {data}"
    else:
        return f"Error fetching air quality data from WAQI: {response.status_code} - {response.text}"

# Function to get live flight cancellation data from AviationStack API
def get_flight_cancellations(api_key):
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&flight_status=canceled"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data:
            cancellations = data['data']
            return {
                "Total Cancellations": len(cancellations),
                "Flight Details": cancellations
            }
        else:
            return "Invalid response format from AviationStack API"
    else:
        return f"Error fetching flight cancellation data: {response.status_code} - {response.text}"

# Main function to run both features
def main():
    # Air quality API key for WAQI
    air_quality_api_key = 'your_waqi_api_key'
    
    # Flight cancellations API key for AviationStack
    flight_cancellations_api_key = 'your_aviationstack_api_key'
    
    # Enter coordinates for air quality data
    lat = input("Enter latitude for air quality data (e.g., 32.7767 for Dallas): ")
    lon = input("Enter longitude for air quality data (e.g., -96.7970 for Dallas): ")
    
    # Get and display air quality data
    air_quality_data = get_air_quality_waqi_by_coordinates(air_quality_api_key, lat, lon)
    print("Air Quality Data:")
    print(air_quality_data)
    
    # Get and display flight cancellation data
    flight_cancellations_data = get_flight_cancellations(flight_cancellations_api_key)
    print("Flight Cancellations Data:")
    print(flight_cancellations_data)

if __name__ == "__main__":
    main()
