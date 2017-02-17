import math

class Distance():
	def __init__(self):
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
	
	def distance(self, x1, x2, y1, y2):
		try:
			self.x1 = float(x1)
			self.x2 = float(x2)
			self.y1 = float(y1)
			self.y2 = float(y2)
		except ValueError:
			raise ValueError("Invalid Input")
		
		return math.sqrt(self.x1 * self.x2 + self.y1 * self.y2)
		