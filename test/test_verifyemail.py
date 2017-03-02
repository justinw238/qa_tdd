import unittest
from app.verifyemail import VerifyEmail


class TDD(unittest.TestCase):
    def setUp(self):
        self.verify = VerifyEmail()

    def test_return_correct_type(self):
        self.assertEqual(True, self.verify.verifyEmail("name@email.com"))

    def test_check_for_at_symbol(self):
        self.assertEqual(True, self.verify.verifyEmail("a@b.cd"))
        self.assertEqual(True, self.verify.verifyEmail("something@else.wat"))
        self.assertEqual(False, self.verify.verifyEmail("hello"))

    def test_check_email_format(self):
        self.assertEqual(True, self.verify.verifyEmail("something@else.wat"))
        self.assertEqual(True, self.verify.verifyEmail("wat@thislongname.co"))
        self.assertEqual(False, self.verify.verifyEmail("somethingwithoutat.bla"))
        self.assertEqual(False, self.verify.verifyEmail("somethingwithout@dotcom"))
        self.assertEqual(False, self.verify.verifyEmail("something@with.toomuchhere"))

