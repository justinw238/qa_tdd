import unittest
from app.distance import Distance

class TDD(unittest.TestCase):
	def setUp(self):
		self.dist = Distance()
		
	def test_distance_returns_correct_results(self):
		result = self.dist.distance(2,1,2,1)
		self.assertEqual(2, result)
		
	def test_distance_only_int_input(self):
		self.assertRaises(ValueError, self.dist.distance, 'one', 'one', 'one', 'one')
		