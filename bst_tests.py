import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

class BSTTests(unittest.TestCase):

    def test_example_fun(self):
        self.assertEqual(True, example_fun(34))
        self.assertEqual(False, example_fun(1423))

    def test_is_empty(self):
        self.assertTrue(is_empty(None))
        self.assertFalse(is_empty(Node(10, None, None)))

    def test_insert_and_lookup(self):
        bst = frozenBinarySearchTree(lambda a, b: a < b, None)
        bst = insert(bst, 10)
        bst = insert(bst, 5)
        self.assertTrue(lookup(bst, 10))
        self.assertFalse(lookup(bst, 99))

    def test_find_min(self):
        bst = Node(10, Node(3, None, None), None)
        self.assertEqual(find_min(bst), 10)
        self.assertEqual(find_min(Node(7, None, None)), 7)

    def test_delete(self):
        bst = frozenBinarySearchTree(lambda a, b: a < b, None)
        bst = insert(bst, 10)
        bst = insert(bst, 5)
        bst = insert(bst, 15)
        bst = delete(bst, 10)
        self.assertFalse(lookup(bst, 10))
        self.assertTrue(lookup(bst, 5))

if __name__ == '__main__':
    unittest.main()
