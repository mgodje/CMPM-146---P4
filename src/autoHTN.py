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
		arr = []
		for item in rule["Requires"]:
			enough = ('have_enough', ID, item[0], item[1])
			arr.append(enough)
		for item in rule["Consumes"]:
			enough = ('have_enough', ID, item[0], item[1])
			arr.append(enough)

		arr.append(name, ID)
		return arr
	
	return method

def declare_methods (data):
	# some recipes are faster than others for the same product even though they might require extra tools
	# sort the recipes so that faster recipes go first

	# your code here
	# hint: call make_method, then declare the method to pyhop using pyhop.declare_methods('foo', m1, m2, ..., mk)	
	def punch_for_wood (state, ID):
		return make_method('op_punch_for_wood', data["Recipes"]["punch for wood"])
	
	def craft_wooden_axe_at_bench (state, ID):
		return make_method('op_craft_wooden_axe_at_bench', data["Recipes"]["craft wooden_axe at bench"])
	
	def iron_axe_for_wood (state, ID):
		return make_method('op_iron_axe_for_wood', data["Recipes"]["iron_axe for wood"])
	
	def craft_wooden_pickaxe_at_bench (state, ID):
		return make_method('op_craft_wooden_pickaxe_at_bench', data["Recipes"]["craft wooden_pickaxe at bench"])
	
	def craft_stone_pickaxe_at_bench (state, ID):
		return make_method('op_craft_stone_pickaxe_at_bench', data["Recipes"]["craft stone_pickaxe at bench"])
	
	def wooden_pickaxe_for_coal (state, ID):
		return make_method('op_wooden_pickaxe_for_coal', data["Recipes"]["wooden_pickaxe for coal"])
	
	def iron_pickaxe_for_ore (state, ID):
		return make_method('op_iron_pickaxe_for_ore', data["Recipes"]["iron_pickaxe for ore"])
	
	def wooden_axe_for_wood (state, ID):
		return make_method('op_wooden_axe_for_wood', data["Recipes"]["wooden_axe for wood"])
	
	def craft_plank (state, ID):
		return make_method('op_craft_plank', data["Recipes"]["craft plank"])
	
	def craft_stick (state, ID):
		return make_method('op_craft_stick', data["Recipes"]["craft stick"])
	
	def craft_rail_at_bench (state, ID):
		return make_method('op_craft_rail_at_bench', data["Recipes"]["craft rail at bench"])
	
	def craft_cart_at_bench (state, ID):
		return make_method('op_craft_cart_at_bench', data["Recipes"]["craft cart at bench"])
	
	def iron_pickaxe_for_cobble (state, ID):
		return make_method('op_iron_pickaxe_for_cobble', data["Recipes"]["iron_pickaxe for cobble"])
	
	def stone_axe_for_wood (state, ID):
		return make_method('op_stone_axe_for_wood', data["Recipes"]["stone_axe for wood"])
	
	def craft_iron_pickaxe_at_bench (state, ID):
		return make_method('op_craft_iron_pickaxe_at_bench', data["Recipes"]["craft iron_pickaxe at bench"])
	
	def craft_furnace_at_bench (state, ID):
		return make_method('op_craft_furnace_at_bench', data["Recipes"]["craft furnace at bench"])
	
	def stone_pickaxe_for_ore (state, ID):
		return make_method('op_stone_pickaxe_for_ore', data["Recipes"]["stone_pickaxe for ore"])
	
	def craft_iron_axe_at_bench (state, ID):
		return make_method('op_craft_iron_axe_at_bench', data["Recipes"]["craft iron_axe at bench"])
	
	def stone_pickaxe_for_coal (state, ID):
		return make_method('op_stone_pickaxe_for_coal', data["Recipes"]["stone_pickaxe for coal"])
	
	def stone_pickaxe_for_cobble (state, ID):
		return make_method('op_stone_pickaxe_for_cobble', data["Recipes"]["stone_pickaxe for cobble"])
	
	def wooden_pickaxe_for_cobble (state, ID):
		return make_method('op_wooden_pickaxe_for_cobble', data["Recipes"]["wooden_pickaxe for cobble"])
	
	def iron_pickaxe_for_coal (state, ID):
		return make_method('op_iron_pickaxe_for_coal', data["Recipes"]["iron_pickaxe for coal"])
	
	def craft_bench (state, ID):
		return make_method('op_craft_bench', data["Recipes"]["craft bench"])
	
	def craft_stone_axe_at_bench (state, ID):
		return make_method('op_craft_stone_axe_at_bench', data["Recipes"]["craft stone_axe at bench"])
	
	def smelt_ore_in_furnace (state, ID):
		return make_method('op_smelt_ore_in_furnace', data["Recipes"]["smelt ore in furnace"])
	
	pyhop.declare_methods ('produce_wood', [punch_for_wood, wooden_axe_for_wood, stone_axe_for_wood, iron_axe_for_wood])
	pyhop.declare_methods ('produce_stick', craft_stick)
	pyhop.declare_methods ('produce_bench', craft_bench)
	pyhop.declare_methods ('produce_cobble', [iron_pickaxe_for_cobble, stone_pickaxe_for_cobble, wooden_pickaxe_for_cobble])
	pyhop.declare_methods ('produce_coal', [wooden_pickaxe_for_coal, iron_pickaxe_for_coal, stone_pickaxe_for_coal])
	pyhop.declare_methods ('produce_ore', [stone_pickaxe_for_ore, iron_pickaxe_for_ore])
	pyhop.declare_methods ('produce_ingot', smelt_ore_in_furnace)
	pyhop.declare_methods ('produce_wooden_axe', craft_wooden_axe_at_bench)
	pyhop.declare_methods ('produce_stone_axe', craft_stone_axe_at_bench)
	pyhop.declare_methods ('produce_iron_pickaxe', craft_iron_pickaxe_at_bench)
	pyhop.declare_methods ('produce_furnace', craft_furnace_at_bench)
	pyhop.declare_methods ('produce_stone_pickaxe', craft_stone_pickaxe_at_bench)
	pyhop.declare_methods ('produce_iron_axe', craft_iron_axe_at_bench)
	pyhop.declare_methods ('produce_wooden_pickaxe', craft_wooden_pickaxe_at_bench)
	pyhop.declare_methods ('produce_rail', craft_rail_at_bench)
	pyhop.declare_methods ('produce_cart', craft_cart_at_bench)
	pyhop.declare_methods ('produce_plank', craft_plank)	
	
