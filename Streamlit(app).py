import streamlit as st
import time as t 
#title- It is used to add the title of an app
st.title("Welcome to Intellipat")

#Header
st.header("Machine Learning")

#sub header
st.subheader("Linear Regression")

#Information
st.info("Information details of a user")

#Warning message
st.warning("Come on time or else you will be mark absent")

#write
st.write("Employee Name")
st.write("range(50)")

#Error message
st.error("Wrong Password")

#Success message
st.success("Congrats you have got a good grade")

#markdown
st.markdown("Intellipat")

st.markdown(":moon:")

st.text("Intellipat learners")

#To write a caption
st.caption("Caption is here")

#to display a mathematical equation
st.latex(r'''a+b x^2+c''')



#Widget
st.checkbox('Login')
#button
st.button("Click")

#Radio Widget

st.radio("Pick your gender",["Male","Female","other"])

#Select box
st.selectbox("Pick your course",["ML","cloud","Cyber security"])

#multiselect
st.multiselect("Choose the dept",["Content","Sales","Marketing"])

#Selectslider
st.select_slider("Rating",["Bad","Good","Excellent","Outstanding"])

#slider
st.slider("Enter your number",0,100)

#number_input
st.number_input("Pick a number", 0,100)

#text input
st.text_input("Enter your Email address")

#date input
st.date_input("Opening Ceremony")

#time input
st.time_input("Hey whats the timing")

#text area
st.text_area("Welcome to the intellipat website. Hello learners")

st.file_uploader("upload your file/folder")

st.color_picker("color")
st.progress(90)

#spinner

with st.spinner('Just wait'):
    t.sleep(5)

st.balloons()

#sidebar
st.sidebar.title("Welcome to Intellipat")
st.sidebar.text_input("Password")

st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])



#Data Visualisation

import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)

