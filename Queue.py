class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return self.items == []


"""A simple implementation of the Stack ADT.

Author: Francois Pitt, January 2013,
        Danny Heap, September 2013, 2014
        Dan Zingaro, January 2016
"""


class Stack:

    """A collection of items stored in 'last-in, first-out' (LIFO) order.
    Items can have any type.

    Supports standard operations: push, pop, is_empty.
    """

    def __init__(self: 'Stack') -> None:
        """
        Initialize this stack.

        >>> isinstance(Stack(), Stack)
        True
        """
        self._items = []

    def push(self: 'Stack', item: object) -> None:

        """
        Add item to the top of this stack.

        >>> s = Stack()
        >>> s.push(7)
        >>> s.pop()
        7
        """
        self._items.append(item)

    def pop(self: 'Stack') -> object:
        """
        Remove and return the top item on this stack.

        >>> s = Stack()
        >>> s.push(7)
        >>> s.pop()
        7
        """
        return self._items.pop()

    def is_empty(self: 'Stack') -> bool:

        """
        Return True iff this stack is empty.

        >>> Stack().is_empty
        True
        """

        return self._items == []