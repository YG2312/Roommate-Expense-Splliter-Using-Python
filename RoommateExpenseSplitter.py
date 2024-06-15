import streamlit as st
from PIL import Image
image = Image.open("C:/Users/ACER/Downloads/abscd.png")
st.title("Roommate Expense Splitter :)")
st.image(image)
rent = st.number_input('Enter rent per month:')
food = st.number_input('Enter money spent on food per month:')
electricity=st.number_input('Enter electricity bill of month:')
person=st.number_input('Total number of persons/roomate:')
if st.button('Submit'):
    Priceperperson=(rent+food+electricity)//person
    st.write('Priceperperson', Priceperperson)