# -*- coding: utf-8 -*-
"""Final

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14VqC4DKTte6YLYpAr94IXcMPuHNG1jMp
"""

import sqlite3 
import pandas as pd
import streamlit as st
from sqlite3 import connect
from sqlite3.dbapi2 import DatabaseError
from PIL import Image

#colnames={c:c for c in list(df)}
database = 'CreateDB.db'

#Title
image=Image.open('descarga.png')
st.image(image)
st.title('Partner search tool')

#Select country
conn=sqlite3.connect(database)
ct= st.selectbox('Select country', ['Spain', 'France', 'Germany'])
country=pd.read_sql(SELECT Country.format(ct) FROM countries, conn)
country=country.Acronym.item()
st.write(f'You selected: {country}-{ct}')

#Other selects
dfs={}
for key,sel in selects.items():
  dfs[key]=pd.read_sql(sel.format(country), conn)

df_grants_year = pd.read_sql('''SELECT p.year, SUM(o.ecContribution) AS grants
    FROM participants o JOIN projects p ON o.projectID==p.projectID
    WHERE o.country='{}'
    GROUP BY p.year '''.format(country), conn)
conn.close()

#grants
st.subheader(f'Yearly EC contribution in {ct} (€)')
st.bar_chart(dfs['grants'])

#participants
st.subheader(f'Participants in {ct}')
st.dataframe(dfs['participants'])
csv_p=dfs['participants'].to_csv().encode('utf-8')
st.download_button(
    label= 'Download participants data as CSV',
    data=csv_p,
    file_name=f'{country}_participants.csv',
    mime='text/csv',
)

#coordinators
st.subheader(f'Project coordinators in {ct}')
st.dataframe(dfs['coordinators'])
csv_c=dfs['coordinators'].to_csv().encode('utf-8')
