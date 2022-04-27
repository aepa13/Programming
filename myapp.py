import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import sqlite3

st.title('Final Project')
image = Image.open('Logo-KDT-JU.webp')
st.image(image)

con = sqlite3.connect('excel_database.db') # Connect

selects = {'country': 'SELECT * FROM countries',
    
'participants': 
           '''SELECT p.shortName, p.name, p.activityType, p.organizationURL, COUNT(*) as projects, SUM(p.ecContribution) as total_grants
            FROM  participants p, projects pr, countries c
            WHERE p.projectID = pr.projectID AND c.Acronym = p.country AND c.Country = '{}'
            GROUP BY p.name ORDER BY SUM(p.ecContribution) DESC''',
    
'grants':
           '''SELECT SUM(o.ecContribution) AS grants
            FROM  organizations o JOIN project p ON o.projectID=p.projectID
            WHERE o.country = '{}'
            GROUP BY p.year '''
}

countries = pd.read_sql(selects['country'], con)
#grants = pd.read_sql(selects['grants'], con)
selection = st.selectbox('', list(countries['Country']))

df = pd.read_sql(selects['participants'].format(selection), con)
st.dataframe(df)

st.bar_chart(participants)
