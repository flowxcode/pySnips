from . import elgamal_flowx    # The code to test
import unittest   # The test framework

class Test_gcd(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(elgamal_flowx.gcd(85, 995), 5)


if __name__ == '__main__':
    unittest.main()
    

    