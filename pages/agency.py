import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
import pydeck as pdk
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Agency", page_icon="💡")

st.title('Novus Agency 💡')
st.header("AI Automating Agency")
st.write("Wellcome to the Freelancing Future 👋")
st.markdown(
  """
  In this web you can find:
  - 📊 _    Talent Monitor Finder
  - 📆 _    Curriculum Vitae Generator
  - 🧠 _    Top 10 Major Paid Skills
  
  Start now 🕰
  """
)


st.title('Talent Monitor Fider')
#datos
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [6.15333, -75.374166],
columns=['lat', 'lon'])
st.pydeck_chart(pdk.Deck(
map_style=None,
initial_view_state=pdk.ViewState(
latitude=6.153333,
longitude=-75.374166,
zoom=11,
pitch=50,
),
layers=[
pdk.Layer(
   'HexagonLayer',
   data=df,
   get_position='[lon, lat]',
   radius=200,
   elevation_scale=4,
   elevation_range=[0, 1000],
   pickable=True,
   extruded=True,
),
pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
),
],
))


st.title('Curriculum Vitae Generator')
col1, col2 = st.columns(2)

with col1:
    territorio = st.selectbox(
        "Select a territory",
        ("Netherlands", "UK", "France", "Germany", "Spain"),
    )
    categoria = st.radio(
        "Select an industry",
        options=['Aerospace', 'Agro','Finance', 'Retail', 'Entertaiment'],
    )

with col2:
    redsocial = st.selectbox(
        "Select the social network from generate Curriculum Vitae",
        ("Facebook", "Instagram", "Twitter", "Google"),
    )
    perfil = st.text_input('Paste the URL of your Profile', '''
    ''')
    otroscandidatos =  st.text_input('Paste the URL of your 1st Reference Profile', '''
    ''')

a = st.selectbox('Choose your principal role:', ['Data Scientist', 'Broker', 'ML Operator'])
b = st.selectbox('Select your experience:', ['Hambre', 'Pobreza', 'Educacion'])
c = st.selectbox('Select your hobbies:', ['Leer', 'Ejercicio', 'Cine'])

h = st.slider('How many years of experience?', 0, 24)

i = st.button('Create my Personal Curriculum Vitae 🤖')

st.write('Con un plan personalizado de ', h,' horas semanales, mediante ejemplos asociados a <<', c, '>> para que aprendas <<', a, '>> y logres aportar a salvar al planeta en <<', b, '>>.')


st.title('Top 10 Major Paid Skills')





def render_basic_radar():
    option = {
        "title": {"text": "Diagnóstico Personalizado de Brecha de Conocimiento"},
        "legend": {"data": ["Estado Actual de Alumno", "Meta de Aprendizaje"]},
        "radar": {
            "indicator": [
                {"name": "Conceptos", "max": 6500},
                {"name": "Teorías", "max": 16000},
                {"name": "Modelos", "max": 30000},
                {"name": "Casos de Estudio", "max": 38000},
                {"name": "Ejercicios", "max": 52000},
                {"name": "Examen VideoLlamada", "max": 25000},
            ]
        },
        "series": [
            {
                "name": "Aprendizaje Actual Vs Proyectado",
                "type": "radar",
                "data": [
                    {
                        "value": [2000, 3000, 2000, 3500, 15000, 11800],
                        "name": "Estado Actual de Alumno",
                    },
                    {
                        "value": [6500, 16000, 30000, 38000, 52000, 25000],
                        "name": "Meta de Aprendizaje",
                    },
                ],
            }
        ],
    }
    st_echarts(option, height="500px")


ST_RADAR_DEMOS = {
    "Radar: Basic Radar": (
        render_basic_radar,
        "https://echarts.apache.org/examples/en/editor.html?c=radar",
    ),
}

render_basic_radar()




