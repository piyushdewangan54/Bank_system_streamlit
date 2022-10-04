from Bank_class import Bank
import streamlit as st
import json

with open('json_data.json') as json_file:
    d = json.loads(json.load(json_file))

    st.title("Bank of Khargarh")
    b = Bank(d)
    genre = st.radio(
        "Choose any service from below -",
        ('Create account', 'Withdraw Cash', 'Deposit Cash', 'Balance check'))

    if genre=='Create account':
      name = st.text_input("Enter your name : ")
      gender = st.selectbox(
        'Select your Gender : ',
        ('Male', 'Female'))
      phone = st.text_input("Enter your mobile number : ")
      if phone.isdigit():
        phone = int(phone)
      password = st.text_input("Enter new password : ", type="password")
      balance = st.text_input("Deposit money to open account : ")
      if balance.isdigit():
        balance = int(balance)
      if st.button("Submit"):
        b.create_account(name,gender,phone,password,balance)
    elif genre=='Withdraw Cash':
      acc = st.text_input("Enter account number : ")
      if acc.isdigit():
        acc=int(acc)
      pss = st.text_input("Enter password : ", type="password")
      if pss.isdigit():
        pss = int(pss)
      amt = st.text_input("Enter Amount you want to withdraw : ")
      if amt.isdigit():
        amt=int(amt)
      if st.button("Submit"):
        b.withdraw_cash(acc,pss,amt)
    elif genre=='Deposit Cash':
      acc = st.text_input("Enter account number : ")
      if acc.isdigit():
        acc = int(acc)
      pss = st.text_input("Enter password : ", type="password")
      if pss.isdigit():
        pss = int(pss)
      amt = st.text_input("Enter cash amount to deposit : ")
      if amt.isdigit():
        amt = int(amt)
      if st.button("Submit"):
        b.deposit_cash(acc,pss,amt)
    elif genre=='Balance check':
      acc = st.text_input("Enter account number : ")
      if acc.isdigit():
        acc = int(acc)
      pss = st.text_input("Enter password : ", type="password")
      if pss.isdigit():
        pss = int(pss)
      if st.button("Submit"):
        b.check_balance(acc,pss)


footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
height: 25px;
width: 100%;
background-color: black;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Made with  ❤  by Piyush Dewangan</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
