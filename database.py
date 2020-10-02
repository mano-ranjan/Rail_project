import sqlite3

connection = sqlite3.connect("Rail_database.db")

crsr = connection.cursor()

sql_query = """CREATE TABLE user (
user_name VARCHAR(20) PRIMARY KEY,  
password VARCHAR(30));"""

crsr.execute(sql_query)

sql_query = """CREATE TABLE tickets (
user_name VARCHAR(20),
ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
age INT(3),
gender VARCHAR(1),
aadhar_no INT(12),
phone_no INT(10),
travel_date DATE,
train_no INT(6),
source_stn VARCHAR(4),
destination_stn VARCHAR(4),
activity VARCHAR(10),
status VARCHAR(3));"""

crsr.execute(sql_query)

sql_query = """CREATE TABLE cancel_tickets (
user_name VARCHAR(20),
ticket_id INTEGER PRIMARY KEY,
name VARCHAR(50),
age INT(3),
gender VARCHAR(1),
aadhar_no INT(12),
phone_no INT(10),
travel_date DATE,
train_no INT(6),
source_stn VARCHAR(4),
destination_stn VARCHAR(4),
activity VARCHAR(10),
status VARCHAR(3));"""

crsr.execute(sql_query)

sql_query = """INSERT INTO user VALUES ("mano", "935");"""
sql_command = """INSERT INTO user VALUES ("xyz", "456");"""

crsr.execute(sql_query)
crsr.execute(sql_command)

sql_query = """CREATE TABLE data (
A_S INT(3), 
W_L INT(3));"""

crsr.execute(sql_query)

sql_query = """INSERT INTO data VALUES (2, 1);"""

crsr.execute(sql_query)

connection.commit() 

connection.close()


#side="left", expand = True