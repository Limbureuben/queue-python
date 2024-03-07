class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class queue:
    def __init__(self):
        self.front = None
        self.count = 0
        
    def enqueue(self, data):
        newnode = node(data)
        if self.front is None:
            self.front = newnode
            self.back = newnode
            return
        
        self.back.next = newnode
        self.back = newnode
        self.count += 1
    
    def dequeue(self):
        if self.front is None:
            return None
        else:
            toreturn = self.front.data
            self.front = self.front.next
            return toreturn
        
    def printqueue(self):
        while self.front is not None:
            print(self.front.data)
            self.front = self.front.next
            
    def getfront(self):
        if self.front is None:
            return None
        
        return self.front.data
    
    def getback(self):
        if self.back is None:
            return None
        else:
            return self.back.data
        
        
queue = queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)

print("The front element is:", queue.getfront())

print("The back element is: ", queue.getback())

queue.printqueue()        
        
        
                    
                    
        