import streamlit as st

import streamlit_authenticator as stauth
from koneksi_db.koneksi_login import get_data
import requests
from streamlit_lottie import st_lottie

for item in get_data():
    names = item['names']
    username = item['username']
    passwords = item['password']

hashed_passwords = stauth.hasher(passwords).generate()

st.set_page_config(page_title = "Bismillah Lancar", page_icon=":tada", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_q5pk6p1k.json")

with st.container():
    st.title("InfluCheck")
    
with st.container():
    left_column, empty2_column, right_column = st.columns((2,0.5,3))
    with left_column:
        st_lottie(lottie_coding, height= 400, key= "login")
    with right_column:
        authenticator = stauth.authenticate(names, username, hashed_passwords, 'cookies', '1234', cookie_expiry_days=2)
        names, authentication_status = authenticator.login('Masuk!', 'main')
        if st.session_state['authentication_status']:
            st.write('Welcome *%s*' % (st.session_state['name']))
            st.title('Some content')
        elif st.session_state['authentication_status'] == False:
            st.error('Username/password is incorrect')
        elif st.session_state['authentication_status'] == None:
            st.warning('Masukkan username dan password kamu')

