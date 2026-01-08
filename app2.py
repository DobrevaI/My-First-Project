import streamlit as st
import numpy as np
from PIL import image
import joblib
import requests
import io

st.set_page_config(page_title="Handwritten Digit Recognition")
st.title("Handwritten Digit Recognition")
st.write("Upload a handwritten digitimage and AI will try to recognise it.")

@st.cache_resource
def load_model():
  try:
    from sklearn.datasets import load_digits
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split

    digits = load_digits()
    X = digits.images.reshape((len(digits.images), -1)) / 16.0
    y = digits.target
    X_train, _, y_train, _ = train_test_split
