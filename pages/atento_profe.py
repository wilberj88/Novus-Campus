import streamlit as st
import numpy as np

with st.chat_message("user"):
    st.write("👋Bienvenido a Novus Campus 🏛️, soy tu profe Atento 🤖: dime qué opinas de la siguiente gráfica?")
    st.bar_chart(np.random.randn(30, 3))
