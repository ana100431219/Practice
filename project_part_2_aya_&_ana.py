
import sqlite3

import pandas as pd

con= sqlite3.connect('exel_database.db')
df_projects.to_sql('projects',con, if_exists='replace', index= False)
df_countries.to_sql('countries',con, if_exists='replace', index= False)
df_participants.to_sql('participants',con, if_exists='replace', index= False)

con.close()
df_projects.head()

database = exel_database.db
selects= {
'country':
'''SELECT Acronym FROM countries WHERE Country = "{}" ''',

'grants':
'''SELECT SUM (O.ecContribution) AS grants
  FROM organizations o JOIN projects p ON o.projectID==p.projectID
  WHERE o.country = '{}'
  GROUP BY p.year''',

'participants':
'''SELECT shortName, o.name, p.acronym, p.keywords
  FROM organizations
  WHERE country = '{}'
  GROUP BY name ORDER BY SUM(ecContribution) DESC''',

'coordinators':
'''SELECT o.shortName
