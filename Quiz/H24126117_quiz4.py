sequence=input('Enter a sequence of integers separated by whitespace: ')
list_sequence=sequence.split(' ')
num_sequence=[int(x) for x in list_sequence]

temp_LICS=[num_sequence[0]]
LICS=[]

for element in num_sequence[1:]:
	if element>temp_LICS[-1]:
		temp_LICS.append(element)
	else:
		if len(temp_LICS)>len(LICS):
			LICS=temp_LICS
		temp_LICS=[element]

if len(temp_LICS)>len(LICS):
	LICS=temp_LICS

print('Length: ',len(LICS))
print('LICS: ',LICS)
