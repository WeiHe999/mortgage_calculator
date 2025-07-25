import streamlit as st

st.title("Mortgage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)
home_value = col1.number_input("Home Value", min_value = 0, max_value = 500000)
deposit = col1.number_input("Deposit", min_value = 0, max_value = 100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value = 0.0, max_value = 5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value = 1, max_value = 30)

loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1))
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)
col1.metric(label = "Monthly Repayments", value = f"${monthly_payment}")
col2.metric(label = "Total Repayments", value = f"${total_payments}")
col3.metric(label = "Total Interest", value = f"${total_interest}")
