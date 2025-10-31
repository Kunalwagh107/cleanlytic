import streamlit as st
import numpy as np
import pandas as pd
from utils.file_validation import file_validation


st.header('Cleanlytic')

st.write('This is file cleaner tool powered by pandas and you can use it to clean your csv files without doing any code')

upload_file = st.file_uploader('Choose CSV to upload',type=['csv'])
file_validation(upload_file)


