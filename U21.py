class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:        
        return self.queue.pop(0)
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue)==0
        
obj = MyQueue()
param_1 = obj.push(1)
param_2 = obj.push(2)
param_3 = obj.pop() 
param_4 = obj.peek()  
param_5 = obj.empty()  

print(param_1)
print(param_2)
print(param_3) 
print(param_4)  
print(param_5)  
