from invalid_search import udf_invalid_search_indicator

with open('test/test_set1.txt') as f1:
		test_content = f1.read().splitlines()
test_content=[element.lower() for element in test_content]

output=list()
for symptom in test_content:
	output.append(udf_invalid_search_indicator(symptom))

with open('test/test_result.txt','w') as f2:	
	for values in output:
		f2.write(str(values))
		f2.write('\n')
	f2.close()
