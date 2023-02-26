import seaborn as sn
import matplotlib.pyplot as plt
from matplotlib import image
import streamlit as st
import pandas as pd
import os
import plotly.express as px

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "Screenshot (130).png")
DATA_PATH = os.path.join(dir_of_interest, "data", "diamonds.csv")

st.title("Dashboard: Diamond Data")

df = pd.read_csv(DATA_PATH)

im = image.imread(IMAGE_PATH)

st.image(im)

st.header("Dataset:")

st.dataframe(df)

st.subheader("Proportion of each type of cut in the Dataset: ")

df2 = df["cut"].value_counts()
fig_3 = px.pie(df, values = df2, names = df2.index)
st.plotly_chart(fig_3)

Cut = st.selectbox("Select the type of cut:", df["cut"].unique())


chart = st.radio("Please select the type of visualization chart you want to view:", ("Histogram", "Boxplot", "Both"))


col1, col2 = st.columns(2)

if(chart == "Histogram"):
    fig_1 = px.histogram(df[df["cut"] == Cut], x = "carat")
    st.plotly_chart(fig_1, use_container_width=True)


elif(chart == "Boxplot"):
    fig_2 = px.box(df[df["cut"] == Cut], y = "carat")
    st.plotly_chart(fig_2, use_container_width=True)

elif(chart == "Both"):

    fig_1 = px.histogram(df[df["cut"] == Cut], x = "carat")
    col1.plotly_chart(fig_1, use_container_width=True)

    fig_2 = px.box(df[df["cut"] == Cut], y = "carat")
    col2.plotly_chart(fig_2, use_container_width=True)


















