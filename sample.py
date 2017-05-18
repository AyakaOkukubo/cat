for i in range(1,21):
	if i%15 == 0:
		print('FizzBuzz')
	elif i%3 == 0:
		print('{} is Fizz'.format(i))
	elif i%5 == 0:
		print('Buzz')
	else:
		print(i)
print('End')

