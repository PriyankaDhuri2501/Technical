from collections import *

class tree:
    def __init__(self,data):
        self.data = data
        self.children = []

# root = tree(1)
# child1 = tree(2)
# child2 = tree(3)
# child3 = tree(4)

# root.children.extend([child1,child2,child3])

# print(root.children[0].data)

def print_tree(root):
    print(root.data)

    for eachchild in root.children:
        print_tree(eachchild)

# print_tree(root)

def print_tree_imp(root):
    if root == None:
        return
    
    print(f"{root.data}", end=":")

    for eachchild in root.children:
        print(eachchild.data,end =",")
    print()

    for eachchild in root.children:
        print_tree_imp(eachchild)


    

def take_input_level():
    data = int(input("Enter the root data:"))
    root = tree(data)

    queue = deque([root])

    while len(queue)!= 0:
        current_node = queue.popleft()
        num_children = int(input("Enter the no. of children for "+str(current_node.data)))

        for i in range(num_children):
            child_data = int(input(f"Enter the data for {i+1} of node {current_node.data}"))
            child_node = tree(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)

    return root

root = take_input_level()

print_tree_imp(root)
        
