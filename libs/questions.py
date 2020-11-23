import inquirer
from libs.register import register
from libs.authenticate import authenticate


# This function is called first
# authenticate or register the user
def greet():
    while True:
        option = inquirer.prompt([inquirer.List('choice', message="Choose an option", choices=["Login", "Signup"])])
        if option['choice'] == 'Login':
            user = authenticate(read_creds()) 
            if user:
                return user
        else:
            user = register(read_creds(True))
            if user:
                return user


# helper function for greet
# read the user credentials
def read_creds(auth = False):
    questions = [
        inquirer.Text('u_name', message="Please enter your user name"),
        inquirer.Password('password', message='Please enter your password'),
    ]
    
    if(auth):
        questions.insert(0, inquirer.Text('name', message="Please enter your name"),)

    return inquirer.prompt(questions)

