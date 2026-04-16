import streamlit as st 
import base64 

st.set_page_config(page_title="BG Img")

with open('img.jpg','rb') as file:
    image= file.read()
img =  base64.b64encode(image).decode()

css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image:url('data:image/png;base64,{img}');
        background-size:cover
    }}
    [data-testid="stBaseButton-secondaryFormSubmit"]{{
        background-color: orange;
        color:black
    }}
    [data-testid="stHeadingWithActionElements"]{{
        color:yellow;
    }}
    [data-testid="stSidebar"]{{
        background-color:orange
    }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# st.header("Registration Form")
# with st.form(key='forms'):
#     col1,col2=st.columns(2)
#     with col1:
#         name=st.text_input("First Name")
#         mail=st.text_input("Email",placeholder='Enter Email here...')
#         age=st.number_input("Age")
#     with col2:
#         lname=st.text_input("Last Name")
#         pwd=st.text_input('Password', placeholder='Enter password', type='password')
#         gender= st.radio(label="Gender", options=['Male','Female'],index=0,horizontal=True)
#     address= st.text_area("Address")
#     terms=st.checkbox('Terms and conditions')
#     state= st.selectbox("State",options=['Punjab','HP','Haryana','UP'], index=3)
#     hobbies= st.multiselect("Hobbies",options=['Reading','Watching Movies','Playing Cricket','Singing','Writing'])
#     btn= st.form_submit_button('Submit')
    
import pandas as pd 
import seaborn as sns 

df=sns.load_dataset('tips')

# st.dataframe(df)
# st.write(df)
# st.table(df)
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

st.plotly_chart(fig)