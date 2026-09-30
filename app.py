import streamlit as st


st.title("Calculator APP")

num1 = st.number_input("Enter your first number")

num2 = st.number_input("Enter your second number")

operation = st.selectbox("Select your operation",("Addition","Subtraction","Multiplication","Division"))


if st.button("Calculate"):
    if operation=="Addition":
        st.write(num1+num2)
    elif operation=="Subtraction":
        st.write(num1-num2)
    elif operation=="Multiplication":
        st.write(num1*num2)
    else:
        st.write(num1/num2)