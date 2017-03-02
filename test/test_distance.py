import unittest
from app.distance import Distance

class TDD(unittest.TestCase):
	def setUp(self):
		self.dist = Distance()
		
	def test_distance_returns_correct_results_positive_input(self):
		result = self.dist.distance(1,1,1,2)
		self.assertEqual(1, result)
		
	def test_distance_returns_correct_results_negative_input(self):
		result = self.dist.distance(-1,-1, -1, -2)
		self.assertEqual(1, result)
		
	def test_distance_returns_correct_results_mixed_input(self):
		result = self.dist.distance(-1,1, 1, 1)
		self.assertEqual(2, result)		
		
	def test_distance_only_int_input(self):
		self.assertRaises(ValueError, self.dist.distance, 'one', 'one', 'one', 'one')
		
	def tearDown(self):
		self.dist = None
		