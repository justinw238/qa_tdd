import unittest
from app.distance import Distance

class TDD(unittest.TestCase):
	def test_distance_returns_correct_results(self):
		dist = Distance()
		result = dist.distance(1,1,1,1)
		self.assertEqual(1, result)
			