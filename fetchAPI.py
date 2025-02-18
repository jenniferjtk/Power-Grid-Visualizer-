import requests  # Allows Python to make API calls to retrieve data from web services
import json  # Enables working with JSON data (reading, writing, parsing)
import pandas as pd  # Enables data analysis and manipulation in tabular form

# ---------------------------
# Function to Fetch Data from Electricity Maps API
# This function is used to retrieve data for either carbon intensity or power consumption breakdown.
# It constructs the appropriate API URL and returns the JSON response.
# ---------------------------
def fetch_data(data_type):
    """
    Fetch data from Electricity Maps API based on the requested type.
    :param data_type: 'carbon-intensity' or 'power-consumption-breakdown'
    :return: JSON response data
    """
    
    # Define API key for authentication (required to access API data)
    API_KEY = "jRRULplDqqvZDxzv300Y"  # Replace with your actual API key
    
    # Define the geographic zone for which we are retrieving data (Tennessee Valley Authority region)
    ZONE = "US-TEN-TVA"
    
    # Construct the API request URL with the specified data type
    API_URL = f"https://api.electricitymap.org/v3/{data_type}/latest?zone={ZONE}"
    
    # Define the headers for authentication (API key is passed as a token)
    headers = {"auth-token": API_KEY}
    
    # Make a request to the API and retrieve the response
    response = requests.get(API_URL, headers=headers)
    
    # Convert the response data from JSON format to a Python dictionary and return it
    return response.json()

# ---------------------------
# Fetch Carbon Intensity Data
# Retrieves and structures the latest carbon intensity data for the specified region.
# ---------------------------
carbon_data = fetch_data("carbon-intensity")
carbon_entry = {
    "zone": "US-TEN-TVA",  # The electricity region being analyzed
    "carbon_intensity": carbon_data["carbonIntensity"],  # The current carbon intensity value in gCO2eq/kWh
    "updated_at": carbon_data["updatedAt"]  # The timestamp for when the data was last updated
}

# ---------------------------
# Fetch Power Consumption Breakdown Data
# Retrieves and structures the latest power source breakdown for the specified region.
# ---------------------------
power_data = fetch_data("power-consumption-breakdown")
power_entry = {
    "zone": "US-TEN-TVA",  # The electricity region being analyzed
    "nuclear": power_data["powerConsumptionBreakdown"].get("nuclear", 0),
    "geothermal": power_data["powerConsumptionBreakdown"].get("geothermal", 0),
    "biomass": power_data["powerConsumptionBreakdown"].get("biomass", 0),
    "coal": power_data["powerConsumptionBreakdown"].get("coal", 0),
    "wind": power_data["powerConsumptionBreakdown"].get("wind", 0),
    "solar": power_data["powerConsumptionBreakdown"].get("solar", 0),
    "hydro": power_data["powerConsumptionBreakdown"].get("hydro", 0),
    "gas": power_data["powerConsumptionBreakdown"].get("gas", 0),
    "oil": power_data["powerConsumptionBreakdown"].get("oil", 0),
    "unknown": power_data["powerConsumptionBreakdown"].get("unknown", 0),
    "hydro_discharge": power_data["powerConsumptionBreakdown"].get("hydro discharge", 0),
    "battery_discharge": power_data["powerConsumptionBreakdown"].get("battery discharge", 0),
    "updated_at": power_data["updatedAt"]  # The timestamp for when the data was last updated
}

# ---------------------------
# Save Data to JSON Files
# This allows for easy reference and debugging by storing data locally.
# ---------------------------
with open("carbon_intensity.json", "w") as file:
    json.dump(carbon_entry, file, indent=4)  # Writes carbon intensity data to a JSON file in a readable format

with open("power_consumption_breakdown.json", "w") as file:
    json.dump(power_entry, file, indent=4)  # Writes power breakdown data to a JSON file in a readable format

# ---------------------------
# Save Data to CSV Files
# ---------------------------

# Convert Carbon Intensity Data to Pandas DataFrame and save to CSV
carbon_df = pd.DataFrame([carbon_entry])
carbon_df.to_csv("carbon_intensity.csv", index=False)  # Save as CSV file

# Convert Power Consumption Breakdown Data to Pandas DataFrame and save to CSV
power_df = pd.DataFrame([power_entry])
power_df.to_csv("power_consumption_breakdown.csv", index=False)  # Save as CSV file

print("Carbon Intensity and Power Consumption Breakdown data successfully stored in CSV files.")
