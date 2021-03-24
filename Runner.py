import mysql.connector
import pandas as pd

def get_db_connection(user, host, database, password):
    connection = None
    try:
        connection = mysql.connector.connect(user = user,
                        host = host,
                        database = database,
                        password = password)
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection

def load_third_party (connection , file_path_csv):
  cursor = connection.cursor()
  ticketdata = pd.read_csv(file_path_csv)
# [Iterate through the CSV file and execute insert statement]
  for i,row in ticketdata.iterrows():
    sql = "INSERT INTO Sales_Loading VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    connection.commit()
  return  

def query_popular_tickets (connection):
# Get the most popular ticket in the past month
    sql_statement = "SELECT event_name FROM Sales_Loading WHERE month(trans_date) = \
      (SELECT month(MAX(trans_date)) FROM Sales_Loading) and year(trans_date) = (SELECT year(MAX(trans_date)) FROM Sales_Loading) \
        GROUP BY year(trans_date), month(trans_date),event_id, event_name \
        ORDER BY COUNT(*) DESC LIMIT 5"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

if __name__ == '__main__':
    print("Enter db details :")
    host = input("Enter hostname :")
    database = input("Enter databasename :")
    user = input("Enter username :")   
    password = input("Enter password :")
    file_path = input("Enter the path of the csv file: Sample format - C:\\Users\\vra\\Ticketing\\third_party_sales_1.csv :")
    #file_path = "C:\\Users\\vra\\Desktop\\Personal\\SpringBoard\\gitLocal\\Ticketing\\third_party_sales_1.csv"
    load_third_party (get_db_connection(user, host, database, password) , file_path)
    records = query_popular_tickets(get_db_connection(user, host, database, password))
    if (records):
        print("\nHere are the most popular tickets in the past month:")
        for event_name in records:
            print("-",event_name[0])
  

    


