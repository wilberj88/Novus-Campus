import streamlit as st
import numpy as np

st.title('Novus Atento 🤖 en Novus Campus 🏛️')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.markdown(message["👋Bienvenido a Novus Campus 🏛️, soy tu profe Atento 🤖: dime ¿qué opinas de la siguiente gráfica"])
        st.bar_chart(np.random.randn(30, 3))

prompt = st.chat_input("Tienes 30 segundos para tu respuesta...")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
