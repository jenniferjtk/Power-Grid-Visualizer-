import sqlite3
import pandas as pd

# ---------------------------
# Connect to the SQLite Database
# ---------------------------
conn = sqlite3.connect("electricity_data.db")  # Connect to SQLite
cursor = conn.cursor()

# ---------------------------
# Read Power Consumption Breakdown Data
# ---------------------------
df = pd.read_sql("SELECT * FROM PowerConsumptionBreakdown", conn)  # Query database and store results

# Print Data
print("\n Power Consumption Breakdown Data:")
print(df)

# ---------------------------
# Read Carbon Intensity Data
# ---------------------------
df_carbon = pd.read_sql("SELECT * FROM CarbonIntensity", conn)  # Query Carbon Intensity Data
print("\n Carbon Intensity Data:")
print(df_carbon)

# Close Connection
conn.close()
