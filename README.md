 Power Grid Visualizer

 Overview
This project fetches real-time electricity grid data from the Electricity Maps API, processes it, and stores it in CSV format, Pandas DataFrames, and an SQLite database for further analysis. The data can be visualized using tools like Power BI, Excel, or other data visualization software.

 Features:
 Fetches Carbon Intensity Data (gCO2/kWh)
 Fetches Power Consumption Breakdown (Nuclear, Coal, Wind, Solar, etc.)
 Saves data to CSV files for external analysis
 Can be expanded to support other regions



 File Structure:
 ElectricityGrid/
|-- fetchAPI.py   Script to fetch electricity grid data & save as CSV
|-- power_consumption_breakdown.csv   Latest power breakdown data
|-- carbon_intensity.csv   Latest carbon intensity data
|-- queryDB.py   Script to read and display CSV data
|-- .gitignore   Excludes unnecessary files like venv/
|-- README.md   Project documentation




 Setup Instructions
 1. Clone the Repository
bash
git clone https://github.com/jenniferjtk/PowerGridVisualizer.git
cd PowerGridVisualizer


 2. Install Dependencies
bash
pip install requests pandas


 3. Run the Script to Fetch Data
bash
python3 fetchAPI.py

This will:
    Fetch real-time electricity data from the API
    Store it in Pandas DataFrames for manipulation
    Save it to CSV files (carbon_intensity.csv, power_consumption_breakdown.csv)
    Store data in an SQLite database (electricity_data.db)

 4. View Data Stored in SQLite
 python3 queryDB.py  

This will:
    display Power Consumption Breakdown and Carbon Intensity data stored in the SQLite database.
 
5. Load Data into Power BI, Excel, or SQL-based tools
 Using CSV Data:
    Open a tool such as Power BI, Excel, or another data visualization software.
    Import carbon_intensity.csv and power_consumption_breakdown.csv.
    Use available charting options to create meaningful visual representations of the data.

 Using SQLite for Live Data:
    Open Power BI (Desktop version required).
    Click Home > Get Data > More...
    Search for ODBC and select it.
    Choose SQLite ODBC Driver.
    Select electricity_data.db as the database.
    Click Load to import the tables.

Now, your SQLite live data is available in Power BI for visualization! 

 (Optional): Suggested Visualizations
 Line Chart → Plot Carbon Intensity Over Time using `updated_at` as Xaxis and `carbon_intensity` as Y axis.
 Bar Chart → Show Power Consumption Breakdown with energy sources (`nuclear`, `coal`, `solar`, etc.) as X axis and their values as Y axis.

 Note: You can view an example visual in the root directory as a png entitled PowerGridVisual.png!

Data ODbl 
Electricity Maps (2025). {COUNTRY NAME} {YEAR} {INTERVAL} Carbon Intensity Data (Version January 27, 2025). Electricity Maps. https://www.electricitymaps.com

