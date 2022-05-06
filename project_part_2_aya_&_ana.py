import sqlite3 
import pandas as pd 
from sqlite3.dbapi2 import DatabaseError
from PIL import Image


#Select country
con=sqlite3.connect(database)
ct= st.selectbox('Select country', ['Spain', 'France', 'Germany'])
country=pd.read_sql(selects['country'].format(ct), conn)
country=country.Acronym.item()
st.write(f'You selected: {country}-{ct}')

#Title
image=Image.open('KDT-JU.png')
st.image(image)
st.title('Partner search tool')
