import streamlit as st
from PIL import Image

### Cheat-Sheet Streamlit ### https://cheat-sheet.streamlit.app/

#-#-# TÍTULO #-#-#
st.title(':male-farmer:   Plataforma Sensor:green[Green]	:male-technologist:')

#-#-# IMAGEM LOGO #-#-#
image = Image.open('logo.png')
st.image(image)

#-#-# AUDIO #-#-#
audio_file = open('cafe2.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

audio_file = open('whats2.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/ogg")

#-#-# DESCRIÇÃO #-#-#
st.text('Aqui aparecerá a transcrição do áudio!')