import streamlit as st
import pickle
import numpy as np
import pandas as pd

df=pd.read_excel("CAR_DETAILS.xlsx")
lrr = pickle.load(open('lrr_modell.pkl','rb'))
dtt = pickle.load(open('dtt_modell.pkl','rb'))
rff = pickle.load(open('rff_modell.pkl','rb'))



st.title('Car price prediction Web App')
st.subheader('Fill the below Details to predict Car Price Charges')


model = st.sidebar.selectbox('Select the ML Model',['Lin_Reg','DT_Reg','RF_Reg'])


# age 	sex 	bmi 	children 	smoker 	charges 	
# region_northwest 	region_southeast 	region_southwest

name = st.selectbox,('name',df['CAR DETAILS'].unique())
year = st.slider('year',1950,2023)
km_driven= st.slider('km_driven',0,200000)
fuel= st.selectbox('fuel',['Petrol','Diesel','CNG','LPG','Electric'])
seller_type = st.selectbox('seller_type',['Individual','Dealer','Trustmark_Dealer'])
transmission = st.selectbox('transmission',['Manual','Automatic'])
owner = st.selectbox('owner',['First_Owner','Second_Owner','Third_Owner','Fourth_Above_Owner','Test_Drive_Car'])


if st.button('Predict Car Price Charges'):
    if fuel=='Petrol':
        Petrol = 1
        Diesel=0
        CNG=0
        LPG=0
        Electric=0
    elif fuel == "Diesel": 
        Petrol = 0
        Diesel=1
        CNG=0
        LPG=0
        Electric=0
    elif fuel == "CNG": 
        Petrol = 0
        Diesel=0
        CNG=1
        LPG=0
        Electric=0
    elif fuel == "LPG": 
        Petrol = 0
        Diesel=0
        CNG=0
        LPG=1
        Electric=0
    else: 
        Petrol = 0
        Diesel=0
        CNG=0
        LPG=0
        Electric=1

    if seller_type == "Individual":
        Individual = 1
        Dealer =0
        Trustmark_Dealer= 0

    elif seller_type == "Dealer": 
        Individual = 0
        Dealer =1
        Trustmark_Dealer= 0

    else:
        Individual = 0
        Dealer =0
        Trustmark_Dealer= 1

    if owner=="First_Owner":
        First_Owner = 1
        Second_Owner = 0
        Third_Owner = 0
        Fourth_Above_Owner = 0
        Test_Drive_Car= 0

    elif owner == "Second_Owner":
        First_Owner = 0
        Second_Owner = 1
        Third_Owner = 0
        Fourth_Above_Owner = 0
        Test_Drive_Car= 0

    elif owner =="Third_Owner":
        First_Owner = 0
        Second_Owner = 0
        Third_Owner = 1
        Fourth_Above_Owner = 0
        Test_Drive_Car= 0

    elif owner =="Fourth_Above_Owner":
        First_Owner = 0
        Second_Owner = 0
        Third_Owner = 0
        Fourth_Above_Owner = 1
        Test_Drive_Car= 0

    else:
        First_Owner = 0
        Second_Owner = 0
        Third_Owner = 0
        Fourth_Above_Owner = 0
        Test_Drive_Car= 1


    test = np.array([name,year,km_driven,fuel,seller_type,transmission,owner])
    test = test.reshape(1,8)
    if model == "Lin_Reg":
        st.success(lrr.predict(test)[0])
    elif model == "DT_Reg":
        st.success(dtt.predict(test)[0])
    else:
        st.success(rff.predict(test)[0])

















# To run Streamlit Web App
# streamlit run app.py









