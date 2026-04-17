import streamlit as st 
import requests


st.header('API call')

# url='http://127.0.0.1:8000/name'


# url='http://13.127.253.83:8000/name'
# if st.button("GetApi call"):
#     response= requests.get(url)
#     st.write(response.json())
    
url='http://13.127.253.83:8000/getname'
# url='http://127.0.0.1:8000/getname'
name= st.text_input('Name')
if st.button("Submit"):
    st.write(name)
    response= requests.post(url,json={'name':name})

    st.write(response)
    st.write(response.json())

    