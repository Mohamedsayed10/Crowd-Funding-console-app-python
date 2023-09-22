from termcolor import colored
def save_user_data(userInfo):
    try:
        fileobj=open('users.txt','a')
    except Exception as e:
        print('Error: Unable to open file ')
        return False
    else:
        fileobj.write(userInfo)
        return True  
    finally:
        fileobj.close()  

def save_logged_user(logged_user):
    try:
        fileobj=open('logs.txt','w')
    except Exception as e:
        print('Error: Unable to open file ')
        return False
    else:
        fileobj.write(logged_user)
        return True  
    finally:
        fileobj.close()          

def save_project(proj_info):
    try:
        projFile = open('projects.txt', 'a')
    except Exception as e:
        print(colored('Error: Unable to open file ', 'red'))
        return False
    else:
        projFile.write(proj_info)
        print(colored("New Project has been added Successfully ", 'green'))
        return True  
    finally:
        projFile.close()
