import mysql.connector

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                passwd="Soni1dec@",
                database="flights"
            )
            self.mycursor = self.conn.cursor()
            print("Connected to MySQL")
        except:
            print("Error connecting to MySQL")
    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights.flights_cleaned  
        UNION 
        SELECT DISTINCT(Source) FROM flights.flights_cleaned
        """)

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city
        print(data)

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM flights_cleaned 
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()
        return data
    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights_cleaned
        GROUP BY Airline
        """)
        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency
    def busy_airport(self):
        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT Source ,Count(*) FROM ( SELECT SOURCE FROM flights_cleaned
                              UNION ALL
                              SELECT Destination FROM flights_cleaned) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
                              """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) from flights_cleaned
        GROUP BY Date_of_Journey
                              """)
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency