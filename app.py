import streamlit as st
st.title("Loan Approval Agent")

Approver=st.text_input("Enter Loan Approval Agent :")
Customer_name=st.text_input("Enter customer Name :")
Loan_amount=st.number_input("Enter Loan amount :")
Credit_score=st.number_input("Enter credit score :")

if st.button("Submit"):
  st.write(f""")  

  Customer Loan Approval Summary

  ------------------------------
  Approver \t: {Approver}
  Customer Name \t: {Customer_name}
  Loan Amount \t: {Loan_amount}
  Credit Score \t: {Credit_score}
  ------------------------------
