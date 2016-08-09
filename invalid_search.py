def udf_invalid_search_indicator(symptom):
	vowels = {'a','e','o','u','i','y'}
	digits = {'0','1','2','3','4','5','6','7','8','9'}

	with open('ErrorCodes_resolve.txt') as f:
		error_content = f.read().splitlines()
	error_content=[element.lower() for element in error_content]

	with open('non_avoid_words.txt') as f2:
		non_avoid_content = f2.read().splitlines()
	non_avoid_content=[element.lower() for element in non_avoid_content]

	indicator_invalid = 0

##	symptom=raw_input('please enter the symptom:')
	symptom=symptom.lower()

	symptom_words_list=str.split(symptom)
	for w in symptom_words_list:
		w=w.lower()
		if not (vowels.intersection(w)):
			print (w +' has no vowel!')
			indicator_invalid = 1
			if w in error_content:
				print ('but '+ w +' is a resolvable error code!')
				indicator_invalid = 0
		if (digits.intersection(w)):
			print (w,'has digits!')
			indicator_invalid = 1
			if w in error_content:
				print ('but '+ w +' is a resolvable error code!') 
				indicator_invalid = 0
		if w in non_avoid_content:
			print (w + ' is non_avoid word!')
			indicator_invalid = 1

	with open('invalid_phrases.txt') as f3:
		invalid_phrases_list = f3.read().splitlines()
	invalid_phrases_list=[element.lower() for element in invalid_phrases_list]

	if symptom in invalid_phrases_list:
		print(symptom + ' is an invalid symptom!')
		indicator_invalid = 1
		
	return indicator_invalid
