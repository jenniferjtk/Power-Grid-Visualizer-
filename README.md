 Power Grid Visualizer

 Overview
This project fetches realtime electricity grid data from the Electricity Maps API, processes it, and stores it in CSV format for easy visualization using tools like Power BI, Excel, or other data visualization software.

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

This will create carbon_intensity.csv and power_consumption_breakdown.csv in your project folder.

 4. Load CSV Data into a Visualization Tool
 Open a tool such as Power BI, Excel, or another data visualization software.
 Import carbon_intensity.csv and power_consumption_breakdown.csv.
 Use available charting options to create meaningful visual representations of the data.



 Suggested Visualizations
 Line Chart → Plot Carbon Intensity Over Time using `updated_at` as Xaxis and `carbon_intensity` as Yaxis.
 Bar Chart → Show Power Consumption Breakdown with energy sources (`nuclear`, `coal`, `solar`, etc.) as Xaxis and their values as Yaxis.

 Note: You can view the example visual in the root directory as a png entitled PowerGridVisual.png!

Data ODbl 
Electricity Maps (2025). {COUNTRY NAME} {YEAR} {INTERVAL} Carbon Intensity Data (Version January 27, 2025). Electricity Maps. https://www.electricitymaps.com

