class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # Fixed-size array
        self.size = 0          # Current number of elements
        self.capacity = k      # Maximum capacity
        self.front = 0         # Points to the front element
        self.rear = -1         # Points to the last element
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = value
        self.size += 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.size -= 1
        return True
    
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]
    
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
