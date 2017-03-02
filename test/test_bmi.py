import unittest
from app.bmi import BMI


class TDD(unittest.TestCase):
    def setUp(self):
        self.body_mass = BMI()

    def test_bmi_returns_correct(self):
        result = self.body_mass.bmi(125,63)
        self.assertEqual('22.7',result)
        result = self.body_mass.bmi(170,73)
        self.assertEqual('23.0',result)

    def test_bmi_rejects_negative_values(self):
        self.assertRaises(ValueError,self.body_mass.bmi, -125, 63)

    def test_bmi_accepts_floats_only(self):
        self.assertRaises(TypeError,self.body_mass.bmi,"one-hundred and twenty-five", 63)

    def tearDown(self):
        self.body_mass = None
