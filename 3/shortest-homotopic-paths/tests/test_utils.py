"""
test_utils.py
~~~~~~~~~~~~~~~

This module contains unit tests for utils
"""
from main.utils import *
import unittest


class UtilsTests(unittest.TestCase):
    """Test suite for utils
    """

    def test_merge(self):
        """Test sort.
        """

        self.assertListEqual(lexicographic_sort([]), [])
        self.assertListEqual(lexicographic_sort([(1, 1), (1, 0)]), [(1, 0), (1, 1)])
        self.assertListEqual(lexicographic_sort([(2, 2), (1, 1), (1, 0)]), [(1, 0), (1, 1), (2, 2)])

        p, rest = take_smallest([(0, 0), (1, 0), (3, 2), (2, 1)])
        self.assertListEqual(orientation_sort(rest, p), [(1, 0), (2, 1), (3, 2)])

    def test_orientation(self):
        """Test orientation.
        """

        self.assertEqual(orientation((1, 1), (2, 1), (3, 1)), 0)
        self.assertGreater(orientation((0, 0), (2, 0), (2, 1)), 0)
        self.assertLess(orientation((0, 0), (2, 0), (2, -1)), 0)

    def test_take_smallest(self):
        """Test take smallest.
        """

        p, rest = take_smallest([(1, 1), (2, 1), (3, 1)])
        self.assertEqual(p, (1, 1))
        self.assertListEqual(rest, [(2, 1), (3, 1)])

        p, rest = take_smallest([(5, 1), (2, 1), (3, 1)])
        self.assertEqual(p, (2, 1))
        self.assertListEqual(rest, [(5, 1), (3, 1)])

    def test_line_intersection(self):
        """Test take smallest.
        """

        self.assertTrue(line_intersection([(0, -1), (0, 1)],[(-1, 0), (1, 0)]))
        self.assertFalse(line_intersection([(0, 0), (1, 0)],[(1, 1), (1, 1)]))

        self.assertFalse(line_intersection([(0, 1), (-1, 0)], [(1, 0), (0.8, 0.8)]))

    def test_has_common_point(self):
        """Test take smallest.
        """

        self.assertTrue(has_common_point([(1, 2), (3, 4)], [(5, 6), (1, 2)]))
        self.assertFalse(has_common_point([(1, 2), (3, 4)], [(5, 6), (7, 8)]))

    def test_connect_points(self):
        """Test take smallest.
        """

        self.assertListEqual(connect_points([(1, 1), (2, 2)]), [[(1, 1), (2, 2)], [(2, 2), (1, 1)]])
        self.assertListEqual(connect_points([(1, 1), (2, 2)], False), [[(1, 1), (2, 2)]])


if __name__ == '__main__':
    unittest.main()
