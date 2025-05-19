import sys
import unittest
from typing import *
from dataclasses import dataclass
import random
import time
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

# -- 

# Function #3 
# PS: 
def lookup(bst: frozenBinarySearchTree, value: Any) -> bool:
    def lookup_helper(b: BinTree, v: Any, comes_before: Callable[[Any, Any], bool]) -> bool:
        if b is None:
            return False
        if not comes_before(v, b.element) and not comes_before(b.element, v): 
            return True
        if comes_before(v, b.element):
            return lookup_helper(b.left, v, comes_before)
        else:
            return lookup_helper(b.right, v, comes_before)
    return lookup_helper(bst.tree, value, bst.comes_before)


# Function 4
# PS: 
def find_min(b: BinTree) -> Any: 
    if b.left is None:
        return b.element
    return find_min(b.left)



def delete(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def delete_helper(b: BinTree, v: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if b is None: 
            return None
        if not comes_before(v, b.element) and not comes_before(b.element, v):
            if b.left is None:
                return b.right
            if b.right is None: 
                return b.left
            
            Tree = find_min(b.right)
            delete_helper(b.right, Tree, comes_before)
            return Node(Tree, b.left, b.right)
        elif comes_before(b, b.element):
            left = delete_helper(b.left, v, comes_before)
            return Node(b.element, left, b.right)
        else:
            right = delete_helper(b.right, v, comes_before)
            return Node(b.element, b.left, right)
        
    new_tree = delete_helper(bst.tree, value, bst.comes_before)
    return frozenBinarySearchTree(bst.comes_before, new_tree)

#
def test_bst_performance():
    sizes = [100_000 * i for i in range(1, 11)]  # 100K to 1M
    insert_times = []
    search_times = []

    def comes_before(a, b):
        return a < b

    for size in sizes:
        values = [random.random() for _ in range(size)]
        bst = frozenBinarySearchTree(comes_before, None)

        # Time insertion
        start = time.perf_counter()
        for v in values:
            bst = insert(bst, v)
        end = time.perf_counter()
        insert_time = end - start
        insert_times.append(insert_time)

        # Time search (search for random values not in the tree)
        search_values = [random.random() for _ in range(1000)]
        start = time.perf_counter()
        for v in search_values:
            lookup(bst, v)
        end = time.perf_counter()
        search_time = end - start
        search_times.append(search_time)

        # Print result for this size
        print(f"Size: {size:>7,} | Insert Time: {insert_time:.4f} sec | Search Time: {search_time:.4f} sec")

    return sizes, insert_times, search_times

if __name__ == "__main__":
    test_bst_performance()