print "Hello, world!"

def factorial(n):
	assert type(n) == int
	val = 1
	for i in range(n+1)[1:]:
		val *= i
	return val

print factorial(3)
