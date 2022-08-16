
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_elements import Elements


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_UWktQI.json")
lottie_coding2 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_hdiNFs.json")

st.set_page_config(page_title="Landing Page", page_icon="🏠", layout="wide")
with st.container():
    st.title("""
    InSona
    ---""")
with st.container():
    st.write("""
            <h2 style='text-align: center;'>
            Kenali influencermu, pilihan tepat bagi bisnismu!
            </h2>""", unsafe_allow_html=True)
    st_lottie(lottie_coding, height = 500, key = "landing")

with st.container():
    left, center, right = st.columns((3,1,3))
    with center:
        #mulai = st.button("Mulai Sekarang!",
        #help="Klik untuk mulai")
        mt = Elements()
        mulai = mt.button(
            "Mulai Sekarang!", 
            target="_blank", 
            size="small", 
            variant="outlined",     
            onclick="none", 
            style={"color":"#000000", "background":"#ffffff"}, 
            href="home",
            help="Klik untuk mulai")

        mt.show(key = "118")

            
        
with st.container():
    left, right = st.columns((1,2))
    with left:
        st_lottie(lottie_coding2,height=300, key = "search")
    with right:
        st.write("""
        ## Know Your Talent! \n
        InfluCheck membantu kamu untuk mengetahui profil dan persona dari calon talent kamu, data yang kami tampilkan berdasarkan Instagram secara real time hanya dengan memasukkan username Instagram calon talent kamu.
        """)    