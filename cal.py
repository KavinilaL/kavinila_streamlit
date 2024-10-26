import streamlit as st 
st.title("calculation")
st.write('''
         1.addition
         2.subraction
         3.multiplication
         4.division''')
choice = st.number_input("Enter your choice:",value = 0)
num_1 = st.number_input("Enter first number:",value = 0)
num_2 = st.number_input("Enter second number",value = 0)
if st.button("click here"):
    if choice==1:
        st.write(num_1 + num_2)
    elif choice==2:
        st.write(num_1 - num_2)
    elif choice==3:
        st.write(num_1 * num_2)
    else:
        st.write(num_1 / num_2)