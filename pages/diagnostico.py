import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Campus", page_icon="🏛️")

st.title('Novus Campus 🏛️')

st.header("Define tu meta ✍️")
st.subheader("Prepárate para alcanzarla 🎯")
st.subheader("Monitorea Paso a Paso 👣 la Materialización ✅")


st.title('Define tu esencia')

st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])
st.multiselect('Selecciona los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])
st.multiselect('Selecciona tus principales pasatiempos', ['Leer', 'Ejercicio', 'Cine'])
st.text_input('Indícanos actualmente en qué te ganas la vida')


st.button('Preparar Mando de Novus Vita exclusivo para mí')
