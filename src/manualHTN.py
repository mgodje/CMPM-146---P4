import pyhop

'''begin operators'''

def op_punch_for_wood (state, ID):
	if state.time[ID] >= 4:
		state.wood[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_craft_wooden_axe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >= 2:
		state.wooden_axe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

# your code here

def op_iron_axe_for_wood(state, ID):
	if state.time[ID] >= 1 and state.iron_axe[ID] >= 1:
		state.wood[ID] += 1
		state.time[ID] -=1
		return state
	return False

def op_craft_wooden_pickaxe_at_bench (state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >= 2:
		state.wooden_pickaxe[ID] += 1
		state.plank[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_stone_pickaxe_at_bench(state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >= 2:
		state.stone_pickaxe[ID] += 1
		state.cobble[ID] -= 3
		state.stick[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_wooden_pickaxe_for_coal(state, ID):
	if state.time[ID] >= 4 and state.wooden_pickaxe[ID] >= 1:
		state.coal[ID] += 1
		state.time[ID] -= 4
		return state
	return False

def op_iron_pickaxe_for_ore(state, ID):
	if state.time[ID] >= 2 and state.iron_pickaxe[ID] >= 1:
		state.ore[ID] += 1
		state.time[ID] -=2
		return state
	return False

def op_wooden_axe_for_wood(state, ID):
	if state.time[ID] >= 2 and state.wooden_axe[ID] >= 1:
		state.wood[ID] += 1
		state.time[ID] -= 2
		return state
	return False

def op_craft_plank(state, ID):
	if state.time[ID] >= 1 and state.wood[ID] >= 1:
		state.plank[ID] += 4
		state.wood[ID] -= 1
		state.time[ID] -= 1
		return state
	return False

def op_craft_stick(state, ID):
	if state.time[ID] >= 1 and state.plank[ID] >= 2:
		state.stick[ID] += 4
		state.plank[ID] -= 2
		state.time[ID] -= 1
		return state
	return False

def op_craft_rail_at_bench(state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 6 and state.stick[ID] >= 1:
		state.rail[ID] += 16
		state.stick[ID] -= 1
		state.ingot[ID] -= 6
		state.time[ID] -= 1
		return state
	return False

def op_craft_cart_at_bench(state, ID):
	if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 5:
		state.cart[ID] += 1
		state.ingot[ID] -= 5
		state.time[ID] -= 1
		return state
	return False

def op_iron_pickaxe_for_cobble(state, ID):
	if state.time[ID] >= 1 and state.iron_pickaxe[ID] >= 1:
		state.cobble[ID] += 1
		state.time[ID] -= 1
		return state
	return False
#
def op_stone_axe_for_wood (state, ID):
    if state.time[ID] >= 1:
        state.wood[ID] += 1
        state.time[ID] -= 1
        return state
    return False

def op_craft_iron_pickaxe_at_bench (state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.plank[ID] >= 3 and state.stick[ID] >=2:
        state.iron_pickaxe[ID] += 1
        state.plank[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_craft_furnace_at_bench (state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
        state.furnace[ID] += 1
        state.cobble[ID] -= 8
        state.time[ID] -= 1
        return state
    return False

def op_stone_pickaxe_for_ore (state, ID):
    if state.time[ID] >= 4:
        state.ore[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_craft_iron_axe_at_bench (state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.ingot[ID] >= 3 and state.stick[ID] >=2:
        state.iron_axe[ID] += 1
        state.ingot[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False

def op_stone_pickaxe_for_coal (state, ID):
    if state.time[ID] >= 2:
        state.coal[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_stone_pickaxe_for_cobble (state, ID):
    if state.time[ID] >= 2:
        state.cobble[ID] += 1
        state.time[ID] -= 2
        return state
    return False

def op_wooden_pickaxe_for_cobble (state, ID):
    if state.time[ID] >= 4:
        state.cobble[ID] += 1
        state.time[ID] -= 4
        return state
    return False

def op_iron_pickaxe_for_coal (state, ID):
    if state.time[ID] >= 1:
        state.coal[ID] += 1
        state.time[ID] -= 1
        return state
    return False

def op_craft_bench (state, ID):
    if state.time[ID] >= 1 and state.plank[ID] >= 4:
        state.bench[ID] += 1
        state.plank[ID] -= 4
        state.time[ID] -= 1
        return state
    return False

def op_craft_stone_axe_at_bench (state, ID):
    if state.time[ID] >= 1 and state.bench[ID] >= 1 and state.cobble[ID] >= 3 and state.stick[ID] >=2:
        state.stone_axe[ID] += 1
        state.cobble[ID] -= 3
        state.stick[ID] -= 2
        state.time[ID] -= 1
        return state
    return False
def op_smelt_ore_in_furnace (state, ID):
    if state.time[ID] >= 5 and state.furnace[ID] >= 1 and state.ore[ID] >= 1 and state.coal[ID] >= 1:
        state.ingot[ID] += 1
        state.ore[ID] -= 1
        state.coal[ID] -= 1
        state.time[ID] -= 5
        return state
    return False

pyhop.declare_operators (op_punch_for_wood, op_craft_wooden_axe_at_bench, op_iron_axe_for_wood, op_craft_wooden_pickaxe_at_bench, 
						 op_craft_stone_pickaxe_at_bench, op_wooden_pickaxe_for_coal, op_iron_pickaxe_for_ore, op_wooden_axe_for_wood, 
						 op_craft_plank, op_craft_stick, op_craft_rail_at_bench, op_craft_cart_at_bench, op_iron_pickaxe_for_cobble,
						 op_stone_axe_for_wood, op_craft_iron_pickaxe_at_bench, op_craft_furnace_at_bench, op_stone_pickaxe_for_ore, 
						 op_craft_iron_axe_at_bench, op_stone_pickaxe_for_coal, op_stone_pickaxe_for_cobble, op_wooden_pickaxe_for_cobble, 
						 op_iron_pickaxe_for_coal, op_craft_bench, op_craft_stone_axe_at_bench, op_smelt_ore_in_furnace)

'''end operators'''

def check_enough (state, ID, item, num):
	# methods either fail or return a list of subtasks,
	# so returning an empty list indicates success
	if getattr(state,item)[ID] >= num: return []
	return False

def produce_enough (state, ID, item, num):
	return [('produce', ID, item), ('have_enough', ID, item, num)]

def produce (state, ID, item):
	if item == 'wood': 
		return [('produce_wood', ID)]
	# your code here

	# for items
	elif item == 'cart': 
		return [('produce_cart', ID)]
	elif item == 'coal': 
		return [('produce_coal', ID)]
	elif item == 'cobble': 
		return [('produce_cobble', ID)]
	elif item == 'ingot': 
		return [('produce_ingot', ID)]	
	elif item == 'ore': 
		return [('produce_ore', ID)]
	elif item == 'plank': 
		return [('produce_plank', ID)]
	elif item == 'rail': 
		return [('produce_rail', ID)]	
	elif item == 'stick': 
		return [('produce_stick', ID)]
	
	# for tools
	elif item == 'wooden_axe':
		# this check to make sure we're not making multiple axes
		if state.made_wooden_axe[ID] is True:
			return False
		else:
			state.made_wooden_axe[ID] = True
		return [('produce_wooden_axe', ID)]
	elif item == 'iron_axe':
		if state.made_iron_axe[ID] is True:
			return False
		else:
			state.made_iron_axe[ID] = True
	elif item == 'wooden_pickaxe':
		if state.made_wooden_pickaxe[ID] is True:
			return False
		else:
			state.made_wooden_pickaxe[ID] = True
	elif item == 'stone_pickaxe':
		if state.made_stone_pickaxe[ID] is True:
			return False
		else:
			state.made_stone_pickaxe[ID] = True
	elif item == 'iron_axe':
		if state.made_iron_axe[ID] is True:
			return False
		else:
			state.made_iron_axe[ID] = True
	elif item == 'iron_pickaxe':
		if state.made_iron_pickaxe[ID] is True:
			return False
		else:
			state.made_iron_pickaxe[ID] = True
	elif item == 'furnace':
		if state.made_furnace[ID] is True:
			return False
		else:
			state.made_furnace[ID] = True
	elif item == 'bench':
		if state.made_bench[ID] is True:
			return False
		else:
			state.made_bench[ID] = True
	else:
		return False

pyhop.declare_methods ('have_enough', check_enough, produce_enough)
pyhop.declare_methods ('produce', produce)

'''begin recipe methods'''

def punch_for_wood (state, ID):
	return [('op_punch_for_wood', ID)]

def craft_wooden_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_axe_at_bench', ID)]

# your code here

def iron_axe_for_wood(state, ID):
    return [('have_enough', ID, 'iron_axe', 1), ('op_iron_axe_for_wood', ID)]

def craft_wooden_pickaxe_at_bench (state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'plank', 3), ('op_craft_wooden_pickaxe_at_bench', ID)]

def craft_stone_pickaxe_at_bench (state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_pickaxe_at_bench', ID)]

def wooden_pickaxe_for_coal (state, ID):
    return [('have_enough', ID, 'wooden_pickaxe', 1), ('op_wooden_pickaxe_for_coal', ID)]

def iron_pickaxe_for_coal (state, ID):
    return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_coal', ID)]

def wooden_axe_for_wood(state, ID):
    return [('have_enough', ID, 'wooden_axe', 1), ('op_wooden_axe_for_wood', ID)]

def craft_plank (state, ID):
    return [('have_enough', ID, 'wood', 1), ('op_craft_plank', ID)]

def craft_stick (state, ID):
    return [('have_enough', ID, 'plank', 1), ('op_craft_stick', ID)]

def craft_rail_at_bench (state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 6), ('have_enough', ID, 'stick', 1), ('op_craft_rail_at_bench', ID)]

def craft_cart_at_bench (state, ID):
    return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'ingot', 5), ('op_craft_cart_at_bench', ID)]

def iron_pickaxe_for_cobble (state, ID):
    return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_cobble', ID)]

def stone_axe_for_wood(state, ID):
    return [('have_enough', ID, 'stone_axe', 1), ('op_stone_axe_for_wood', ID)]

def craft_iron_pickaxe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_pickaxe_at_bench', ID)]

def craft_furnace_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'cobble', 8), ('op_craft_furnace_at_bench', ID)]

def stone_pickaxe_for_ore (state, ID):
	return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_ore', ID)]

def craft_iron_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'ingot', 3), ('op_craft_iron_axe_at_bench', ID)]

def stone_pickaxe_for_coal (state, ID):
	return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_coal', ID)]

def stone_pickaxe_for_cobble (state, ID):
	return [('have_enough', ID, 'stone_pickaxe', 1), ('op_stone_pickaxe_for_cobble', ID)]

def wooden_pickaxe_for_cobble (state, ID):
	return [('have_enough', ID, 'wooden_pickaxe', 1), ('op_wooden_pickaxe_for_cobble', ID)]

def iron_pickaxe_for_coal (state, ID):
	return [('have_enough', ID, 'iron_pickaxe', 1), ('op_iron_pickaxe_for_coal', ID)]

def craft_bench (state, ID):
	return [('have_enough', ID, 'plank', 4), ('op_craft_bench', ID)]

def craft_stone_axe_at_bench (state, ID):
	return [('have_enough', ID, 'bench', 1), ('have_enough', ID, 'stick', 2), ('have_enough', ID, 'cobble', 3), ('op_craft_stone_axe_at_bench', ID)]

def smelt_ore_in_furnace (state, ID):
	return [('have_enough', ID, 'furnace', 1), ('have_enough', ID, 'ore', 1), ('have_enough', ID, 'coal', 1), ('op_smelt_ore_in_furnace', ID)]

pyhop.declare_methods ('produce_wood', punch_for_wood) #wooden_axe_for_wood, stone_axe_for_wood, iron_axe_for_wood ?
pyhop.declare_methods ('produce_wooden_axe', craft_wooden_axe_at_bench)

# do we need these???

pyhop.declare_methods ('produce_stone_axe', craft_stone_axe_at_bench)
pyhop.declare_methods ('produce_iron_pickaxe', craft_iron_pickaxe_at_bench)
pyhop.declare_methods ('produce_furnace', craft_furnace_at_bench)
pyhop.declare_methods ('produce_stone_pickaxe', craft_stone_pickaxe_at_bench)
pyhop.declare_methods ('produce_iron_axe', craft_iron_axe_at_bench)
pyhop.declare_methods ('produce_wooden_pickaxe', craft_wooden_pickaxe_at_bench)
pyhop.declare_methods ('produce_rail', craft_rail_at_bench)
pyhop.declare_methods ('produce_cart', craft_cart_at_bench)
pyhop.declare_methods ('produce_plank', craft_plank)
pyhop.declare_methods ('produce_stick', craft_stick)
pyhop.declare_methods ('produce_bench', craft_bench)

'''end recipe methods'''

# declare state
state = pyhop.State('state')
state.wood = {'agent': 0}
state.time = {'agent': 4}
# state.time = {'agent': 46}
state.wooden_axe = {'agent': 0}
state.made_wooden_axe = {'agent': False}
# your code here 

# for items
state.cart = {'agent': 0}
state.cobble = {'agent': 0}
state.ingot = {'agent': 0}
state.ore = {'agent': 0}
state.plank = {'agent': 0}
state.rail = {'agent': 0}
state.stick = {'agent': 0}

# for tools
state.iron_axe = {'agent': 0}
state.made_iron_axe = {'agent': False}
state.wooden_pickaxe = {'agent': 0}
state.made_wooden_pickaxe = {'agent': False}
state.stone_pickaxe = {'agent': 0}
state.made_stone_pickaxe = {'agent': False}
state.iron_pickaxe = {'agent': 0}
state.made_iron_pickaxe = {'agent': False}
state.stone_axe = {'agent': 0}
state.made_stone_axe = {'agent': False}
state.furnace = {'agent': 0}
state.made_furnace = {'agent': False}
state.bench = {'agent': 0}
state.made_bench = {'agent': False}

# pyhop.print_operators()
# pyhop.print_methods()

pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 1)], verbose=3)
# pyhop.pyhop(state, [('have_enough', 'agent', 'wood', 12)], verbose=3)