import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import toml
import psycopg2
import streamlit_shadcn_ui as ui


st.set_page_config(
   page_title="Flight & airport tracker",
   page_icon="🛫"
)


st.title("🛫 Flight Tracker")


image_path = 'images/aviation-night.jpg'
st.image(image_path, use_column_width=True)



########### Connection to the db #############

def db_connection():
    secrets = toml.load('.streamlit/secrets.toml')


    conn = psycopg2.connect(
        database="pagila",
        user= secrets['sql_user'],
        password= secrets['sql_password'],
        host= secrets['host'],
        port=secrets['port']
    )
    return conn


########### fetching data #################

def fetch_data(query):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data




################# metrics on the top #######################

query_nb_flight = 'SELECT COUNT(id) AS total_num_flight FROM student.iz_aviationstack'
data_nb_flight = fetch_data(query_nb_flight)
df_nb_flight = pd.DataFrame(data_nb_flight, columns=['total_num_flight'])


query_nb_airport = 'SELECT COUNT(DISTINCT departure_airports) AS unique_airport FROM student.iz_aviationstack'
data_nb_airport = fetch_data(query_nb_airport)
df_nb_airport = pd.DataFrame(data_nb_airport, columns=['unique_airport'])


query_nb_airline = 'SELECT COUNT(DISTINCT airline_names) AS unique_airline FROM student.iz_aviationstack'
data_nb_airline = fetch_data(query_nb_airline)
df_nb_airline = pd.DataFrame(data_nb_airline, columns=['unique_airline'])


query_nb_days = 'SELECT COUNT(DISTINCT flight_dates) AS unique_dates FROM student.iz_aviationstack'
data_nb_days = fetch_data(query_nb_days)
df_nb_days = pd.DataFrame(data_nb_days, columns=['unique_airline'])


cols = st.columns(4)
with cols[0]:
    ui.metric_card(title="Total Days", content=data_nb_days[0][0], key="card1")
with cols[1]:
    ui.metric_card(title="Total Flights", content=data_nb_flight[0][0], key="card2")
with cols[2]:
    ui.metric_card(title="Total Airport", content=data_nb_airport[0][0], key="card3")
with cols[3]:
    ui.metric_card(title="Total Airline", content=data_nb_airline[0][0], key="card4")


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


################ All data for report ###################

query_all = 'SELECT flight_dates, flight_statuses, flight_number, airline_names, departure_airports, arrival_airports FROM student.iz_aviationstack'
data_all = fetch_data(query_all)
df_all = pd.DataFrame(data_all, columns=['flight_dates', 'flight_statuses','flight_number', 'airline_names','departure_airports', 'arrival_airports'])


################ Sidebar filter ###################
st.sidebar.subheader("Filter of the Data Report")

# Date range selection
start_date = st.sidebar.date_input("Select start date", value=pd.to_datetime('today') - pd.DateOffset(days=3))
end_date = st.sidebar.date_input("Select end date", value=pd.to_datetime('today'))

# Airport selection
unique_airports = ['All Airport']+list(df_all['departure_airports'].unique())
selected_airport = st.sidebar.selectbox("Select Airport", unique_airports)

# Airline selection
unique_airlines = ['All Airlines'] + list(df_all['airline_names'].unique())
selected_airline = st.sidebar.selectbox("Select Airline", unique_airlines)

# Filter data based on selections
filtered_data = df_all[
    (df_all['flight_dates'] >= start_date) &
    (df_all['flight_dates'] <= end_date) &
    ((selected_airport == 'All Airport') | (df_all['departure_airports'] == selected_airport)) &
    ((selected_airline == 'All Airlines') | (df_all['airline_names'] == selected_airline))
]

# Display
st.header('Data report')
st.write('This report includes all flights data from July 2nd, 2024. You can filter the data using the options available in the sidebar.')
st.write(filtered_data)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
################ Graphs ####################

###### Departure Airports ######

st.header('Top 3 Departure Airports')

query_top_departure = 'SELECT departure_airports, COUNT(*) AS num_departures FROM student.iz_aviationstack GROUP BY departure_airports ORDER BY num_departures DESC LIMIT 3'
data_top_departure = fetch_data(query_top_departure)
# Convert fetched data to Pandas DataFrame
df = pd.DataFrame(data_top_departure, columns=['Airport', 'Num_Departures'])


# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airport', y='Num_Departures', data=df, hue='Airport', palette='viridis', legend=False)
plt.xlabel('Airport')
plt.ylabel('Number of Departures')

# Display plot 
st.pyplot(plt)

if st.button(f"Departure Details"):
    st.write(df)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


###### Arrival Airports ######

st.header('Top 3 Arrival Airports')


query_top_arrival = 'SELECT arrival_airports, COUNT(*) AS num_arrival FROM student.iz_aviationstack GROUP BY arrival_airports ORDER BY num_arrival DESC LIMIT 3'
data_top_arrival = fetch_data(query_top_arrival)
df_top_arrival = pd.DataFrame(data_top_arrival, columns=['Airport', 'num_arrival'])



# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airport', y='num_arrival', data=df_top_arrival, hue='Airport', palette='viridis', legend=False)
plt.xlabel('Airport')
plt.ylabel('Number of Arrival')
st.markdown("<br>", unsafe_allow_html=True)

# Display plot 
st.pyplot(plt)  

if st.button(f"Arrival Details"):
    st.write(df_top_arrival)


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


###### Airlines ######
st.header('Top 3 Airlines')


query_top_airline = 'SELECT airline_names, COUNT(*) AS num_airline FROM student.iz_aviationstack GROUP BY airline_names ORDER BY num_airline DESC LIMIT 3'
data_top_airline = fetch_data(query_top_airline)
df_top_airline = pd.DataFrame(data_top_airline, columns=['Airline', 'num_airline'])



# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airline', y='num_airline', data=df_top_airline, hue='Airline', palette='viridis', legend=False)
plt.xlabel('Airline')
plt.ylabel('Number of Arrival')

# Display plot
st.pyplot(plt)  

if st.button(f'Airline Details'):
    st.write(df_top_airline)