import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Campus", page_icon="🏛️")

st.title('Novus Campus 🏛️')

st.header("Define tu meta ✍️")
st.subheader("Prepárate para alcanzarla 🎯")
st.subheader("Monitorea Paso a Paso 👣 la Materialización ✅")

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')
