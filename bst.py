from collections import *
from binary_tree import print_binary_tree


class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


root = bst(2)
root.left = bst(1)
root.right = bst(3)


print_binary_tree(root)
    

def search_in_bst(root,value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif value< root.data == value:
        return search_in_bst(root.left, value)
    else:
        return search_in_bst(root.right, value)

print("Search 3 in root 1:", search_in_bst(root,3))
print("Search 9 in root 1:", search_in_bst(root,9))

def insert_in_bst(root,value):
    if root is None:
        return bst(value)
    if value < root.data:
        root.left = insert_in_bst(root.left,value)
    else:
        root.right = insert_in_bst(root.right,value)
    return root

def delete_in_bst(root,value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete_in_bst(root.left,value)
    elif value > root.data:
        root.right = delete_in_bst(root.right,value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_node = root.right
            while min_node is not None:
                min_node = min_node.left
            root.data = min_node.data
            root.right = delete_in_bst(root.right, min_node.data)
    return root

target = 4
root = insert_in_bst(root,target)
print("Insert 4 in root 1:")
print_binary_tree(root)

root1 = delete_in_bst(root,target)
print("Delete 4 in root 1")
print_binary_tree(root1)


#successor and predescessor in a bst
# recover bst
# bst queries
# kth smallest in bst
# sorted list to bst
# check bst 
# print elements in a range
# check bst using limits
# bst class search
# bst class insert delete 
# balancing a tree
# traversal in binary tree
# count nodes in an array tree