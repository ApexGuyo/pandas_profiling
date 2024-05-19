import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import time

st.set_page_config(page_title="Data Profiling")

# title
st.title('Exploratory Data Analysis')

st.markdown('''---''')

# uploadinf file section
with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
 # st.sidebar.markdown("[Example csv file](df)")
# profiling report


if uploaded_file is not None:

    with st.spinner(text='In progress'):
        time.sleep(3)

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
    st.warning(" ## ***please upload your csv file for Data Analysis***")


footer_html = """<div style='text-align: center;'>
  <p>Developed ❤️ by Guyo </p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)
