import requests  # Allows Python to make API calls to retrieve data from web services
import json  # Enables working with JSON data (reading, writing, parsing)
import pandas as pd  # Enables data analysis and manipulation in tabular form
import sqlite3  # SQLite for optional live data export functionality  

# ----------------------------
# Connect to SQLite Database
# ----------------------------
conn = sqlite3.connect("electricity_data.db")  # Connect to SQLite
cursor = conn.cursor()  # Create a cursor object for executing SQL queries

# ----------------------------
# Create Tables IF NOT already Exist
# ----------------------------
cursor.execute("""
  CREATE TABLE IF NOT EXISTS CarbonIntensity (
    zone TEXT,
    carbon_intensity INTEGER,
    updated_at TEXT
  )
""")

cursor.execute("""
  CREATE TABLE IF NOT EXISTS PowerConsumptionBreakdown (
    zone TEXT,
    nuclear INTEGER,
    geothermal INTEGER,
    biomass INTEGER,
    coal INTEGER,
    wind INTEGER,
    solar INTEGER,
    hydro INTEGER,
    gas INTEGER,
    oil INTEGER,
    unknown INTEGER,
    hydro_discharge INTEGER,
    battery_discharge INTEGER,
    updated_at TEXT
  )
""")
conn.commit()  # Save the table creation

# ---------------------------
# Function to Fetch Data from Electricity Maps API
# ---------------------------
def fetch_data(data_type):
    API_KEY = "jRRULplDqqvZDxzv300Y"  # Replace with your actual API key
    ZONE = "US-TEN-TVA"  # Define geographic ZONE where data is pulled from 
    API_URL = f"https://api.electricitymap.org/v3/{data_type}/latest?zone={ZONE}"  # Format API URL request
    headers = {"auth-token": API_KEY}  # Define the headers for authentication (API key is passed as a token)
    response = requests.get(API_URL, headers=headers)  # Make a request to the API and retrieve the response
    print(json.dumps(response.json(), indent=4))  # Print API response for debugging
    return response.json()  # Convert response data to Python dictionary

# ---------------------------
# Fetch Carbon Intensity Data
# ---------------------------
carbon_data = fetch_data("carbon-intensity") #raw JSON response form API (not formatted)
carbon_entry = { # create a dictionary containing only the relevant fields wanted
    "zone": "US-TEN-TVA",
    "carbon_intensity": carbon_data["carbonIntensity"],
    "updated_at": carbon_data["updatedAt"]
}

# Create A ZONE dictionary to remove mismatched data from JSON API response
zone_dict = {
     "US-TN-TVA" : "US-TEN-TVA"
    }

# Checks IF value is found in zone_dict, IF yes replace with mapped value, ELSE
# leave value unchanged (default) 
carbon_entry["zone"] = zone_dict.get(carbon_entry["zone"], carbon_entry["zone"])

# Insert Carbon Intensity into SQLite**
cursor.execute("""
    INSERT INTO CarbonIntensity (zone, carbon_intensity, updated_at)
    VALUES (?, ?, ?)
""", (carbon_entry["zone"], carbon_entry["carbon_intensity"],carbon_entry["updated_at"]))

# ---------------------------
# Fetch Power Consumption Breakdown Data
# ---------------------------
power_data = fetch_data("power-consumption-breakdown")


# Extract power breakdown values safely
# Use .get() to extract the specific key from PowerConsumptionBreakdown
# Logic: IF key "nuclear" is found in the dictionary, the value pair will be returned
# IF key is NOT found, just return 0
# Prevents crashing if value not found 
power_entry = {
    "zone": "US-TEN-TVA",
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
    "updated_at": power_data["updatedAt"]
}

# Same check for power_entry zone 
power_entry ["zone"] = zone_dict.get(power_entry["zone"], power_entry["zone"])

# Insert Power Consumption into SQLite
cursor.execute("""
    INSERT INTO PowerConsumptionBreakdown 
    (zone, nuclear, geothermal, biomass, coal, wind, solar, hydro, gas, oil, unknown, hydro_discharge, battery_discharge, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    power_entry["zone"], power_entry["nuclear"], power_entry["geothermal"], power_entry["biomass"],
    power_entry["coal"], power_entry["wind"], power_entry["solar"], power_entry["hydro"],
    power_entry["gas"], power_entry["oil"], power_entry["unknown"], power_entry["hydro_discharge"],
    power_entry["battery_discharge"], power_entry["updated_at"]
))

# ---------------------------
# Save Data to CSV Files
# ---------------------------
pd.DataFrame([carbon_data]).to_csv("carbon_intensity.csv", index=False)
pd.DataFrame([power_entry]).to_csv("power_consumption_breakdown.csv", index=False)

# Commit and Close Database Connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully stored in SQLite & CSV files!")
