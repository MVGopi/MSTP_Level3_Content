try:
	a = input('Enter a value : ')
	b = 5
	c = a + b
	print(c)
except TypeError:
	#a = int(input('Enter a value : '))
	#b = 5
	c = int(a) + b
finally:
	print(c)