**Presentation**
This Streamlit application provides a Flight Tracker and Data Report for analyzing flight data including metrics, top departure and arrival airports, and top airlines.


**Features**
- Metrics Display: Shows key metrics such as total flights, unique airports, unique airlines, and total days.
- Data Report: Displays a comprehensive report of flight data with filtering options based on date, airport, and airline.
- Charts: Visualizes top 3 departure and arrival airports, and top 3 airlines based on flight counts.


**How to Use**
Setup:
   - Clone the repository to your local machine.
   - Install the required dependencies using pip install -r requirements.txt.
   - Ensure PostgreSQL is installed and configure your database connection details in .streamlit/secrets.toml.
   - Running the Application:

Launch the Streamlit application:
   - Launch the app locally with 'streamlit run streamlit_app.py'.
   - Access the application through your browser at http://localhost:8501.



**Technologies Used**
   - Streamlit: Python framework for building interactive web applications.
   - Matplotlib & Seaborn: Libraries for data visualization.
   - Pandas: Data manipulation and analysis.
   - PostgreSQL: Dbeaver Database management system for storing flight data.
   - API used: https://aviationstack.com/