def make_operator (rule):
	def operator (state, ID):
		# your code here
		if rule["Time"] < state.time[ID]:
			return False
		for item in rule["Requires"]:
			if getattr(state, item)[ID] < rule["Requires"].get(item):
				return False
		for item in rule["Consumes"]:
			if getattr(state, item)[ID] < rule["Consumes"].get(item):
				return False
			else:
				setattr(state, item, {ID: getattr(state, item)[ID] - rule["Consumes"].get(item)})
		for item in rule["Produces"]:
			setattr(state, item[ID], rule["Produces"].get(item))
		return state
	
	return operator

def declare_operators (data):
	# your code here
	# hint: call make_operator, then declare the operator to pyhop using pyhop.declare_operators(o1, o2, ..., ok)
	def op_punch_for_wood(state, ID):
		state = make_operator(data["Recipes"]["punch for wood"])
		return state
	
	def op_craft_wooden_axe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft wooden_axe at bench"])
		return state
	
	def op_iron_axe_for_wood(state, ID):
		state = make_operator(data["Recipes"]["iron_axe for wood"])
		return state
	
	def op_craft_wooden_pickaxe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft wooden_pickaxe at bench"])
		return state
	
	def op_craft_stone_pickaxe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft stone_pickaxe at bench"])
		return state
	
	def op_wooden_pickaxe_for_coal(state, ID):
		state = make_operator(data["Recipes"]["wooden_pickaxe for coal"])
		return state
	
	def op_iron_pickaxe_for_ore(state, ID):
		state = make_operator(data["Recipes"]["iron_pickaxe for ore"])
		return state
	
	def op_wooden_axe_for_wood(state, ID):
		state = make_operator(data["Recipes"]["wooden_axe for wood"])
		return state
	
	def op_craft_plank(state, ID):
		state = make_operator(data["Recipes"]["craft plank"])
		return state
	
	def op_craft_stick(state, ID):
		state = make_operator(data["Recipes"]["craft stick"])
		return state
	
	def op_craft_rail_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft rail at bench"])
		return state
	
	def op_craft_cart_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft cart at bench"])
		return state
	
	def op_iron_pickaxe_for_cobble(state, ID):
		state = make_operator(data["Recipes"]["iron_pickaxe for cobble"])
		return state
	
	def op_stone_axe_for_wood(state, ID):
		state = make_operator(data["Recipes"]["stone_axe for wood"])
		return state
	
	def op_craft_iron_pickaxe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft iron_pickaxe at bench"])
		return state
	
	def op_craft_furnace_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft furnace at bench"])
		return state
	
	def op_stone_pickaxe_for_ore(state, ID):
		state = make_operator(data["Recipes"]["stone_pickaxe for ore"])
		return state
	
	def op_craft_iron_axe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft iron_axe at bench"])
		return state
	
	def op_stone_pickaxe_for_coal(state, ID):
		state = make_operator(data["Recipes"]["stone_pickaxe for coal"])
		return state
	
	def op_stone_pickaxe_for_cobble(state, ID):
		state = make_operator(data["Recipes"]["stone_pickaxe for cobble"])
		return state
	
	def op_wooden_pickaxe_for_cobble(state, ID):
		state = make_operator(data["Recipes"]["wooden_pickaxe for cobble"])
		return state
	
	def op_iron_pickaxe_for_coal(state, ID):
		state = make_operator(data["Recipes"]["iron_pickaxe for coal"])
		return state
	
	def op_craft_bench(state, ID):
		state = make_operator(data["Recipes"]["craft bench"])
		return state
	
	def op_craft_stone_axe_at_bench(state, ID):
		state = make_operator(data["Recipes"]["craft stone_axe at bench"])
		return state
	
	def op_smelt_ore_in_furnace(state, ID):
		state = make_operator(data["Recipes"]["smelt ore in furnace"])
		return state

	pyhop.declare_operators (op_punch_for_wood, op_craft_wooden_axe_at_bench, op_iron_axe_for_wood, op_craft_wooden_pickaxe_at_bench, 
						 op_craft_stone_pickaxe_at_bench, op_wooden_pickaxe_for_coal, op_iron_pickaxe_for_ore, op_wooden_axe_for_wood, 
						 op_craft_plank, op_craft_stick, op_craft_rail_at_bench, op_craft_cart_at_bench, op_iron_pickaxe_for_cobble,
						 op_stone_axe_for_wood, op_craft_iron_pickaxe_at_bench, op_craft_furnace_at_bench, op_stone_pickaxe_for_ore, 
						 op_craft_iron_axe_at_bench, op_stone_pickaxe_for_coal, op_stone_pickaxe_for_cobble, op_wooden_pickaxe_for_cobble, 
						 op_iron_pickaxe_for_coal, op_craft_bench, op_craft_stone_axe_at_bench, op_smelt_ore_in_furnace)
	
	pass

