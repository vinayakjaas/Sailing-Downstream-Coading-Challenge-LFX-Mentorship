from reducelist import *
from unittest import TestCase

import unittest

class TestReduce(TestCase):
    
    def test_reduce(self):
        """Tests the `reduce` function in `reducelist` package.
        """
        
        test1 = list(range(1, 21))
        test2 = list(range(1, 11))
        
        c1 = [1, 2, 6, 8, 12, 14, 18, 20]
        c2 = [1, 2, 6, 8]
        
        cases = [
            ((test1,), c1),
            ((test2,), c2),
        ]
        
        success = 0
        for i, (t, c) in enumerate(cases):
            try:
                self.assertEqual(reduce(*t), c)
                success += 1
            except AssertionError:
                print(f"Failed testcase {i} t = {t}; c = {c}")
                print(f"Got {reduce(*t)}...")
        
        print(f"Passed {success}/{len(cases)} test cases...")


if __name__ == '__main__':    
    unittest.main()