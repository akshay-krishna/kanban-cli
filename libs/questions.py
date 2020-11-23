import inquirer
from libs.register import register
from libs.authenticate import authenticate

def read_option():
    while True:
        option = inquirer.prompt([inquirer.List('choice', message="Choose an option", choices=["Login", "Signup"])])
        if option['choice'] == 'Login':
            auth = authenticate(read_creds()) 
            if auth:
                return auth
        else:
            registerd = register(read_creds(True))
            if registerd:
                return registerd

def read_creds(auth = False):
    questions = [
        inquirer.Text('u_name', message="Please enter your user name"),
        inquirer.Password('password', message='Please enter your password'),
    ]
    
    if(auth):
        questions.insert(0, inquirer.Text('name', message="Please enter your name"),)

    return inquirer.prompt(questions)
