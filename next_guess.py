



# Eliminates answers from the list of the answers based on the possible positions of
# letters that are left.
# @param answers -> list of words that can be answers.
# @param possible_positions -> dictionary that maps each letter to a list of positions (1-5)
# 														 that are still possible.
# @return -> list of answers after eliminating ones that are not possible.
def eliminate_answers(answers, possible_positions):
	print("Answers before:", len(answers))

	# Create copy of guesses list
	new_answers = []
	for w in answers:
		new_answers.append(w)

	# Eliminate impossible answers
	for word in answers:
		for i in range(0, 5):
			if (i+1) not in possible_positions[word[i]]:
				new_answers.remove(word)
				break
			
	print("Answers after:", len(new_answers), "\n")
	return new_answers

