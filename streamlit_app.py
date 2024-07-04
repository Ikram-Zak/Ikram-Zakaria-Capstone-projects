import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
import toml
import psycopg2
import streamlit_shadcn_ui as ui


st.title("🛫 Real-time Flight")


########### Connection to the db
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

########### fetching data

def fetch_data(query):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data





query_nb_flight = 'SELECT COUNT(id) AS total_num_flight FROM student.iz_aviationstack'
data_nb_flight = fetch_data(query_nb_flight)
df_nb_flight = pd.DataFrame(data_nb_flight, columns=['total_num_flight'])

query_nb_airport = 'SELECT COUNT(DISTINCT departure_airports) AS unique_airport FROM student.iz_aviationstack'
data_nb_airport = fetch_data(query_nb_airport)
df_nb_airport = pd.DataFrame(data_nb_airport, columns=['unique_airport'])

query_nb_airline = 'SELECT COUNT(DISTINCT airline_names) AS unique_airline FROM student.iz_aviationstack'
data_nb_airline = fetch_data(query_nb_airline)
df_nb_airline = pd.DataFrame(data_nb_airline, columns=['unique_airline'])

cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Total Flights", content=data_nb_flight[0][0], key="card1")
with cols[1]:
    ui.metric_card(title="Total Airport", content=data_nb_airport[0][0], key="card2")
with cols[2]:
    ui.metric_card(title="Total Airline", content=data_nb_airline[0][0], key="card3")











### querying data ###
##query = 'SELECT * FROM student.iz_aviationstack'
##data = fetch_data(query)

##query2 = 'SELECT departure_airports, COUNT(*) AS num_departures FROM student.iz_aviationstack GROUP BY iz_aviationstack.departure_airports ORDER BY num_departures DESC'
##data = fetch_data(query2)

##################################

query_top_departure = 'SELECT departure_airports, COUNT(*) AS num_departures FROM student.iz_aviationstack GROUP BY departure_airports ORDER BY num_departures DESC LIMIT 3'
data_top_departure = fetch_data(query_top_departure)


# Convert fetched data to Pandas DataFrame
df = pd.DataFrame(data_top_departure, columns=['Airport', 'Num_Departures'])


# Display data as a table
#st.write("Top 5 Departure Airports:")
st.write(df)


# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airport', y='Num_Departures', data=df, hue='Airport', palette='viridis', legend=False)
plt.xlabel('Airport')
plt.ylabel('Number of Departures')
plt.title('Top 5 Departure Airports by Number of Departures')
st.pyplot(plt)  # Display plot in Streamlit


##################################

query_top_arrival = 'SELECT arrival_airports, COUNT(*) AS num_arrival FROM student.iz_aviationstack GROUP BY arrival_airports ORDER BY num_arrival DESC LIMIT 3'
data_top_arrival = fetch_data(query_top_arrival)


# Convert fetched data to Pandas DataFrame
df_top_arrival = pd.DataFrame(data_top_arrival, columns=['Airport', 'num_arrival'])

st.write(df_top_arrival)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airport', y='num_arrival', data=df_top_arrival, hue='Airport', palette='viridis', legend=False)
plt.xlabel('Airport')
plt.ylabel('Number of Arrival')
plt.title('Top 5 Arrival Airports by Number of Arrival')
st.pyplot(plt)  # Display plot in Streamlit

##################################

query_top_airline = 'SELECT airline_names, COUNT(*) AS num_airline FROM student.iz_aviationstack GROUP BY airline_names ORDER BY num_airline DESC LIMIT 3'
data_top_airline = fetch_data(query_top_airline)


# Convert fetched data to Pandas DataFrame
df_top_airline = pd.DataFrame(data_top_airline, columns=['Airline', 'num_airline'])

st.write(df_top_airline)

# Plotting using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Airline', y='num_airline', data=df_top_airline, hue='Airline', palette='viridis', legend=False)
plt.xlabel('Airline')
plt.ylabel('Number of Arrival')
plt.title('Top 5 Airline by Number of flight')
st.pyplot(plt)  # Display plot in Streamlit





st.balloons()