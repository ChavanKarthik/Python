class A:
	def sum(x,y,z):
		return (x+y+z)
	def sub(x,y,z):
		return ((x-y)-z)

class B:
	def sum(x,y):
		return (x*y)
	def sub(x,y):
		return (x-y)

class C:
	def sum(x):
		return (x**2)
	def sub(x):
		return ((x**2)-x)

for z in range(4):
	for y in range(4):
		for x in range(12):
			if (x<11):
				print('# ', end=" ")
			else:
				print('# ')
				break
