import math

class Distance():
	#take in two points, and output the distance between them
	def distance(self, x1, y1, x2, y2):
		
		#make sure they are floats
		try:
			x1 = float(x1)
			x2 = float(x2)
			y1 = float(y1)
			y2 = float(y2)
		except ValueError:
			raise ValueError("Invalid Input")
	
		#return the distance
		return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
		