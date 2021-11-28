import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # nopep8

import streamlit as st
import tensorflow as tf

import cv2
from PIL import Image, ImageOps
import numpy as np

dir_ = "\\".join(os.path.realpath(__file__).split("\\")[:-1])

st.set_option('deprecation.showfileUploaderEncoding', False)

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model(os.path.join(dir_, 'Alzheimers_Model_2.hdf5'))
    return model

with st.spinner('Model is being loaded..'):
    model = load_model()


def app():
    st.title("Alzhiemers Prediction")
    file = st.file_uploader("Please upload an alzhiemer's image", type=["jpg", "png"])
    def import_and_predict(image_data, model):
        image = np.asarray(image_data)[np.newaxis, ..., np.newaxis]
        prediction = model.predict(image)

        return prediction

    if file is None:
        st.text("Please upload an image file")
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        predictions = import_and_predict(image, model)
        class_names = ["MildDemented" ,"ModerateDemented", "NonDemented", "VeryMildDemented"]
        strg = "This image most likely is: "+ class_names[np.argmax(predictions)]
        st.success(strg)
