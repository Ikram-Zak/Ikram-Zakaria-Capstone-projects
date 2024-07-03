import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
import toml
import psycopg2



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

st.title("🛫 Real-time Flight trStatus")



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
sns.barplot(x='Airport', y='Num_Departures', data=df, palette='viridis')
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
sns.barplot(x='Airport', y='num_arrival', data=df_top_arrival, palette='viridis')
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
sns.barplot(x='Airline', y='num_airline', data=df_top_airline, palette='viridis')
plt.xlabel('Airline')
plt.ylabel('Number of Arrival')
plt.title('Top 5 Airline by Number of flight')
st.pyplot(plt)  # Display plot in Streamlit


st.balloons()