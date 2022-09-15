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
table_data_ts = table_data.set_index(pd.to_datetime(table_data['date_request']))

mean_inf_time = table_data['time_treated'].mean()
mean_input_len = (table_data['input_text'].apply(len)).mean()

st.title('Dashboard of model utilisation')

st.header('Performance')
st.write(f'Mean processing time : {mean_inf_time:.2f}s')
st.write(f'Mean input len : {mean_input_len:.0f} words')

st.header('Plots')
fig, ax = plt.subplots()
table_data['time_treated'].hist(ax=ax)
ax.set_title('Distribution of model inference time')
st.pyplot(fig=fig)

st.header('Number of request by selected sampling time')
dict_options = {'by day':'1D', 'by hour':'1H', 'by minute':'60S'}
choice = st.radio('Select Time Frame', options=dict_options.keys())
table_data_ts = table_data_ts.resample(dict_options[choice]).count()
fig, ax = plt.subplots()
table_data_ts['time_treated'].plot(ax=ax)
ax.set_ylabel(f'Number of model requests {choice}')
st.pyplot(fig=fig)
st.dataframe(data=table_data_ts)

st.header('Model performance by input lenght')
len_input = table_data['input_text'].apply(len)
len_output = table_data['output_text'].apply(len)
fig, ax = plt.subplots()
ax.scatter(x= len_input.values, y= table_data['time_treated'].values)
ax.set_ylabel('Inference time(sec)')
ax.set_xlabel('Text Input Len')
st.pyplot(fig=fig)

# Graphique Distribution de la longueur du texte à résumer : 
st.header('Distribution of length Input texte')
fig, ax = plt.subplots()
len_output.hist(ax=ax, bins=50)
ax.set_title('Distribution of length Input texte')
st.pyplot(fig=fig)

# Graphique Comparaison de la longueur du texte à résumer vs la longueur du texte résumé : 
st.header('Length Input Text VS Output Text')
fig, ax = plt.subplots()
ax.scatter(x= len_input.values, y= len_output.values)
ax.set_ylabel('Length Output Text')
ax.set_xlabel('Length Input Text')
ax.set_title('Length Input Text VS Output Text')
st.pyplot(fig=fig)
st.header('Raw Data')
st.dataframe(data=table_data)

surprise = st.button(label='Ne pas toucher debug only')
if surprise: 
    st.snow()