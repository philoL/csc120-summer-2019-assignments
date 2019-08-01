# CSc 120: Construct Binary Search Tree from Preorder Traversal

## Expected Behavior
Implement at least one function *build_tree(preorder)* (**preorder** is a list of intergers), and a tree class. The build_tree function should return a tree object. The tree object should have a __str__ method to print trees as the output in examples.

## Algorithm
For a normal binary tree, it needs two traversals (e.g., preorder and inorder traversals)to build the tree. However, for binary search tree, it only needs preorder traversal to build the tree. E.g., given a preorder traversal "8, 5, 1, 7, 10, 12", the first element 8 should be the root, and the following "5, 1, 7" should be the left subtree, since they are smaller than 8; the rest "10, 12" should be the right subtree.

## Examples

```
>>> str(build_tree([8, 5, 1, 7, 10, 12]))
'(8 (5 (1 None None) (7 None None)) (10 None (12 None None)))'

>>> str(build_tree([]))
'None'

>>> str(build_tree([1, 2, 3, 4, 5]))
'(1 None (2 None (3 None (4 None (5 None None)))))'

>>> str(build_tree([5, 4, 3, 2, 1]))
'(5 (4 (3 (2 (1 None None) None) None) None) None)'

>>> str(build_tree([23, 24, 13, 42, 21]))
'(23 None (24 (13 None None) (42 (21 None None) None)))'

```