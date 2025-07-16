from binary_tree import *

def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    heightoftree = 1+max(left_height,right_height)

    return heightoftree

root = height()
print("Height of the tree :", height(root))



def diameter_of_a_tree(root):
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    left_diameter = diameter_of_a_tree(root.left)
    right_diameter = diameter_of_a_tree(root.right)

    return max(left_diameter,right_diameter,leftHeight,rightHeight)
print("Diameter of the tree is: ",diameter_of_a_tree(root))



def count_nodes(root):
    if(root== None):
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    
print("Count of the node:", count_nodes(root))


def sum_of_nodes(root):
    if(root==None):
        return 0
    else:
        return root.data + count_nodes(root.left) + count_nodes(root.right)
    
print("Sum of the node:", sum_of_nodes(root))