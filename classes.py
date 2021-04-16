class Dog:
	# Class attribute
	species = "canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	# instance method

	def __str__(self):
		return f"{self.name} is {self.age} years old"

	# Another instance method

	def speak(self, sound):
		return f"{self.name} says {sound}"



class JackRussellTerrier(Dog):
	def speak(self, sound="Arf"):
		return super().speak(sound)


class GoldenRetriever(Dog):
	def speak(self, sound="Bark"):
		return super().speak(sound)
	

class Dachshund(Dog):
	pass

class Bulldog(Dog):
	pass

miles = JackRussellTerrier("Miles",  4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
maxx = GoldenRetriever("Max", 7)



print(jim.speak("Woof"))
print(miles.speak())
print(maxx.speak())



