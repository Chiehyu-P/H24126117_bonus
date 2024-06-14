import random

def valid_alphabet(guess_alphabet,guess_list,tries):
	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	while True:
		if guess_alphabet not in alphabet:
			#當guess_alphabet沒有在alphabet中重新輸入
			print('Please enter a lowercase alphabet.')
			guess_alphabet=input('Guess the lowercase alphabet: ')
		else:
			guess_list.append(guess_alphabet)
			tries+=1
			#直到輸入有在alphabet中的值回傳guess_alphabet,guess_list,tries
			return guess_alphabet,guess_list,tries
			break


def condition(correct,guess_alphabet,guess_list,tries):
	tmpt=True
	#判斷guess_alphabet是否是有在alphabet中
	guess_alphabet,guess_list,tries=valid_alphabet(guess_alphabet,guess_list,tries)
	if guess_alphabet==correct:
		#在第一次輸入時判斷是否正確
		tries=1
		print('Congratuation! You guess the alphabet {} in {} tries'.format(correct,tries))
		tmpt=False
		return True,guess_list
	while tmpt:
		#重覆判斷不同情況
		if guess_alphabet>correct:
			print('The alphabet you are looking for is alphabetically lower.')
			guess_alphabet=input('Guess the lowercase alphabet: ')
			#每重新輸入一次guess_alphabet就去判斷一次guess_alphabet是否是有在alphabet中
			guess_alphabet,guess_list,tries=valid_alphabet(guess_alphabet,guess_list,tries)

		elif guess_alphabet<correct:
			print('The alphabet you are looking for is alphabetically higher.')
			guess_alphabet=input('Guess the lowercase alphabet: ')
			guess_alphabet,guess_list,tries=valid_alphabet(guess_alphabet,guess_list,tries)

		elif guess_alphabet==correct:
			#當輸入正確回傳True,guess_list
			print('Congratuation! You guess the alphabet {} in {} tries'.format(correct,tries))
			return True,guess_list
			break


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#隨機產生一個正確的字母
correct=random.choice(alphabet)
print(correct)  
guess_list=[]
tries=0

guess_alphabet=input('Guess the lowercase alphabet: ')

while True:
	#判斷guess_alphabet是否有猜中
	count,guess_list=condition(correct,guess_alphabet,guess_list,tries)

	#看guess_list在各區間中有幾個數
	interval_1=0
	interval_2=0
	interval_3=0
	interval_4=0
	interval_5=0
	interval_6=0
	interval_7=0

	#列舉不同區間會有的字母
	intervalalphabet_1=['a','b','c','d']
	intervalalphabet_2=['e','f','g','h']
	intervalalphabet_3=['i','j','k','l']
	intervalalphabet_4=['m','n','o','p']
	intervalalphabet_5=['q','r','s','t']
	intervalalphabet_6=['u','v','w','x']
	intervalalphabet_7=['y','z']

	if count==True:
		for i in guess_list:
			#如果guess_list在各區間中interval
			if i in intervalalphabet_1:
				interval_1+=1
			elif i in intervalalphabet_2:
				interval_2+=1
			elif i in intervalalphabet_3:
				interval_3+=1
			elif i in intervalalphabet_4:
				interval_4+=1
			elif i in intervalalphabet_5:
				interval_5+=1
			elif i in intervalalphabet_6:
				interval_6+=1
			elif i in intervalalphabet_7:
				interval_7+=1

		#印出Histogram
		print(' ')
		print('Guess Histogram:')
		print('a-d','*'*interval_1)
		print('e-h','*'*interval_2)
		print('i-l','*'*interval_3)
		print('m-p','*'*interval_4)
		print('q-t','*'*interval_5)
		print('u-x','*'*interval_6)
		print('y-z','*'*interval_7)
		exit()




