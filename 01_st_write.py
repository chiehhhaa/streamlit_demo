import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")

st.caption(":gray[用於標注]")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")