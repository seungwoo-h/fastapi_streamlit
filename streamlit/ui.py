import requests
import pandas as pd
import streamlit as st

backend_csv = 'http://localhost:8000/csv'
backend_single = 'http://localhost:8000/inference'

st.title("Test")

inp_csv = st.file_uploader("csv 업로드")
if inp_csv:
    st.write("Before")
    df = pd.read_csv(inp_csv)
    st.write(df)

    r = requests.post(
        backend_csv, {'file': inp_csv.getvalue()}
    )
    st.write(pd.read_json(r.content))

s = st.text_input("입력")

st.write(type(s))
if s:
    r2 = requests.post(
        backend_single, json={'merch_name': s}
    )
    st.write(r2.content.decode())