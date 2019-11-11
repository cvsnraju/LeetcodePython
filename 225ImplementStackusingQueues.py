
# 225. Implement Stack using Queues
# Easy

# Implement the following operations of a stack using queues.

#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     empty() -- Return whether the stack is empty.


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.list.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.list) == 0:
            return False
        x = self.list[-1]
        self.list = self.list[:-1]
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.list[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.list) == 0
        