import pickle
import streamlit as st
import numpy as np


with open('Breast Cancer_Classifierf.pickle', 'rb') as f:
    clf = pickle.load(f)
    print(clf)

def app():
    st.title("Breast-Cancer Prediction")
    rm = st.number_input("Radius mean", format="%.5f", min_value=0.00000)#1
    tm = st.number_input("Texture mean", format="%.5f", min_value=0.00000)#2
    pm = st.number_input("Perimeter mean", format="%.5f", min_value=0.00000)#3
    am = st.number_input("Area mean", format="%.5f", min_value=0.00000)#4
    sm = st.number_input("smoothness mean", format="%.5f", min_value=0.00000)#5
    cm  = st.number_input("Compactness mean", format="%.5f", min_value=0.00000)#6
    cam = st.number_input("Concavity mean", format="%.5f", min_value=0.00000)#7
    copm = st.number_input("Concave points mean", format="%.5f", min_value=0.00000)#8
    sym = st.number_input("Symmetry mean", format="%.5f", min_value=0.00000)#9
    # fdm = st.number_input("Fractal dimension mean", format="%.5f", min_value=0.00000)#10
    rse = st.number_input("Radius se", format="%.5f", min_value=0.00000)#11
    tse = st.number_input("Texture se", format="%.5f", min_value=0.00000)#12
    pse = st.number_input("Perimeter se", format="%.5f", min_value=0.00000)#13
    ase = st.number_input("Area se", format="%.5f", min_value=0.00000)#14
    # sse = st.number_input("Smoothness se", format="%.5f", min_value=0.00000)#15
    cse = st.number_input("Compactness se", format="%.5f", min_value=0.00000)#16
    cose = st.number_input("Concavity se", format="%.5f", min_value=0.00000)#17
    copse = st.number_input("Concave points se", format="%.5f", min_value=0.00000)#18
    # syse = st.number_input("symmetry se", format="%.5f", min_value=0.00000)#19
    fdse = st.number_input("Fractal dimension se", format="%.5f", min_value=0.00000)#20
    rw =st.number_input("Radius Worst", format="%.5f", min_value=0.00000)#21
    # Tw = st.number_input("Texture worst", format="%.5f", min_value=0.00000)#22
    pw = st.number_input("Perimeter worst", format="%.5f", min_value=0.00000)#23
    aw = st.number_input("Area worst", format="%.5f", min_value=0.00000)#24
    sw = st.number_input("smoothness worst", format="%.5f", min_value=0.00000)#25
    cw = st.number_input("Compactness worst", format="%.5f", min_value=0.00000)#26
    cow = st.number_input("Concavity worst", format="%.5f", min_value=0.00000)#27
    cpw = st.number_input("Concave points worst", format="%.5f", min_value=0.00000)#28
    syw = st.number_input("Symmetry worst", format="%.5f", min_value=0.00000)#29
    fdw = st.number_input("Fractal dimension worst", format="%.5f", min_value=0.00000)#30




    arr= [[rm, tm, pm, am, sm, cm, cam, copm, sym, rse, tse, pse, ase, cse, cose, copse, fdse, rw, pw, aw, sw, cw, cow, cpw, syw, fdw]]
    # x = StandardScaler().fit_transform(arr)

    val = np.asarray([rm, tm, pm, am, sm, cm, cam, copm, sym, rse, tse, pse, ase, cse, cose, copse, fdse, rw, pw, aw, sw, cw, cow, cpw, syw, fdw])


    if st.button('Predict'):

        # result = clf.predict(rm, tm, pm, am, sm, cm, cam, copm, sym, fdm, rse, tse, pse, ase, sse, cse, cose, copse, syse, fdse, rw, Tw, pw, aw, sw, cw, cow, cpw, syw, fdw)
        result = clf.predict(val.reshape(1, -1))[0]
        # model.predict(values.reshape(1, -1))[0]

        print(result)
        if result == 0:
            st.success("No Cancer!!")

        elif result == 1:
            st.success("Cancer!!")
