This Streamlit application provides a Flight Tracker and Data Report for analyzing flight data including metrics, top departure and arrival airports, and top airlines.

Features
Metrics Display: Shows key metrics such as total flights, unique airports, unique airlines, and total days based on the data from a PostgreSQL database.
Data Report: Displays a comprehensive report of flight data with filtering options based on date, airport, and airline.
Top Airports and Airlines: Visualizes top 3 departure and arrival airports, and top 3 airlines based on flight counts.
Interactive Graphs: Uses seaborn for plotting bar charts that dynamically update based on user interactions.
How to Use
Setup:

Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Ensure PostgreSQL is installed and configure your database connection details in .streamlit/secrets.toml.
Running the Application:

Launch the Streamlit application locally with streamlit run app.py.
Access the application through your browser at http://localhost:8501.
Using the Application:

Use the sidebar filters to select a date range, airport, and airline for filtering the flight data report.
Explore the top departure airports, arrival airports, and airlines using interactive graphs.
Technologies Used
Streamlit: Python framework for building interactive web applications.
Matplotlib & Seaborn: Libraries for data visualization.
Pandas: Data manipulation and analysis.
PostgreSQL: Database management system for storing flight data.