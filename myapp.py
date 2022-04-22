import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import sqlite3

st.title('Final Project')
image = Image.open('Logo-KDT-JU.webp')
st.image(image)

con = sqlite3.connect('excel_database.db') # Connect

selects = {'country': 'SELECT Acronym FROM countries',
    
    'participants':
    '''SELECT p.shortName, p.name, p.activityType, p.organizationURL, COUNT(*) as projects, SUM(p.ecContribution) as total_grants
        FROM  participants p, projects pr, countries c
        WHERE p.projectID = pr.projectID AND c.Acronym = p.country AND c.Country = '{}'
        GROUP BY p.name ORDER BY SUM(p.ecContribution) DESC'''}

st.selectbox('Pick a European country',to_list(selects['country']))

df = pd.read_sql(selects['participants'], con)
st.dataframe(df)
