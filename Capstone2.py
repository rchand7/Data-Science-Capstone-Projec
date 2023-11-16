import pickle
import streamlit as st


rf = pickle.load(open('C:\\Users\\RAHUL\\rf_model.pkl','rb'))
lr = pickle.load(open('C:\\Users\\RAHUL\\lr_model.pkl','rb'))
knn = pickle.load(open('C:\\Users\\RAHUL\\knn_model.pkl','rb'))


ml_model = ['Logistic Regression','RandomForest Classiifer','KNN Classifier']
cars   =   ['Maruti 800 AC', 'Maruti Wagon R LXI Minor',
       'Hyundai Verna 1.6 SX', ..., 'Mahindra Verito 1.5 D6 BSIII',
       'Toyota Innova 2.5 VX (Diesel) 8 Seater BS IV',
       'Hyundai i20 Magna 1.4 CRDi']
fuel=['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric']
Seller_Type=['Individual', 'Dealer', 'Trustmark Dealer']
Owner=['First Owner','Second Owner','Third Owner','Fourth Owner']

option = st.sidebar.selectbox('Select the ML model',ml_model)
option = st.sidebar.selectbox('Select the car',cars)
sl = st.slider('Select year', 2000,2020)
sw = st.slider('km_driven', 1000,2000000)
option = st.sidebar.selectbox('Select the Fuel type',fuel)
option = st.sidebar.selectbox('Select the Seller_Type',Seller_Type)
option = st.sidebar.selectbox('Select the Owner type',Owner)




test =  [[sl,sw]]

st.write('Test Data')
st.write(test)


if st.button('Classify'):
    res = None
    if option=='Logistic Regression':
        st.success(lr.predict(test)[0])
    elif option=="RandomForest Classiifer":
        st.success(rf.predict(test)[0])
    else:
        st.success(knn.predict(test)[0])

# st.success(res)

