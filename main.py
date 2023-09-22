from termcolor import colored
from registeration import registerFun
from login import loginFun
from helpers import ask_for_num
from loginMenu import goToSecMenu

def mainMenu():
    print("Welcome to Crowd-Funding APP")
    while True:
        print(colored(" --- To Register press 1 --- ", "yellow"))
        print(colored(" --- To Login press 2 ---", "yellow"))
        print(colored(" --- To Exit press 0 --- ", "red"))
        choice = ask_for_num("Enter your choice: ")
        if(choice==1):
            registerFun()
            
         
        elif(choice==2):
            loginFun()
            goToSecMenu()
            
            
            
        elif(choice==0):
            print(colored("See you later ","cyan"))
            break
        

        else:
            print(colored(" Please Enter 1 or 2 ","blue"))   


mainMenu()

        

