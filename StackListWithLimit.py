class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        if self.isEmpty():
            return 'Stack is empty!'
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            counter = 0
            for i in self.list:
                counter += 1
            return counter

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def delete(self):
        self.list = []

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty!'
        else:
            return self.list[-1]

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty!'
        else:
            return self.list.pop(-1)

    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        return False

    def push(self, value):
        if not self.isFull():
            self.list.append(value)
            return 'value pushed successfully!'
        else:
            return 'The stack is full!'


stack = Stack(max_size=3)
print(stack.isEmpty())
print(stack)
print(len(stack))
print(stack.isFull())
print('-----')
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack)
print(stack.isFull())
print('-----')
print(stack.push(4))
print(stack.pop())
print(stack.isFull())
print(stack.push(4))
print(stack.peek())
stack.delete()
print(stack)
