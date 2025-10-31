import numpy as np
import pandas as pd
import streamlit as st
from utils.helpers import count_rows


def file_validation(user_uploaded_file):

    if user_uploaded_file is not None :
        try:
            df = pd.read_csv(user_uploaded_file)

            st.success(f'File Uploaded Successfully')
            st.dataframe(df)
            count_rows(df)
            st.write(f"**File:** {user_uploaded_file.name}")
            st.write(f"**Size:** {user_uploaded_file.size} bytes")
            st.write(f"**Type:** {user_uploaded_file.type}")

        except Exception as e :
            st.error(f'error loading the file : {e}')
