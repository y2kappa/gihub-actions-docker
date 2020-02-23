from fns import add
import unittest

class Test(unittest.TestCase):

    def test_add(self):
        res = add(2, 3)
        self.assertEqual(res, 5)

if __name__ == "__main__":
    unittest.main()
