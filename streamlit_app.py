import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import requests
import toml
import psycopg2



###########
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

###########

def fetch_data(query):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

st.title("🛫 Real-time Flight trStatus")


##query = 'SELECT * FROM student.iz_aviationstack'
##data = fetch_data(query)

query2 = 'SELECT departure_airports, COUNT(*) AS num_departures FROM student.iz_aviationstack GROUP BY iz_aviationstack.departure_airports ORDER BY num_departures DESC'
data = fetch_data(query2)


#display
st.write('this is the pagila data')
st.write(data)

#def main():
   ## st.title('PostgreSQL Database Connection Example')
    
    # Example query
   ## query = 'SELECT * FROM student.iz_aviationstack WHERE airline_names=\'Qantas'\'
   ## data = fetch_data(query)
    
    # Display data
    

##if __name__ == '__main__':
##    main()




st.balloons()