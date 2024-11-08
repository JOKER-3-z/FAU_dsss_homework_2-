import unittest
from math_quiz import function_integer_choice, function_operation_choice, function_calculation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_integer_choice(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if random operator generated are within the specified range
        for _ in range(1000):
            rand_oper = function_operation_choice()
            self.assertTrue(rand_oper in ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '*', '5 * 3', 15),
                (3, 1, '-', '3 - 1', 2),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                fproblem ,fanswer = function_calculation(num1,num2,operator)
                self.assertTrue(fproblem == expected_problem)
                self.assertTrue(fanswer == expected_answer)

if __name__ == "__main__":
    unittest.main()
