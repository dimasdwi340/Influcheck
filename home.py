import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_f74ijzbr.json")

with st.container():
    st.write("""
    ### InfluCheck
    ---""")

with st.container():
    st.write("""
            <h2 style='text-align: center;'>
            Cari tau yuk!
            </h2>""", unsafe_allow_html=True)
    st_lottie(lottie_coding, height = 300, key = "home")

with st.container():
    left, center, right = st.columns((1,2,1))
    with center:
        username = st.text_input("")