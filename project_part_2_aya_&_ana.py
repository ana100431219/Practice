import sqlite3
import pandas as pd 
from sqlite3.dbapi2 import DatabaseError
from PIL import Image
con= sqlite3.connect('excel_database.db')

df_participants=pd.read_excel(r'C:/Users/User/Desktop/PROGRA/participants.xlsx')
df_countries=pd.read_excel(r'C:/Users/User/Desktop/PROGRA/countries.xlsx')
df_projects=pd.read_excel(r'C:/Users/User/Desktop/PROGRA/projects.xlsx')

df_projects.to_sql('projects', con, if_exists='replace', index= False)
df_countries.to_sql('countries', con, if_exists='replace', index= False)
df_participants.to_sql('participants', con, if_exists='replace', index= False)

con.close()
df_projects.head()

#colnames={c:c for c in list(df)}
database = excel_database.db
selects= {
'country':
'''SELECT Acronym FROM countries WHERE Country = "{}" ''',

'grants':
'''SELECT SUM (o.ecContribution) AS grants
  FROM organizations o JOIN projects p ON o.projectID==p.projectID
  WHERE o.country = '{}'
  GROUP BY p.year''',

'participants':
'''SELECT shortName, name, activityType, organizationURL, COUNT(ecContribution) n_projects, SUM(ecContribution)   #maybe this is incomplete
  FROM organizations
  WHERE country = '{}'
  GROUP BY name ORDER BY SUM(ecContribution) DESC''',

'coordinators':
'''SELECT o.shortName, o.name, p.acronym, p.keywords
  FROM organizations o JOIN projects p ON o.projectID = p.projectID
  WHERE o.country='{}' AND o.role = 'coordinator' '''
}

#Title
image=Image.open('KDT-JU.png')
st.image(image)
st.title('Partner search tool')

#Select country
conn=sqlite3.connect(database)
c t= st.selectbox('Select country', ['Spain', 'France', 'Germany'])
country=pd.read_sql(selects['country'].format(ct), conn)
country=country.Acronym.item()
st.write(f'You selected: {country}-{ct}')

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
