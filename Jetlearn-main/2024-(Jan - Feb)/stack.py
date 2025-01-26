class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        if value not in self.stack:
            self.stack.append(value)

            return True
        else:
            return False
        
    def peak(self):
        return self.stack[-1]
    
    def remove(self):
        if len(self.stack) <= 0:
            return "No item's in stack"
        else:
            return self.stack.pop(-1)
        
    def __str__(self):
        return str(self.stack)

abc = Stack()

abc.add("monday")
abc.add("tuesday")
abc.add("wednesday")

print(abc.peak())

print(abc.remove())

print(abc)