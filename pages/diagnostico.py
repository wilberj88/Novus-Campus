import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Campus", page_icon="🏛️")

st.title('Novus Campus 🏛️')

st.header("Define tu meta ✍️")
st.subheader("Prepárate para alcanzarla 🎯")
st.subheader("Monitorea Paso a Paso 👣 la Materialización ✅")

a = st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])
b = st.multiselect('Selecciona los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])
c = st.multiselect('Selecciona tus principales pasatiempos', ['Leer', 'Ejercicio', 'Cine'])

h = st.slider('¿Cuántas horas puedes estudiar al día?', 0, 24)

i = st.button('Preparar Hoja de Ruta de Novus Campus🏛️ exclusivo para mí')


if a and b and c and h and i:
  st.write('Perfecto, hemos preparado la mejor hoja de ruta para que logres aportar a salvar al planeta en <<', b, '>> con tu aprendizaje en <<', a, '>> mediante ejemplos asociados a <<', c, '>>.')


