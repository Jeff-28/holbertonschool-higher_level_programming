#!/usr/bin/python3
"""
Singly Linked List Module:
    creates and defines nodes for a singly linked list.
"""


class Node:
    """Node class - creates nodes and defines them by data, and the location
    of the next node in the list."""

    def __init__(self, data, next_node=None):
        """Takes data and the next_node address as parameters."""
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Returns the attribute data."""
            return (self.__data)

        @data.setter
        def data(self, value):
            """Defines the attribute data."""
            if type(data) != int:
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Returns the address of the next node."""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, next_node):
            """Defines the address of the next node."""
            if next_node is not None and type(next_node) != Node:
                raise TypeError("next_node must be a Node object")
            self.__next_node = next_node

        def __str__(self):
            """Returns the node's data as string."""
            return str(self.data)


class SinglyLinkedList:
    """SinglyLinkedList class - defines and modifies a singly linked list."""

    def __init__(self):
        """Initializes the list empty."""
        self.__head = None

    def __str__(self):
        """Returns a list of nodes."""
        temp = self.__head
        nodes_list = []
        while temp:
            nodes_list.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(nodes_list))

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position of the list."""
        temp = self.__head
        if type(value) is not int:
            raise TypeError("data must be an integer")
        if temp is None:
            self.__head = Node(value)
            return
        elif value < temp.data:
            self.__head = Node(value, temp)
            return
        while temp:
            if not temp.next_node:
                temp.next_node = Node(value)
                break
            if value < temp.next_node.data:
                temp.next_node = Node(value, temp.next_node)
                break
            temp = temp.next_node
