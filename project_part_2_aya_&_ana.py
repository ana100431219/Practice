import sqlite3
import pandas as pd 
from sqlite3.dbapi2 import DatabaseError

con= sqlite3.connect('ecsel_database.db')
df_projects.to_sql('projects', con, if_exists='replace', index= False)
df_countries.to_sql('countries', con, if_exists='replace', index= False)
df_participants.to_sql('participants', con, if_exists='replace', index= False)

con.close()
df_projects.head()
