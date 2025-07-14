class stack_list:
    def __init__(self):
        self.__stack = []

    def push(self,data):
        self.__stack.append(data)
        print(f"pushed {data} into stack")

    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def top(self):
        if self.is_empty():
            print("Stack is empty in top")
            return None
        # return self.stack(len(self.__stack)-1)
        return self.__stack[-1]
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty in pop")
            return None
        return self.__stack.pop()
    
myStack = stack_list()
print(myStack.is_empty())

print(myStack.push(10))
print(myStack.push(7))
print(myStack.push(3))
print(myStack.push(1))


print(myStack.pop())


print(myStack.top())

print(myStack.size())

