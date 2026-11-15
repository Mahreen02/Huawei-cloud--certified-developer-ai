import streamlit as st


st.title("UI for Biginners")

input = st.number_input(
    "Enter the number in int or float",
    min_value = 0,
    max_value = 1000,
    value = 1,
    step = 2
)
if st.button("Square"):
    output = input **2
    st.success(f"The square of the input is{output}")
    
 if st.button("Addition"):
     output = input + input
     st.success(f"The square of the input is{output}")  
     
     
     
     import opencv as cv2