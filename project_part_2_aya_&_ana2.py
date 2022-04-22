import sqlite3
from sqlite3.dbapi2 import DatabaseError

import pandas as pd
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

#df_participants=pd.read_excel('/content/drive/MyDrive/participants.xlsx')
#df_countries=pd.read_excel('/content/drive/MyDrive/countries.xlsx')
#df_projects=pd.read_excel('/content/drive/MyDrive/projects.xlsx')

con= sqlite3.connect('exel_database.db')
df_projects.to_sql('projects',con, if_exists='replace', index= False)
df_countries.to_sql('countries',con, if_exists='replace', index= False)
df_participants.to_sql('participants',con, if_exists='replace', index= False)

con.close()
df_projects.head()


