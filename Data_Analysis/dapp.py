import streamlit as st  #helps in designing UI 
#CD DATA ANALYSIS
#streamlit run dapp.py
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
# title of the app
st.title('Data Analysis App')

def load_data():
    df = sns.load_dataset('titanic')
    return df 

with st.spinner('Loading Data..'):
    df = load_data()
    st.write("😁😁")


if st.checkbox("View All Data"):
   st.dataframe(df)

if st.checkbox("Show Some Statistics"):
    cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    c1,c2  = st.columns(2)
    
    c1.metric(label="Average Age OF Passengers",value=df['age'].mean().astype(int))
    c2.metric(label="Average Fare",value=df['fare'].mean().astype(int),delta=round(df['fare'].std(),1))
    c1,c2 = st.columns(2)
    c1.text("Number of Survivors")
    c1.dataframe(df['survived'].value_counts())
    c1.dataframe(survivors) 
    fig = px.pie(survivors,survivor.index,survivors.values)
    c1.plotly_chart(fig, use_container_width=True)
    c2.text("Number of Passengers in Each Class")
    classes = df['pclass'].value_counts()
    c2.dataframe(classes)
    fig = px.bar(classes,classes.index, classes.values)
    c2.plotly_chart(fig, use_container_width=True)

#if st.checkbox("visualize categorical data"):
 #   st.subheader("Categorical Data Visualization")
  #  st_col = st.radio("Select Column", cat_cols, horizontal=True)
   # set_col_count = df[sel_col].value_counts()
    #fig = px.pie(set_col_count, sel_col_count.index,sel_col_count.index,sel_col_count.values, title=)
if st.checkbox("visualize categorical data"):
    graph_type = ['Area', 'Line', 'Histogram', 'Boxplot', 'Violinplot',]
    st.subheader("Numerical data visualization")
    set_col = st.selectbox("select columns",num_cols)
    graph_type = st.radio('Select Graph Type', graph_types, horizontal=True)
    if graph_type == graph_type[0]:
            fig = px.area(df, y =set_col, title=f"Area Plot of {set_col}")
            fig2 = px.histogram(df, x=set_col, title=f"Histogram of {set_col}")
            c1, c2 = st.columns(2)
            c1.plotly_chart(fig, use_container_width=True)
            c2.plotly_chart(fig2, use_container_width=True)
            if graph_type == graph_type[0]:

    if graph_type == graph_type[0]:

    if graph_type == graph_type[0]:

    if graph_type == graph_type[0]:


