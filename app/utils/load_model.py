import pickle
import streamlit as st


@st.cache_resource
def load_model(path_model):
    with open(path_model, "rb") as file:
        return pickle.load(file)
