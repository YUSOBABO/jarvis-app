import streamlit as st
from groq import Groq

st.set_page_config(page_title="JARVIS", layout="centered")

st.markdown("""
<style>
    body { background: #000d1a; }
    .main { background: #000d1a; }
    h1 { color: #00aaff !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 J.A.R.V.I.S.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Merhaba efendim. Nasil yardimci olabilirim?"}]

client = Groq(api_key="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")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Bir sey soyleyiniz...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    komut = user_input.lower()
    
    if "tarayici" in komut or "chrome" in komut:
        cevap = "Tarayici aciliyor efendim..."
    elif "youtube" in komut:
        cevap = "YouTube aciliyor efendim..."
    else:
        response = client.chat.completions.create(
           model="llama2-70b-4096"
            messages=[{"role": "user", "content": user_input}],
            max_tokens=300
        )
        cevap = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": cevap})
    with st.chat_message("assistant"):
        st.write(cevap)
