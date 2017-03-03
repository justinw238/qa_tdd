import unittest
from app.retirement import Retirement

class TDD(unittest.TestCase):
	def setUp(self):
		self.retire = Retirement()

	def test_retirment_returns_correct_results(self):
		self.assertEqual(34, self.retire.retirement(25 ,50000, 10, 50000))
		self.assertEqual(54, self.retire.retirement(50 ,50000, 20, 50000))
		self.assertEqual(100, self.retire.retirement(99, 100, 5, 100000))

	def test_retirement_non_int_input(self):
		self.assertRaises(ValueError, self.retire.retirement, 38, 'int', 25, 58000)

	def test_retirement_invalid_age(self):
		self.assertRaises(ValueError, self.retire.retirement, 105, 50000, 25, 59000)
		self.assertRaises(ValueError, self.retire.retirement, -20, 50000, 25, 59000)

	def test_retirement_invalid_salary(self):
		self.assertRaises(ValueError, self.retire.retirement, 105, -60, 25, 59000)

	def test_retirement_invalid_saving(self):
		self.assertRaises(ValueError, self.retire.retirement, 105, 50000, -5, 59000)
		self.assertRaises(ValueError, self.retire.retirement, 105, 50000, 109, 59000)

	def test_retirement_invalid_goal(self):
		self.assertRaises(ValueError, self.retire.retirement, 105, 50000, 25, -5)

	def tearDown(self):
		self.retire = None
