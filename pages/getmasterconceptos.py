import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Concepto para Get Master", page_icon="🧑‍🎓")

st.title('Get Master 🧑‍🎓')
st.header("Sistemas Inteligentes de Aprendizaje")

st.write("Bienvenidos al futuro educativo 👋")


a = st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])
b = st.selectbox('Selecciona los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])
c = st.selectbox('Selecciona tus principales pasatiempos', ['Leer', 'Ejercicio', 'Cine'])

h = st.slider('¿Cuántas horas puedes estudiar al día?', 0, 24)

i = st.button('Preparar Hoja de Ruta de Novus Campus🏛️ exclusivo para mí')


if a and b and c and h and i:
  col1, col2, col3 = st.columns(3)
  with col1:
    acelerometro1 = {
          "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
          "series": [
              {
                  "name": "Pressure",
                  "type": "gauge",
                  "axisLine": {
                      "lineStyle": {
                          "width": 10,
                      },
                  },
                  "progress": {"show": "true", "width": 10},
                  "detail": {"valueAnimation": "true", "formatter": "{value}"},
                  "data": [{"value": 30, "name": "Teoría"}],
              }
          ],
      }

    st_echarts(options=acelerometro1)

  with col2:
    acelerometro2 = {
          "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
          "series": [
              {
                  "name": "Pressure",
                  "type": "gauge",
                  "axisLine": {
                      "lineStyle": {
                          "width": 10,
                      },
                  },
                  "progress": {"show": "true", "width": 10},
                  "detail": {"valueAnimation": "true", "formatter": "{value}"},
                  "data": [{"value": 50, "name": "Práctica"}],
              }
          ],
      }

    st_echarts(options=acelerometro2)

  with col3:
    acelerometro3 = {
          "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
          "series": [
              {
                  "name": "Pressure",
                  "type": "gauge",
                  "axisLine": {
                      "lineStyle": {
                          "width": 10,
                      },
                  },
                  "progress": {"show": "true", "width": 10},
                  "detail": {"valueAnimation": "true", "formatter": "{value}"},
                  "data": [{"value": 80, "name": "Evaluación"}],
              }
          ],
      }
    st_echarts(options=acelerometro3)
 
st.write('Con un plan personalizado de ', h,' horas semanales, mediante ejemplos asociados a <<', c, '>> para que aprendas <<', a, '>> y logres aportar a salvar al planeta en <<', b, '>>.'
