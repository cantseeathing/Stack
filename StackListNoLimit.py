class Stack:
    def __init__(self):
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

    def push(self, value):
        self.list.append(value)
        return 'value pushed successfully!'

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty!'
        else:
            return self.list.pop(-1)

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty!'
        else:
            return self.list[-1]

    def delete(self):
        self.list = []

stack = Stack()
print(stack.isEmpty())
print(stack)
print(len(stack))
print('-----')
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print('-----')
print(stack.pop())
print(stack.peek())
stack.delete()
print(stack)