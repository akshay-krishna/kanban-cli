from sys import exit
from libs.mongo import add_task, list_chart, move_task, clear_tasks

def handler(command, chart_id):
	command = command.lower()
	if command == 'exit':
		exit(0)

	elif command == 'show':
		list_chart(chart_id)

	elif command == 'clear':
		clear_tasks(chart_id)

	elif command == "logout":
		return False

	elif 'doing' in command or 'done' in command:
		move_task(command, chart_id)

	elif 'add' in command:
		add_task(command, chart_id)
	elif 'help' in command:
		print(
			"""
			exit- exit the terminal
			show- show all the tasks
			clear- clear all the tasks
			logout- logout
			doing taks_name- move the task to the doing column
			done tasks_name- move the task from doing to done column
			add task_name- create a new task
			help- show this manual
			"""
			)
	else:
		print("Enter an valid input")

	return True