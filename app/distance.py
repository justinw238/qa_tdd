import math

class Distance():
	def __init__(self):
		#self.x1 = 0
		#self.x2 = 0
		#self.y1 = 0
		#self.y2 = 0
		pass
	
	def distance(self, x1, y1, x2, y2):
		
		try:
			x1 = float(x1)
			x2 = float(x2)
			y1 = float(y1)
			y2 = float(y2)
		except ValueError:
			raise ValueError("Invalid Input")
		#result = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
		
		result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
		return result
		