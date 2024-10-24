import unittest

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def find_max_digit_sum(numbers):
    max_number = None
    max_sum = -1

    for num in numbers:
        current_sum = sum_of_digits(num)

        if current_sum > max_sum:
            max_sum = current_sum
            max_number = num

    return max_number

class TestSumAndMaxDigitSum(unittest.TestCase):

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(-456), 15)
        self.assertEqual(sum_of_digits(0), 0)
        self.assertEqual(sum_of_digits(987654321), 45)
        self.assertEqual(sum_of_digits(1001), 2)

    def test_find_max_digit_sum(self):
        self.assertEqual(find_max_digit_sum([12, -34, 56]), 56)      # 12 (3), -34 (7), 56 (11)
        self.assertEqual(find_max_digit_sum([7]), 7)                  # 7 (7)
        self.assertEqual(find_max_digit_sum([100, 200]), 200)         # 100 (1), 200 (2)
        self.assertEqual(find_max_digit_sum([-10, -20, -30]), -30)    # -10 (1), -20 (2), -30 (3)
        self.assertEqual(find_max_digit_sum([-10, -20, -30, -5]), -5) # -10 (1), -20 (2), -30 (3), -5 (5)

if __name__ == '__main__':
    unittest.main()



