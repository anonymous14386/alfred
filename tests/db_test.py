import unittest
import data.db as db


class TestDBMethods(unittest.TestCase):

    def test_getNumber(self):
        self.assertEqual(db.getNumber(), 42)


if __name__ == "__main__":
    unittest.main()
