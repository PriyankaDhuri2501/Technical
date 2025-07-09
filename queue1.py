class QueueUsingList():
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def is_Empty(self):
        return self.size()==0
    
    def enqueue(self,data):
        self.__queue.append(data)
        return f"We have added data to the queue"
    
    def front(self):
        if(self.size()==0):
            print("Queue is Empty, cannot dequeue")
            return None
        return self.__queue[0]
    
    def dequeue(self):
        if(self.size()==0):
            print("Queue is Empty, cannot dequeue")
            return None
        
        return self.__queue.pop(0)
    
Q = QueueUsingList()



Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.dequeue()
print(Q.size())
print(Q.is_Empty())
print(Q.front())


