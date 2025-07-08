from linked_list import *

def take_input():
    value = int((input("Enter the value of node or to stop -1:")))
    head = None
    tail = None
    while value!=-1:
        new_node = Node(value)
        if head == None:
            head = new_node
        else:
            temp = head
            while temp.next!= None:
                temp= temp.next
            temp.next = new_node
            
        value = int((input("Enter the value of node or to stop -1:")))
    return head 

def delete(head1):
    if head1== None or head1.next== None:
        return None
    temp = head1
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head1
    
    

def insert(head1):
    val = int(input("Enter new node to add:"))
    newnode = Node(val)
    newnode.next = head1
    return newnode




def len(head1):
    if head1 == None:
        return 0
    else:
        return 1+len(head1.next)


head1 = take_input()

# print(len(head1))

print_linked_list(head1)
# head1 = insert(head1)
# print_linked_list(head1)
head1 = delete(head1)
print("Tail deleted: ")
print_linked_list(head1)







