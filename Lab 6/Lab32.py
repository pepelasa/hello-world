import unittest
import filecmp


class Test_Lab32(unittest.TestCase):
    # Right
    def test_same(self):
        self.assertEqual(filecmp.cmp("1.txt", "2.txt"), True)

    def test_dif(self):
        self.assertFalse(filecmp.cmp("1.txt", "3.txt"))
    # Boundaries

    # Inverse relationships

    # Cross-check results by other means

    # Errors forced to happen
    def test_nofile(self):
        with self.assertRaises(FileNotFoundError):
            filecmp.cmp("1.txt", "nofile.txt")
    # Performance


if __name__ == '__main__':
    unittest.main()
