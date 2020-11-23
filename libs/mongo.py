import pymongo
from bson.objectid import ObjectId
from tabulate import tabulate
from itertools import zip_longest
def connect():
	client = pymongo.MongoClient()
	db = client.kanban
	return db.charts


def gen_chart():
	charts = connect()
	data = {
		'task': [],
		'doing': [],
		'done': []
	}

	return charts.insert_one(data).inserted_id

def add_task(command, chart_id):
	charts = connect()
	chart = charts.find_one({'_id': ObjectId(chart_id)})
	(_, command_arg) = parse_command(command)
	chart['task'].append(command_arg)
	charts.find_one_and_update({'_id': ObjectId(chart_id)}, {"$set": chart})


def list_chart(chart_id):
	charts = connect()
	table = [['task', 'doing', 'done']]
	chart = charts.find_one({'_id': ObjectId(chart_id)})
	for (a, b, c) in zip_longest(chart['task'], chart['doing'], chart['done']):
		table.append([a, b,c])
	print(tabulate(table))


def move_task(command, chart_id):
	charts = connect()
	(command_name, command_arg) = parse_command(command)
	chart = charts.find_one({'_id': ObjectId(chart_id)})
	option = 'task' if command_name == 'doing' else "doing"
	try:
		chart[option].remove(command_arg)
	except ValueError as e:
		print("No such task")
		return
	chart[command_name].append(command_arg)
	charts.find_one_and_update({'_id': ObjectId(chart_id)}, {"$set": chart})

def clear_tasks(chart_id):
	charts = connect()
	data = { 
		'task': [],
		'doing': [],
		'done': []
	}
	charts.find_one_and_update({'_id': ObjectId(chart_id)}, {"$set": data})


def parse_command(command):
	return (command[:command.index(' ')], command[command.index(' ')+1:])