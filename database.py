import os 
from dotenv import load_dotenv, dotenv_values
import mysql.connector
from mysql.connector import Error
import pandas as pd

load_dotenv()

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "ricebikes",
            passwd = os.getenv("RB_PW"),
            database = "emails"
        )
        print("MySQL Database connection succesful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}")

#create_database_query = "CREATE DATABASE emails"
#create_database(connection, create_database_query)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}")


# create_employee_table = """
# CREATE TABLE employee (
#     employee_id INT AUTO_INCREMENT PRIMARY KEY,
#     first_name VARCHAR(100),
#     last_name VARCHAR(100)
#     );
# """
# execute_query(connection, create_employee_table)

create_avail_table = """
CREATE TABLE availability (
    avail_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    day VARCHAR(9),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id));
"""
connection = create_server_connection()
execute_query(connection, create_avail_table)