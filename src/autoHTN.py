import pyhop
import json

def check_enough (state, ID, item, num):
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

pyhop.declare_methods ('have_enough', check_enough, produce_enough)

def produce (state, ID, item):
	return [('produce_{}'.format(item), ID)]

pyhop.declare_methods ('produce', produce)

def make_method (name, rule):
	def method (state, ID):
		# your code here
		#
		#print(rule[1]['Requires'])
		arr = []
		
		#print(type(rule))
		#print("rule: ")
		#print(rule[1])
		if "Requires" in rule[1]:
			for key, amount in rule[1]['Requires'].items():
				#print("key: " + key)
				enough = ('have_enough', ID, key, amount)
				arr.append(enough)
		
		if "Consumes" in rule[1]:
			for key, amount in rule[1]['Consumes'].items():
				enough = ('have_enough', ID, key, amount)
				arr.append(enough)
		
		arr.append((name, ID))
		return arr
	
	return method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)	
	for item in data['Items']:
		methods = []
		task = "produce_" + item
		#print("item: " + item)
		for rule in data['Recipes'].items():
			if item == list(rule[1]['Produces'])[0]:
				#print("true!!")
				name = "op_" + rule[0].replace(" ", "_")
				method = make_method(name, rule)
				method.__name__ = rule[0].replace(" ", "_")
				#print("method name: " + method.__name__)
				methods.append(method) 
		#print("name: " + task)
		pyhop.declare_methods(task, *methods) 
	
	for item in data['Tools']:
		methods = []
		task = "produce_" + item
		#print("item: " + item)
		for rule in data['Recipes'].items():
			if item == list(rule[1]['Produces'])[0]:
				#print("true!!")
				name = "op_" + rule[0].replace(" ", "_")
				method = make_method(name, rule)
				method.__name__ = rule[0].replace(" ", "_")
				#print("method name: " + method.__name__)
				methods.append(method) 
		#print("name: " + task)
		pyhop.declare_methods(task, *methods) 
	

	"""
	print("========methods=======")
	pyhop.print_methods()"""


def make_operator (rule):
	def operator (state, ID):
		# your code here
		#print(rule[0])
		#print("state: ")
		print("rule: ")
		print(rule)
		if rule['Time'] > state.time[ID]:
			#print(rule[1]['Time'])
			return False
		if "Requires" in rule:
			for item, amount in rule['Requires'].items():
				#print("item: " + item)
				#print("getattr(state, item)[ID]" + getattr(state, item)[ID])
				if getattr(state, item)[ID] < amount:
					return False
		
		if "Consumes" in rule:
			for item, amount in rule['Consumes'].items():
				if getattr(state, item)[ID] < amount:
					return False
				else:
					setattr(state, item, {ID: getattr(state, item)[ID] - rule['Consumes'].get(item)})
		
		if "Produces" in rule:
			print("rule[1]['Produces']: ")
			print(rule['Produces'])
			for item, amount in rule['Produces'].items():
				new_value = getattr(state, item)[ID] + amount
				#print("item, amount: " + item + amount)
				state.time[ID] = state.time[ID] - rule['Time']
				setattr(state, item, {ID:new_value})
		
		#print("state: " + state)
		return state
	
	return operator

def declare_operators (data):
	# your code here
	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	
	for rule in data['Recipes'].items():
		#print(rule)
		operator = make_operator(rule[1])
		operator.__name__ = "op_" + rule[0].replace(" ", "_")
		#print(operator)
		pyhop.declare_operators(operator)
	
	
def add_heuristic (data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters: 
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic (state, curr_task, tasks, plan, depth, calling_stack):
		# your code here

		# use the data to get the recipes and the tools
		# use the ID to get the agent's ID

		#state: the current problem state
		#curr_task: the task addressed by every method in methods
		#tasks: the list of tasks that follow curr_task in its sequential task list
		#plan: the currently accrued plan of operations
		#depth: the depth of curr_task in pyhop’s search tree
		#calling-stack: the list of subtasks connecting the overall task to curr_task

		# if the current task is complete, return true
		# if the current task is not complete, check if the task can be completed
		# if the task can be completed, return true
		# else return false
		print("State: ")
		pyhop.print_state(state)
		
		if depth > 10:
			return True

		return False

	pyhop.add_check(heuristic)

def set_up_state (data, ID, time=0):
	state = pyhop.State('state')
	state.time = {ID: time}

	for item in data['Items']:
		setattr(state, item, {ID: 0})

	for item in data['Tools']:
		setattr(state, item, {ID: 0})

	for item, num in data['Initial'].items():
		setattr(state, item, {ID: num})

	return state

def set_up_goals (data, ID):
	goals = []
	for item, num in data['Goal'].items():
		goals.append(('have_enough', ID, item, num))

	return goals

if __name__ == '__main__':
	rules_filename = 'crafting.json'

	with open(rules_filename) as f:
		data = json.load(f)

	state = set_up_state(data, 'agent', time=239) # allot time here
	goals = set_up_goals(data, 'agent')
	"""print("state: ")
	pyhop.print_state(state)
	print(state.cart)"""

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')

	# pyhop.print_operators()
	# pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct; 
	# try verbose=1 if it is taking too long
	pyhop.pyhop(state, goals, verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)

