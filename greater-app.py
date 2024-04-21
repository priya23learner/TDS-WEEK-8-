import streamlit as st

def calc(a,b,c):
  if a > b:
    if a > c:
      return a
    else:
      return c
  else:
    if b > c:
      return b
    else:
      return c
    
st.title("Find Largest")
a = st.number_input('Insert 1st number: ')
b = st.number_input('Insert 2nd number: ')
c = st.number_input('Insert 3rd number: ')
# op = st.text_input('Insert operation (+ or - or * or / ): ')

value = calc(a,b,c)  
st.write(value)
