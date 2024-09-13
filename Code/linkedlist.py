#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?
        O(n) because the runtime is directly proportional to the input size (number of nodes in the linked list). We need to visit each node exactly once, so if we double the input size, we double the time to visit each node (aka traverse the list).
        """
        # TODO: Loop through all nodes and count one for each
        count = 0
        current = self.head

        while current is not None:
            count += 1

            # move pointer to next node (stay inside LL class)
            current = current.next

        return count

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        O(1) because appending to the tail of the linked list takes constant time. We have direct access to the tail node, so no traversal is needed (we do not need to visit each node), and the time to insert the new node is the same, no matter the list length.
        """
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        # TODO: Else append node after tail
        else:
            # Take the current tail node and set its next to the new node and then set the tail to the new node
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        O(1) because prepending to the head of the linked list takes constant time. We have direct access to the head node, so no traversal is needed (we do not need to visit each node), and the time to insert the new node is the same, no matter the list length.
        """
        # TODO: Create new node to hold given item
        new_node = Node(item)

        # Store the current head
        current = self.head

        # TODO: Prepend node before head, if it exists
        if self.head is not None:
            # Make the new node the head of the list
            self.head = new_node
            # Link the new head's pointer to the old head so we don't lose it
            self.head.next = current
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, matcher):
        """
        Return an item from this linked list if it is present.
        TODO: Best case running time: O(1) Why and under what conditions?
        The best case running time is if we find the matcher in the first node (the head). Then we get to exit early and do not have to visit each node in the linked list.
        TODO: Worst case running time: O(n) Why and under what conditions?
        The worst case running time is if the matcher is at the end of the linked list (the tail) or not found because we have to visit each node and traverse through the whole linked list.

        Args:
            matcher (function): A function that takes an item as input and returns True if the item matches, False if there is no match.
        """
        # TODO: Loop through all nodes to find item, if present return True otherwise False

        # Below works and passed GS tests but doesn't treat matcher as a function (does not pass the lambda unit test)
        current = self.head

        while current is not None:
            if current.data == matcher:
                return True

            # move pointer to next node (stay inside LL class)
            current = current.next

        return False

        # This version passed unit tests and treats matcher as a function, but doesn't pass GS tests
        # current = self.head

        # while current is not None:
        #     if matcher(current.data):
        #         return current.data

        #     # move pointer to next node (stay inside LL class)
        #     current = current.next

        # return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
        The best case is if the item to delete is the first node in the linked list. Then we only have to update the head.
        TODO: Worst case running time: O(n) Why and under what conditions?
        The worst case is if the item to delete is at the end of the list or not in the list. Then we have to visit each node in the list.
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        # Is the list empty?
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        # Start with first node (head) as current
        current = self.head

        # There is no previous node to the first, so it's None
        previous = None

        # Case: when the item is also the head
        if item == self.head.data:
            self.head = self.head.next
            # If the list becomes empty after deleting the head, update the tail
            if self.head is None:
                self.tail = None
            return

        while current is not None:
            if current.data == item:
                # Delete the node by updating the previous node's next pointer to skip over the current node
                previous.next = current.next
                # If the current node is the tail, update the tail to the previous node
                if current == self.tail:
                    self.tail = previous
                return
            previous = current
            current = current.next

        # Case: when the item is not found.
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    # print("######################################################")
    # Initialize a linked list with values
    # ll = LinkedList(['D', 'E', 'F', 'G'])
    # ll = LinkedList(['Z', 'Y'])

    # print(f"print ll: {ll}")

    # # Check the length of the list
    # print('Length:', ll.length())
    # print('should be 4')

    # prepend a value
    # ll.prepend('C')
    # print('prepend C:', ll)

    # # find
    # matcher = 'F'
    # result = ll.find(matcher)
    # print(result)
    # print("Should be True")

    # matcher_2 = "$"
    # result = ll.find(matcher_2)
    # print(result)
    # print("Should be False")

    # # Initialize a linked list with values
    # short_ll = LinkedList(['D'])
    # matcher_3 = 'D'
    # result = short_ll.find(matcher_3)

    # print(result)

    # delete
    ll = LinkedList(['D', 'E', 'F'])
    ll.delete('F')
    print(ll)

    # delete
    # ll = LinkedList(['D', 'E', 'F', 'G'])
    # item = 'E'
    # result = ll.delete(item)
    # print(ll)

    # ll_2 = LinkedList(['D', 'E', 'F', 'G'])
    # item = "D"
    # result = ll_2.delete(item)
    # print(ll_2)

    # try:
    #     ll_2.delete('Z')
    # except ValueError as e:
    #     print(e)

    # ll = LinkedList(['B', 'C'])
    # ll.delete('C')
    # print(ll)

    # ll = LinkedList(['A'])
    # ll.delete('A')
    # print(ll)

    # print("######################################################")

    # ll = LinkedList()
    # print('list: {}'.format(ll))
    # print('\nTesting append:')
    # for item in ['A', 'B', 'C']:
    #     print('append({!r})'.format(item))
    #     ll.append(item)
    #     print('list: {}'.format(ll))

    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('length: {}'.format(ll.length()))

    # # Enable this after implementing delete method
    # delete_implemented = True
    # if delete_implemented:
    #     print('\nTesting delete:')
    #     for item in ['B', 'C', 'A']:
    #         print('delete({!r})'.format(item))
    #         ll.delete(item)
    #         print('list: {}'.format(ll))

    #     print('head: {}'.format(ll.head))
    #     print('tail: {}'.format(ll.tail))
    #     print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
