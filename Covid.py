import pickle
import streamlit as st

with open('Covid_Classifier.pickle', 'rb') as f:
    clf = pickle.load(f)
    print(clf)

def app():
    st.title('Covid-Prediction')
    bp = st.selectbox('Breathing Problem', ("No", "Yes"))
    fv = st.selectbox('Fever', ("No", "Yes"))
    dc = st.selectbox('Dry Cough', ("No", "Yes"))
    sth = st.selectbox('Sore throat', ("No", "Yes"))
    rn = st.selectbox('Running Nose', ("No", "Yes"))
    As = st.selectbox('Asthama', ("No", "Yes"))
    cld = st.selectbox('Chronic Lung Disease', ("No", "Yes"))
    ha = st.selectbox('Headache', ("No", "Yes"))
    hd = st.selectbox('Heart Disease', ("No", "Yes"))
    dia = st.selectbox('Diabetes', ("No", "Yes"))
    hte = st.selectbox('Hyper Tension', ("No", "Yes"))
    fa = st.selectbox('Fatique', ("No", "Yes"))
    ga = st.selectbox('Gastrointestenial', ("No", "Yes"))
    At = st.selectbox('Abroad Travel', ("No", "Yes"))
    CC = st.selectbox('Contact with covid patient', ("No", "Yes"))
    Al = st.selectbox('Attended large gatherings', ("No", "Yes"))
    VP = st.selectbox('Visited public exposed places', ("No", "Yes"))
    FW = st.selectbox('Family working in public exposed places', ("No", "Yes"))
    WM = st.selectbox('Wearing masks',("No", "Yes"))
    Sa = st.selectbox('Sanitization from market', ("No", "Yes"))

    arr = [bp, fv, dc, sth, rn, As, cld, ha, hd, dia, hte, fa, ga, At, CC, Al, VP, FW, WM, Sa]
    for i in range(len(arr)):
        if arr[i]=="Yes":
            arr[i]=1
        else:
            arr[i]=0



    if st.button('Predict'):

        result = clf.predict(
            [arr]
        )

        if result == 0:
            st.success('Least Chances of having covid-19!')

        else:
            st.success('High chances of having covid-19!')
