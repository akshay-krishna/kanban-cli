from  libs.questions import *
from libs.commandhandler import handler
if __name__ == '__main__':
	chart_id = greet()

	print("Write a command")
	auth = True
	while auth:
		command = input(">")
		auth = handler(command.lower(), chart_id)
