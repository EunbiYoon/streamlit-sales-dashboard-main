import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SVC Dashboard", page_icon=":hand:", layout="wide")


df = pd.read_excel(
        io="Part Nonpart svc.xlsx",
        engine="openpyxl",
        sheet_name="sheet1",
        skiprows=0,
        usecols="D:T",
        nrows=1000,
    )

## --- sidebar ---
st.sidebar.header("Please filter here: ")
model=st.sidebar.multiselect(
    "Select the Model:",
    options=df["MODEL"].unique(),
    default=df["MODEL"].unique()
)

cause_cd=st.sidebar.multiselect(
    "Select the Cause:",
    options=df["CAUSE_CD"].unique(),
    default=df["CAUSE_CD"].unique()
)

repair_cd1=st.sidebar.multiselect(
    "Select the Repair:",
    options=df["REPAIR_CD1"].unique(),
    default=df["REPAIR_CD1"].unique()
)

## 중복 되는 것
df_selection = df.query(
    "MODEL == @model & CAUSE_CD == @cause_cd & REPAIR_CD1 == @repair_cd1"
)

st.dataframe(df_selection)



