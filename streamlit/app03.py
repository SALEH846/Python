import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from streamlit.proto.Checkbox_pb2 import Checkbox

st.title("BigMac Index")

@st.cache
def load_data():
    col_list = ["date", "currency_code", "name", "local_price", "dollar_ex"]
    data = pd.read_csv("bigmac.csv", usecols=col_list)
    return data.assign(date = lambda d: pd.to_datetime(d['date']))

df = load_data()

countries = st.sidebar.multiselect(
    "Select Countries",
    df["name"].unique()
)

varname = st.sidebar.selectbox(
    "Select column",
    ("local_price", "dollar_ex")
)

subset_df = df.loc[lambda d: d['name'].isin(countries)]

fig, ax = plt.subplots()
for name in countries:
    plotset = subset_df.loc[lambda d: d['name'] == name]
    ax = plt.plot(plotset['date'], plotset[varname], label=name)
plt.legend()
st.pyplot(fig)

if st.sidebar.checkbox("Show Raw Data"):
    st.markdown("### Raw Data")
    st.write(subset_df)