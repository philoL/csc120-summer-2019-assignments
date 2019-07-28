import unittest
from unittest import TestCase
from unittest.mock import patch
from expression_tree import *
from gradescope_utils.autograder_utils.decorators import weight

class TestExpressionTree(TestCase):

	@weight(3)
	def testcase_1(self):
		self.assertEqual(str(build_parsetree("7")), "(7 None None)")

	@weight(3)
	def testcase_2(self):
		self.assertEqual(str(build_parsetree("7 * 5 ")), "(* (7 None None) (5 None None))")

	@weight(3)
	def testcase_3(self):
		self.assertEqual(str(build_parsetree("( 7 )")), "(@ (7 None None) None)")

	@weight(3)
	def testcase_4(self):
		self.assertEqual(str(build_parsetree("4  * ( 2 - 2 )")), "(* (4 None None) (- (2 None None) (2 None None)))")

	@weight(3)
	def testcase_5(self):
		self.assertEqual(str(build_parsetree("( 4 - 3 )  * ( 2 / 2 )")), "(* (- (4 None None) (3 None None)) (/ (2 None None) (2 None None)))")

	@weight(3)
	def testcase_6(self):
		self.assertEqual(str(build_parsetree("( 17 + 25 ) / ( 32 * 43 )")), "(/ (+ (17 None None) (25 None None)) (* (32 None None) (43 None None)))")


if __name__ == "__main__":
	unittest.main()
