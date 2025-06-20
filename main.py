import streamlit as st
from transformers import pipeline
import soundfile as sf
import tempfile
import numpy as np

@st.cache_resource
def load_tts_model():
    return pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")

text_speech = load_tts_model()


st.title("🗣️ Text to Speech with Hugging Face VITS")
st.markdown("Type your text below and click 'Generate Speech' to hear it!")

# Text input
user_input = st.text_area("Enter your text:")

# Button to generate speech
if st.button("🔊 Generate Speech"):
    with st.spinner("Generating audio..."):
        # Generate speech using raw text (let pipeline handle phonemization)
        result = text_speech(user_input)
        audio = result["audio"]
        # Ensure audio is a 1D numpy array of float32
        audio_data = np.array(audio, dtype=np.float32).flatten()
        # Save audio to temporary file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            sf.write(f.name, audio_data, result["sampling_rate"], format='WAV', subtype='PCM_16')
            audio_path = f.name
        st.audio(audio_path, format="audio/wav")
        st.success("✅ Speech generated!")


