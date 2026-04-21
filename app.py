import streamlit as st
import random
import string

st.set_page_config(page_title="URL Shortener", layout="centered")

# in-memory storage (resets on refresh/redeploy)
if "urls" not in st.session_state:
    st.session_state.urls = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

st.title("🔗 Simple URL Shortener")

url = st.text_input("Enter URL")

if st.button("Generate Short Link"):
    if url:
        code = generate_short_code()
        st.session_state.urls[code] = url

        short_url = f"?code={code}"

        st.success("Short URL:")
        st.code(short_url)
    else:
        st.error("Enter valid URL")

# redirect logic
query_params = st.query_params

if "code" in query_params:
    code = query_params["code"]

    if code in st.session_state.urls:
        st.success("Redirecting...")
        st.markdown(f"[Click here if not redirected]({st.session_state.urls[code]})")
    else:
        st.error("Invalid link")
