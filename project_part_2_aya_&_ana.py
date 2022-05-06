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

#Other selects
dfs={}
for key,sel in selects.items():
  dfs[key]=pd.read_sql(sel.format(country), conn)

df_grants_year = pd.read_sql('''SELECT p.year, SUM(o.ecContribution) AS grants
    FROM organizations o JOIN projects p ON o.projectID==p.projectID
    WHERE o.country='{}'
    GROUP BY p.year '''.format(country), conn)

#grants
st.subheader(f'Yearly EC contribution in {ct} (€)')
st.bar_chart(dfs['grants'])

#participants
st.subheader(f'Participants in {ct}')
st.dataframe(dfs['participants'])
csv_p=dfs['participants'].to_csv().encode('utf-8')
st.download_button(
    label=''Download participants data as CSV",
    data=csv_p,
    file_name=f'{country}_participants.csv',
    mime='text/csv',
)

#coordinators
st.subheader(f'Project coordinators in {ct}')
st.dataframe(dfs['coordinators'])
csv_c=dfs['coordinators'].to_csv().encode('utf-8')
