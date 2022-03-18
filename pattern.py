from copy import copy


# Get the pattern that would be reveals from a guess if we know the answer.
# @param guess -> the word that we are guessing.
# @param answer -> the answer to the wordle.
# @return -> a list with the pattern that would be revealed
def get_pattern_from_words(guess, answer):
	pattern = []

	for i in range(0, 5):
		if guess[i] == answer[i]:
			pattern.append("correct")
		else:
			if guess[i] in answer:
				# see if we already gave a "present" hint for this letter, or if it's correct
				reveal_count = 0
				letter_count = 0
				for j in range(0, i):
					if guess[j] == guess[i] and pattern[j] == "present":
						reveal_count += 1
				
				for j in range(0, 5):
					if j != i and guess[j] == guess[i]: # going to be correct hint
						reveal_count += 1

				for l in answer:
					if l == guess[i]:
						letter_count += 1

				if reveal_count < letter_count:
					pattern.append("present")
				else:
					pattern.append("absent")
			else:
				pattern.append("absent")
	return pattern




def get_pattern_frequencies(guess, answers):
	# initialize frequencies
	frequencies = {}

	for answer in answers:
		pattern = get_pattern_from_words(guess, answer)	
		index = get_index_from_pattern(pattern)
		if index in frequencies:
			frequencies[index] += 1
		else:
			frequencies[index] = 1
	return frequencies



#
def get_index_from_pattern(pattern):
	evaluations = {}
	evaluations["a"] = 0
	evaluations["p"] = 1
	evaluations["c"] = 2

	index = 0
	for i in range(0, 5):
		index += evaluations[pattern[i][0]] * pow(3, i)
	return index



#
def get_index_patterns():
	evaluations = ["absent", "present", "correct"]
	patterns = {}
	pattern = []

	for i in range(0, 3):
		pattern.append(evaluations[i])
		for j in range(0, 3):
			pattern.append(evaluations[j])
			for k in range(0, 3):
				pattern.append(evaluations[k])
				for n in range(0, 3):
					pattern.append(evaluations[n])
					for m in range(0, 3):
						pattern.append(evaluations[m])
						index = (i * pow(3, 4)) + (j * pow(3, 3)) + (k * pow(3, 2)) + (n * pow(3, 1)) + (m * pow(3, 0)) 
						patterns[index] = copy(pattern)
						pattern.pop()
					pattern.pop()
				pattern.pop()
			pattern.pop()
		pattern.pop()
	return patterns



def compare_patterns(p1, p2):
	for i in range(0, 5):
		if p1[i] != p2[i]:
			return False
	return True
