from helpers import ask_for_num, ask_for_str, validate_email, is_email_exist
import re
import uuid
import time
from filesOperations import *
from getpass import getpass
from termcolor import colored

def registerFun():
   print(colored("You Want to Join us ? We're so grateful ", "green"))

   fname = ask_for_str("Please Enter Your First Name : ")
   lname = ask_for_str("Please Enter Your Last Name : ")

   while True:
      email = validate_email()
      if is_email_exist(email):
         print(colored("This Email is already in use", "red"))
         continue
      else:
         password = validate_pass()
         confirmed_password = confirm_pass(password)
         phone_num = validate_phone_number()
         id = uuid.uuid4()    # Generate a UUID
         time_id = round(time.time())

         user_info = f"{id}:{fname}:{lname}:{email}:{password}:{phone_num}:{time_id}\n"

         if save_user_data(user_info):
            print(colored("Registration Successful ", "green"))
         else:
            print(colored("Error occurred while registering. Please Try Again later.", "red"))
         
         break


def validate_pass():
    while True:
        password = getpass(colored("Please Enter your Password  : ","yellow"))
        if len(password) >= 8:
            return password
        else:
            print(colored("Your Password has to contain at least 8 Characters Please Try Again ", "red"))


def confirm_pass(password_to_confirm):
    while True:
        password = getpass(colored("Please Enter your Password Again : ","yellow"))
        if password_to_confirm == password:
            return password
        else:
            print(colored("The Password Confirmation doesn't match  Please Try Again ", "red"))


def validate_phone_number():
    while True:
        number = input(colored("Please Enter Your Phone Number: ", "yellow"))

        if len(number) == 13 and number.startswith("+20"):
            return number
        else:
            print(colored("The phone number must start with +20 and be 13 digits in length.", "red"))
