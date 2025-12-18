import streamlit as st
st.title("My firts project")
name=st.text_imput("What is your name")
if name:
  st.write(f"Hello, {name}!")
