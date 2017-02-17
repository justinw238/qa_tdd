import unittest

class TDD(unittest.TestCase):
	def test_distance_returns_correct_results(self):
		dist = Distance()
		result = dist.getDistance(1,1)
		self.assertEqual(1, resul)
			