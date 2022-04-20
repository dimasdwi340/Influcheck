import streamlit as st
from koneksi_db.koneksi_result import items

for item in items:
    username = item['username']
    url = item['url_profile_pict']
    post_count = item['post_count']
    follower = item['follower']
    biography = item['biography']
    category_name = item['category_name']
    fullname = ['full_name']
    persona = ['persona']

st.set_page_config(page_title="Hasil dong", page_icon=":tada", layout="wide")

if persona == "traveller":
    persona_acc = "Travel Blogger"
else:
    persona_acc = "Unknown"

with st.container():
    st.title("InfluCheck")

with st.container():
    left,center1, center2, right = st.columns((1,1,1,1))
    with left:
        st.image("asset/profile/amrazing.jpg", width=200)
    with center1:
        with st.container():
            st.write(f"""
            Username :\n
            ## {username}""")
            st.write(f"""
            ###### {category_name}""")
    with center2:
        st.write(f"""
        Post :
        ## {post_count}""")
    with right:
        st.write(f"""
        Followers :\n 
        ## {follower}""")

with st.container():
    left, center,right = st.columns((1,2,1))
    with center:
        st.write("""
        Author⁣ - Content creator⁣ - Storygrapher⁣ \n
        #LetMeTellYouAStory about how I see the world 😗
        """)

with st.container():
    st.write(f"""#### Talent kamu adalah seorang Travel Blogger, dengan jumlah followers sebanyak {follower} dan sudah membagikan sejumlah {post_count} postingan. Talent kamu termasuk "Macro Influencers" yang cenderung memiliki audiens yang beragam dengan minat yang beragam.""")

with st.container():
    st.sidebar.write("""#### Profil Kamu""")