class user:
	def __init__(self, full_name, birthday):
		self.name=full_name
		self.birthday=birthday
user=user("Ram",'18830101')
print(user.name)
print(user.birthday)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 = Person("Benny", 45)
p3 = Person("aston", 24)

print(p1)