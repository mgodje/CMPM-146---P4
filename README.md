Maryann Godje and Andrew Byi

The heuristic we chose to program was one where it prunes the branch (returns True) if the current task at hand does produce a tool. 
This method prevents infinite loops from happening. 
For example, if we need to produce an wooden axe, and a wooden axe can be produced, then it will return true. 
Without this implementation, it may go through finding a wood, a stick, then plank, then a wooden axe over and over. 
This way, with our heuristic, it will stop once the wooden axe is made.
We applied this to the following: furnace, bench, iron pickaxe, iron axe, wooden pickaxe, wooden axe, stone pickaxe, stone axe, rail, and cart.