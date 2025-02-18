import sqlite3  # Import SQLite to connect to the database
import pandas as pd  # Import Pandas to organize data in tables

# ---------------------------
# Connect to the SQLite Database
# ---------------------------
conn = sqlite3.connect("electricity_data.db")  # Connect to the database file

# ---------------------------
# Read Power Consumption Breakdown Data from Database
# ---------------------------
df = pd.read_sql("SELECT * FROM PowerConsumptionBreakdown", conn)  # Run SQL query and store results in Pandas DataFrame

# Print the data in a readable format
print("\nPower Consumption Breakdown Data:")
print(df)

# Close the database connection
conn.close()
