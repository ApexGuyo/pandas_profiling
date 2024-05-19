import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# title
st.markdown('''# **Exploratory Data Analysis**''')

# uploadinf file section
with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example csv file](df)")
# profiling report
if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    pr.to_file("report.html")
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**PROFILE**')
    st_profile_report(pr)
else:
    st.warning("please upload your file")
