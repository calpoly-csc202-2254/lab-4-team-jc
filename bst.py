import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

def example_fun(x : int) -> bool:
    return x < 142

## Data Definitions
BinTree = Union['Node', None]

@dataclass(frozen=True)
class Node:
    element: Any
    right: BinTree
    left: BinTree

@dataclass(frozen=True)
class frozenBinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

# Function 1
# PS: Return True if BinarySearchTree is empy, otherwise False
def is_empty(b: BinTree) -> bool:
    if b is None:
        return True
    else:
        return False

# Function 2
# PS: Add a value to a BST using comes_before func. and returns the resulting Tree
def insert(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def insert_helper(b: BinTree, v: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if b is None:
            return Node(v, None, None)
        if comes_before(v, b.element):
            left = insert_helper(b.left, v, comes_before)
            return Node(b.element, left, b.right)
        else:
            right = insert_helper(b.right, v, comes_before)
            return Node(b.element, b.left, right)

    new_tree = insert_helper(bst.tree, value, bst.comes_before)
    return frozenBinarySearchTree(bst.comes_before, new_tree)




