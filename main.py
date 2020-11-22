import inquirer
from inquirer.themes import GreenPassion
from models.userModel import UserModel  

if __name__ == '__main__':

    questions = [
        inquirer.Text('name', message="Please enter your name"),
        inquirer.Text('u_name', message="Please enter your user name"),
        inquirer.Password('password', message='Please enter your password'),
        ]

    answers = inquirer.prompt(questions, theme=GreenPassion())

    user = UserModel(answers)
    print(user)
