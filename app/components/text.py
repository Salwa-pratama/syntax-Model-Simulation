import streamlit as st

def text(value, color="#FF8C00", ukuran="50px", text_align="left"):
    st.markdown(
            f"<h1 style='color: {color}; font-size: {ukuran}; text-align: {text_align};'>{value}</h1>",
            unsafe_allow_html=True
        )

