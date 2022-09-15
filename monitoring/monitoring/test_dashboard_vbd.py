import streamlit as st
import pandas as pd
import numpy as np
from db_utils import get_engine, verify_database

def load_data(conn, table):
    return pd.read_sql_table(table, con = conn)

verify_database()
cnx = get_engine()
my_df = load_data(cnx, "text_summarize")

st.subheader('Raw data')
st.write(my_df)