import streamlit as st
from db_utils import PGSQL_DB
import pandas as pd
import matplotlib.pyplot as plt

mydb = PGSQL_DB()
mydb.connect_to_default_db()

data = mydb.get_table()

table_data = pd.read_sql_table(
    table_name='text_summarize',
    con = mydb.engine,
    index_col='id'
)

table_data = table_data[['date_request','time_treated','input_text','output_text']]

mean_inf_time = table_data['time_treated'].mean()
mean_input_len = (table_data['input_text'].apply(len)).mean()

st.title('Dashboard of model utilisation')

st.header('Performance')
st.write(f'Mean processing time : {mean_inf_time:.2f}s')
st.write(f'Mean input len : {mean_input_len:.0f} words')

st.header('Plots')
fig, ax = plt.subplots()
ax = table_data['time_treated'].hist(ax=ax)
st.pyplot(fig=fig)

st.header('Raw Data')
st.dataframe(data=table_data)

st.snow()
