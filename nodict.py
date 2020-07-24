#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Cory, and after hours group'


class Node:
    """A container that stores key value in a hashtable"""
    def __init__(self, key, value=None):
        """The init method that takes a key and a value required"""
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """Returns a string in Repr"""
        return f'{self.__class__.__name__}{self.key}, {self.value}'

    def __eq__(self, other):
        """This method allows the key value to be compared"""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """If number of buckets didn't provide, it will be defult to 10"""
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets
    
    def __repr__(self):
        """Return a string representing the NoDic contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate
        (self.buckets)])

    def add(self, key, value=None):
        """It accepts key and value and creates a new_node and stores in a bucket"""
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)
        

    def get(self, key):
        """Accepts just one parameter, if key doesn't exist it will raise an error"""
        key_value = Node(key)
        bucket = self.buckets[key_value.hash % self.size]
        for kv in bucket:
            if kv == key_value:
                return kv.value
        raise KeyError(f'{key} not found')


    def __getitem__(self, key):
        """A method that allows the use of square-bracket notation to look up a value"""
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """Method that allows to use square-bracket notation to set the value of the key"""    
        self.add(key, value)
