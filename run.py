import streamlit as st
from audio_transcribe import audio
value = audio(stream=True)
st.write(value)