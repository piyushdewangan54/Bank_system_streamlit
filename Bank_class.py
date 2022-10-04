import streamlit as st
import json

class Bank:

    def __init__(self, d):
        st.subheader("Welcome to Bank of Khargarh!")
        self.d = d

    def create_account(self,name,gender,phone,password,balance):
      self.name = name
      self.gender = gender
      self.__phone = phone
      self.__password = password
      self.__balance = balance
      if self.__balance >= 1000:
        self.acn = int(list(self.d)[-1]) + 1
        st.markdown(f"\nHi, {self.name}! Your new account is created with Account number : {self.acn}")
        self.d[self.acn] = [self.__password, self.__balance, self.name]
        json_string = json.dumps(self.d)
        with open('json_data.json', 'w') as outfile:
          json.dump(json_string, outfile)
      else:
        st.markdown("Deposit minimum amount of Rs.1000 !!!")

    def withdraw_cash(self, acn, passwd, cash):
      self.cash = cash
      if self.d[f'{acn}'][0] == str(passwd):
          if self.d[f'{acn}'][1] - self.cash >= 1000:
            self.d[f'{acn}'][1] -= self.cash
            json_string = json.dumps(self.d)
            with open('json_data.json', 'w') as outfile:
                json.dump(json_string, outfile)
            st.markdown(f"\nYou have Withdrawn amount of Rs.{self.cash}")
          else:
            st.markdown("YOU SHOULD MAINTAIN MINIMUN BALANCE of Rs.1000/-")

      else:
        st.markdown("Enter correct account number and password !")

    def deposit_cash(self, acn, passwd, money):
      self.money=money
      if self.d[f'{acn}'][0] == str(passwd):
          if self.money > 0 :
            self.d[f'{acn}'][1] += self.money
            json_string = json.dumps(self.d)
            with open('json_data.json', 'w') as outfile:
                json.dump(json_string, outfile)
            st.markdown(f"\nYou have deposited an amount of Rs.{self.money}")
          else:
            st.markdown("ENTER POSITIVE AMOUNT !!!")

      else:
        st.markdown("Enter correct account number and password !")

    def check_balance(self, acn, passwd):
      if self.d[f'{acn}'][0] == str(passwd):
        st.markdown(f"Hi {self.d[f'{acn}'][2]}, Your current balance is Rs.{self.d[f'{acn}'][1]}")
      else:
        st.markdown("Enter correct account number and password !")
