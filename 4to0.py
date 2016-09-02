def inital_position() :
	return 6

def primitive(pos) :
	if (pos == 0):
		return "Lose"
	else:
		return "Undecided"

def gen_moves(pos) :
	if (pos >= 2): 
		return [2, 1]
	else:
		return [1]

def do_moves(pos, move) :
	return pos - move


def solve(pos) :

	saved_states = {} 

	def solver(pos, saved_states):

		fate = "Lose"

		if primitive(pos) == "Lose" or saved_states.get(pos) == "Lose":
			saved_states[pos] = "Lose"
		else :
			for move in gen_moves(pos):
				new_pos = do_moves(pos, move)
				
				if (new_pos in saved_states):
					player2_saved = saved_states[new_pos]
					if (player2_saved == "Lose"):
						fate = "Win"

				player2_result = solver(new_pos, saved_states)
				if (player2_result == "Lose"):
					fate = "Win"

		saved_states[pos] = fate
		return fate

	return solver(pos, saved_states)

start = inital_position()
result = solve(start)
print("Player 1 will " + result)



