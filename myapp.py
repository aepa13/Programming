import pandas as pd
import streamlit as st
from PIL import Image
import sqlite3

st.title('Partner Search App')
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
           '''SELECT pr.year, SUM(p.ecContribution) as total_grants
            FROM  participants p, projects pr, countries c
            WHERE p.projectID = pr.projectID AND c.Acronym = p.country AND c.Country = '{}'
            GROUP BY pr.year''',
           
'coordinators':
           '''SELECT p.shortName, p.name, p.activityType, pr.acronym, pr.objective
            FROM participants p, projects pr, countries c
            WHERE c.Acronym = p.country AND pr.projectID = p.projectID AND p.role = 'coordinator' AND c.Country = '{}' '''
}

countries = pd.read_sql(selects['country'], con)
selection = st.selectbox('', list(countries['Country']))

grants = pd.read_sql(selects['grants'].format(selection), con)
bar = grants.set_index('year')
st.title('Grants per year')
st.bar_chart(bar)

chart = pd.read_sql(selects['participants'].format(selection), con)
st.title('Contributions')
st.dataframe(chart)

st.download_button(
     label="Download data as CSV",
     data = chart.to_csv(),
     file_name='contributions.csv',
     mime='text/csv',
 )

coordinators = pd.read_sql(selects['coordinators'].format(selection), con)
st.title('Coordinators')
st.dataframe(coordinators)

st.download_button(
     label="Download data as CSV",
     data = coordinators.to_csv(),
     file_name='coordinators.csv',
     mime='text/csv',
 )


