from collections import *

class binarytree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# root = binarytree(1)
# root.left = binarytree(2)
# root.right = binarytree(3)
# root.left.left = binarytree(4)
# root.left.right = binarytree(5)
# root.right.left = binarytree(6)
# root.right.left.left = binarytree(7)
# root.right.left.right = binarytree(8)
# root.right.left.right.left = binarytree(10)

def print_binary_tree(root):
    if root is None:
        return
    
    print(root.data,end=':')

    if(root.left is not None):
        print(f"l->{root.left.data}", end = '\n')
    else:
        print("L->None", end = "\n")

    if(root.right is not None):
        print(f"R->{root.right.data}", end = '\n')
    else:
        print("R->None", end = "\n")

    print_binary_tree(root.left)
    print_binary_tree(root.right)
    

# def take_input_level_wise():
#     data = int(input("ENter the data for the root:"))
#     if(data == -1):
#         return None
    
#     root = binarytree(data)
#     queue = deque([root])

#     while len(queue)!=0:
#         current_node = queue.popleft()

#         left_child_data = int (input(f"Enter left child for{current_node.data }"))
#         if(left_child_data!=-1):
#             left_node = binarytree(left_child_data)
#             current_node.left = left_node
#             queue.append(left_node)

#         right_child_data = int (input(f"Enter right child for{current_node.data }"))
#         if(right_child_data!=-1):
#             right_node = binarytree(right_child_data)
#             current_node.right = right_node
#             queue.append(right_node)
#     return root

# print_binary_tree(root)
    


# root = take_input_level_wise()


