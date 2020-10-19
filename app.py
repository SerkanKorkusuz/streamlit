import streamlit as st


x_start = st.sidebar.slider('Start for X', value=125, key='sx')
y_start = st.sidebar.slider('Start for Y', value=332, key='sy')
x_finish = st.sidebar.slider('Target for  X', value=309, key='fx')
y_finish = st.sidebar.slider('Target for  Y', value=330, key='fy')

uploaded_file = st.file_uploader('Choose a file', ['jpg', 'jpeg', 'png', 'doc', 'ppt', 'xls', 'csv', 'xlsx', 'xml', 'py', 'txt'])
st.write('But')
no_upload = st.checkbox('I want to upload no file!')
