import streamlit as st
st.title("Image viewer")
upload_image = st.file_uploader("Choose your image",type=("png","jpg","jpeg"))
if upload_image:
    st.image(upload_image)