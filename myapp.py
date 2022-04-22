import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

st.title('Final Project')
image = Image.open('Logo-KDT-JU.webp')
st.image(image)

participants = pd.read_excel('participants.xlsx')
projects = pd.read_excel('projects.xlsx')
countries = pd.read_excel('countries.xlsx')

pd.options.display.float_format = '{:.2f}'.format

con = sqlite3.connect('ecsel_database.db') # Connect

participants.to_sql('participants', con , if_exists='replace', index=True)
projects.to_sql('projects', con , if_exists='replace', index=True)
countries.to_sql('countries', con , if_exists='replace', index=True)

database = 'ecsel_database.db'

selects = {
    'participants':
    '''SELECT p.shortName, p.name, p.activityType, p.organizationURL, COUNT(*) as projects, SUM(p.ecContribution) as total_grants
        FROM  participants p, projects pr, countries c
        WHERE p.projectID = pr.projectID AND c.Acronym = p.country AND c.Country = '{}'
        GROUP BY p.name ORDER BY SUM(p.ecContribution) DESC'''    
}

df = pd.read_sql(selects['participants'].format(st.selectbox(countries['Country']), con)
