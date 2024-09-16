import os

from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import pytds
import pyodbc
import sqlalchemy


# # initialize Connector object
# connector = Connector()

# # function to return the database connection object
# def getconn():
#     conn = connector.connect(
#         "sacred-alliance-433217-e3:us-central1:tf-mssql-public-efe4c33f",
#         "pyodbc",
#         user="sqlserver",
#         password="test123",
#         db="msdb",
#         sql_driver= '{ODBC Driver 17 for SQL Server}'
#     )
#     return conn

# # create connection pool with 'creator' argument to our connection object function
# pool = sqlalchemy.create_engine(
#     "mssql+pyodbc://",
#     creator=getconn,
# )

from sqlalchemy.engine import URL
sql_server = '34.173.135.6'
sql_database = 'msdb'
sql_username = 'sqlserver'
sql_password = 'test123'   
sql_driver= '{ODBC Driver 17 for SQL Server}'
connection_string = f"DRIVER={sql_driver};SERVER={sql_server};DATABASE={sql_database};UID={sql_username};PWD={sql_password}"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
pool = sqlalchemy.create_engine(connection_url)



