# -*- coding: utf-8 -*-
"""Group_6_mvp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12tX5o9M1Zu6hvtS-nPMCotD6n8X0ErX5
"""

import pandas as pd 
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

df_participants=pd.read_excel('/content/drive/MyDrive/participants.xlsx')
df_countries=pd.read_excel('/content/drive/MyDrive/countries.xlsx')
df_projects=pd.read_excel('/content/drive/MyDrive/projects.xlsx')

acronyms=list(df_countries.Acronym) 
countries=list(df_countries.Country)
answer= input("please input name or acronym of country ")
while answer.upper() not in acronyms and answer.title() not in countries : 
    answer= input("please input name or acronym of country ")
if answer.upper() in acronyms :
  answer_acronym = answer.upper()
  answer_name = df_countries[df_countries.Acronym==answer_acronym]
elif answer.title() in countries:
  answer_name = answer.title()
  answer_acronym = df_countries[df_countries.Country== answer_name].Acronym.item()

print('Selected:{}-{}'.format(answer_acronym,answer_name))    


df_selcountry=df_participants[df_participants.country==answer_acronym]
df_projyear=df_projects[["projectID","year"]]
df_selcountry=pd.merge(df_selcountry,df_projyear,how="left",on="projectID")

df_ECcontr_year=df_selcountry[["ecContribution","year"]].groupby(by="year").sum()
df_ECcontr_year=df_selcountry.groupby('year').sum().ecContribution
df_ECcontr_year.plot(kind='bar', title='Total EU contribution in {ct} (M€)')

df_ECcontr_year.describe()

df_best=df_selcountry.groupby(['shortName','name','activityType','organizationURL']).agg({'ecContribution':['count', 'sum']}).sort_values([("ecContribution","sum")],ascending=False)
df_best.to_excel("country_participants.xlsx")
df_best.head()

