https://books.google.hu/books?id=vTK_vVXV-m0C&pg=PA365&lpg=PA365&dq=model+solar+system+programming+python&source=bl&ots=o6sWWPOorR&sig=R9RlpbTlYIgufhpXvNgjJOeOFws&hl=en&sa=X&redir_esc=y#v=onepage&q=model%20solar%20system%20programming%20python&f=false

class Planet: 
	# constructor
	def __init__(self, name, radius, mass, distance):
		self.name = name
		self.radius = radius
		self.mass = mass
		self.distance = distance

	def __str__(self):
		return self.name

	def __repr__(self):
		return 'yo'

class Sun:

	def __init__(self, radius, mass):
		self.radius = radius
		self.mass = mass


class SolarSystem:

	def __init__(self, name, sun):
		self.name = name
		self.sun = sun
		self.planets = []

	def __repr__(self):
		return self.name

	def addPlanet(self, planet):
		self.planets.append(planet)

	def showPlanets(self):
		for planet in self.planets:
			print planet

mercury = Planet('Mercury', 5, 25, 500)
print mercury

solar_system = SolarSystem('Solar System', Sun(3, 5))

print solar_system
