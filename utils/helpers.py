import numpy as np
import pandas as pd
import streamlit as st


# count the columns in the uploaded data
def count_rows(dataframe):
    return st.write(f'number of rows in data frame is {len(dataframe)}')