import streamlit as st
import random
import string

st.set_page_config(page_title="URL Shortener", layout="centered")

# ---------- STATE ----------
if "urls" not in st.session_state:
    st.session_state.urls = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.main-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    text-align: center;
    color: white;
}

.title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 16px;
    color: #cfcfcf;
    margin-bottom: 30px;
}

.stTextInput>div>div>input {
    border-radius: 12px;
    padding: 12px;
}

.stButton button {
    width: 100%;
    height: 45px;
    border-radius: 12px;
    background: linear-gradient(90deg,#ff416c,#ff4b2b);
    color: white;
    font-size: 16px;
    border: none;
}

.stButton button:hover {
    background: linear-gradient(90deg,#ff4b2b,#ff416c);
}

.result-box {
    background: rgba(0,0,0,0.4);
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown("<div class='title'>🔗 Smart URL Shortener</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Fast • Minimal • Clean Experience</div>", unsafe_allow_html=True)

url = st.text_input("Paste your long URL")

if st.button("Generate Short Link"):
    if url:
        code = generate_short_code()
        st.session_state.urls[code] = url
        short_url = f"?code={code}"

        st.markdown(f"""
        <div class='result-box'>
            <b>Your Short URL:</b><br><br>
            <a href="{short_url}" target="_blank" style="color:#4fc3f7; font-size:18px;">
                {short_url}
            </a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter a valid URL")

# ---------- REDIRECT ----------
query_params = st.query_params

if "code" in query_params:
    code = query_params["code"]

    if code in st.session_state.urls:
        st.success("Redirecting...")
        st.markdown(f"[Click here]({st.session_state.urls[code]})")
    else:
        st.error("Invalid or expired link")

st.markdown("</div>", unsafe_allow_html=True)
