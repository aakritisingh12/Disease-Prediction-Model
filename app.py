import streamlit as st
from multiapp import Multiapp
import Covid, BreastCancer, Alzheimers, Home

app = Multiapp()

# st.markdown("""
#     # Multi - Page App
#
#     bla bla bla bla bla
# """)


app.add_app("Home", Home.app)
app.add_app("Covid-Prediction", Covid.app)
app.add_app("Breast-Cancer Prediction", BreastCancer.app)
app.add_app("Alzhiemer- Prediction", Alzheimers.app)

app.run()
