class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next


class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return 'stack is empty!'
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.linkedlist.head
            counter = 0
            while temp:
                temp = temp.next
                counter += 1
            return counter

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedlist.head = node
        else:
            node.next = self.linkedlist.head
            self.linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            return 'The stack is empty!'
        temp = self.linkedlist.head.value
        self.linkedlist.head = self.linkedlist.head.next
        return temp

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty!'
        return self.linkedlist.head.value

    def delete(self):
        self.linkedlist.head = None


stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print('-----')
print(stack.pop())
print('-----')
print(stack)
print('-----')
print(stack.peek())
print('----')
print(stack.pop())
print(stack.pop())
print(len(stack))
stack.delete()
print(stack)
stack.push(1)
print(stack)