def add_heuristic (data, ID):
	# prune search branch if heuristic() returns True
	# do not change parameters to heuristic(), but can add more heuristic functions with the same parameters: 
	# e.g. def heuristic2(...); pyhop.add_check(heuristic2)
	def heuristic (state, curr_task, tasks, plan, depth, calling_stack):
		# your code here

		# use the data to get the recipes and the tools
		# use the ID to get the agent's ID

		# state = current state
		# curr_task = current task
		# use tasks to get the tasks that are left
		# plan = current plan
		# use the depth to get the current depth of the search tree
		# calling_stack is to get the current task and the tasks that are left

		# if the current task is complete, return true
		# if the current task is not complete, check if the task can be completed
		# if the task can be completed, return true
		# else return false

		for task in tasks:
			if task[0] == curr_task:
				return False
			if curr_task == 'produce_furnace':
				if getattr(state,'furnace')[ID] >= 1: return True
			if curr_task == 'produce_bench':
				if getattr(state,'bench')[ID] >= 1: return True
			if curr_task == 'produce_iron_pickaxe':
				if getattr(state,'iron_pickaxe')[ID] >= 1: return True
			if curr_task == 'produce_iron_axe':
				if getattr(state,'iron_axe')[ID] >= 1: return True
			if curr_task == 'produce_stone_pickaxe':
				if getattr(state,'stone_pickaxe')[ID] >= 1: return True
			if curr_task == 'produce_stone_axe':
				if getattr(state,'stone_axe')[ID] >= 1: return True
			if curr_task == 'produce_wooden_pickaxe':
				if getattr(state,'wooden_pickaxe')[ID] >= 1: return True
			if curr_task == 'produce_wooden_axe':
				if getattr(state,'wooden_axe')[ID] >= 1: return True
			if curr_task == 'produce_cart':
				if getattr(state,'cart')[ID] >= 1: return True
			if curr_task == 'produce_rail':
				if getattr(state,'rail')[ID] >= 20: return True

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

	declare_operators(data)
	declare_methods(data)
	add_heuristic(data, 'agent')

	# pyhop.print_operators()
	# pyhop.print_methods()

	# Hint: verbose output can take a long time even if the solution is correct; 
	# try verbose=1 if it is taking too long
	pyhop.pyhop(state, goals, verbose=3)
	# pyhop.pyhop(state, [('have_enough', 'agent', 'cart', 1),('have_enough', 'agent', 'rail', 20)], verbose=3)