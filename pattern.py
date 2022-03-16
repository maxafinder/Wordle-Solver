


# Get the pattern that would be reveals from a guess if we know the answer.
# @param guess -> the word that we are guessing.
# @param answer -> the answer to the wordle.
# @return -> a list with the pattern that would be revealed
def get_pattern(guess, answer):
	print("finding pattern")
	pattern = []

	for i in range(0, 5):
		if guess[i] == answer[i]:
			pattern.append("correct")
		else:
			if guess[i] in answer:
				# see if we already gave a "present" hint for this letter
				present_count = 0
				letter_count = 0
				for j in range(0, i):
					if guess[j] == guess[i] and pattern[j] == "present":
						present_count += 1

				for l in answer:
					if l == guess[i]:
						letter_count += 1

				if present_count < letter_count:
					pattern.append("present")
				else:
					pattern.append("absent")
			else:
				pattern.append("absent")
	return pattern