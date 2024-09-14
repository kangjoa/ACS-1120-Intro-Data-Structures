#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        # Track the number of key-value pairs in the hash table
        self.size = 0
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """
        Return a list of all keys in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        The running time is O(n) where n is the total number of key-value pairs in the hash table.
        - Why: Each key-value pair in each bucket is visited once and only once.
        - Conditions: The run time will be O(n) if the hash collisions are well-handled and if there aren't too many key-value pairs in any one bucket.
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        The running time is O(n) where n is the total number of key-value pairs in the hash table.
        - Why: Each key-value pair in each bucket is visited once and only once.
        - Conditions: The run time will be O(n) if the hash collisions are well-handled and if there aren't too many key-value pairs in any one bucket.
        """
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions?
        The running time is O(n) where n is the total number of key-value pairs in the hash table.
        - Why: Each key-value pair in each bucket is visited once and only once.
        - Conditions: The run time will be O(n) if the hash collisions are well-handled and if there aren't too many key-value pairs in any one bucket.
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(1) Why and under what conditions?
        The running time is O(1) because the size of the hash table is stored in a variable and updated in constant time.
        - Why: The size of the hash table is updated in constant time when we use the set() and delete() methods.
        - Conditions: The run time will be O(1) if the hash collisions are well-handled and if there aren't too many key-value pairs in any one bucket.
        """
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        # total_length = 0
        # for bucket in self.buckets:
        #     # bucket is an instance of a Linked List
        #     total_length += bucket.length()
        # return total_length
        return self.size

    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n) Why and under what conditions?
        - Why: In the worst case, we might have to traverse the entire linked list to find the key. 
        - Conditions: If the buckets are small and the keys are well-distributed, the run time will be O(1).
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]

        # Traverse the linked list in this bucket to find the key
        current = bucket.head
        while current is not None:
            # Unpack the key-value pair
            item_key, value = current.data
            if item_key == key:
                return True
            current = current.next

        # key not found
        return False

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(n) Why and under what conditions?
        - Why: In the worst case, we might have to traverse the entire linked list to find the key. 
        - Conditions: If the buckets are small and the keys are well-distributed, the run time will be O(1).
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        # Find the bucket where the key should be located
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]

        # Traverse the linked list in this bucket to find the key-value pair
        current = bucket.head
        previous = None
        while current is not None:
            # Unpack the key-value pair
            item_key, item_value = current.data
            # Found a match
            if item_key == key:
                if previous is None:
                    # Node to delete is the head
                    bucket.head = current.next
                else:
                    # Bypass the current node
                    previous.next = current.next

                # If the node to delete is the tail, update the tail
                if current == bucket.tail:
                    bucket.tail = previous
                return item_value
            # Move to the next node
            previous = current
            current = current.next

        # If the key is not found, raise a KeyError
        raise KeyError(f'Key not found: {key}')

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n) Why and under what conditions?
        - Why: In the worst case, we might have to traverse the entire linked list to find the key. 
        - Conditions: If the buckets are small and the keys are well-distributed, the run time will be O(1).
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]

        # Traverse the bucket to see if the key already exists
        current = bucket.head
        while current is not None:
            item_key, item_value = current.data
            if item_key == key:
                # Key found, update its value
                current.data = (key, value)
                return

            current = current.next

        # If key was not found, append the new key-value pair
        bucket.append((key, value))
        self.size += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n) Why and under what conditions?
        - Why: In the worst case, we might have to traverse the entire linked list to find the key. 
        - Conditions: If the buckets are small and the keys are well-distributed, the run time will be O(1).
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]

        current = bucket.head
        previous = None

        while current is not None:
            # Unpack the key-value pair
            item_key, item_value = current.data
            if item_key == key:
                # If we found the node, remove it
                if previous is None:
                    # Node to delete is the head
                    bucket.head = current.next
                else:
                    # Skip over the current node
                    previous.next = current.next

                # If the node to delete is the tail, update the tail
                if current == bucket.tail:
                    bucket.tail = previous

                self.size -= 1

                return  # Key found and deleted, exit the method

            # Move to the next node
            previous = current
            current = current.next

        # If we reach here, the key was not found
        raise KeyError(f'Key not found: {key}')


def test_hash_table():
    # ht = HashTable()

    # # Add data to buckets
    # bucket_1 = ht.buckets[0]
    # bucket_1.append(('I', 1))
    # bucket_1.append(('V', 5))

    # bucket_2 = ht.buckets[1]
    # bucket_2.append(('X', 10))

    # print('Manually added items to buckets')

    # # Test `keys()` method
    # print('Keys:', ht.keys())

    # # Test `values()` method
    # print('Values:', ht.values())

    # # Test `items()` method
    # print('Items:', ht.items())  # Expected: [('I', 1), ('V', 5), ('X', 10)]

    # # Test `length()` method
    # print('Length:', ht.length())  # Expected: 3

    # key = ('V', 5)
    # print(f'Contains {key}:', ht.contains(key))

    # key = ('V', 7)
    # print(f'Contains {key}:', ht.contains(key))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
