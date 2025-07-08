class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

# first = Node(1)
# second = Node(2)
# third = Node(3)

# print(id(first),"\n",id(second),"\n",id(third))
        

# first.next = second
# second.next = third 

# head =first

# del(first)
# del(second)
# del(third)

# print(head.next.next.data)

def print_linked_list(head):
    while(head!= None):
        print(head.data,end='\n')
        head = head.next
    return

# print(print_linked_list(head))




