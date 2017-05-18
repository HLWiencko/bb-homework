# coding=utf-8
# Readability counts. 

""" Code homework problem 2:
    Implement a least recently used (LRU) cache mechanism using a 
    decorator and demonstrate it use in a small script. The LRU 
    must be able to admit a ‘max_size’ parameter that by default 
    has to be 100.
"""

## for me: breadcrumbs for debugging
import inspect
def lineno():
    """Returns the current line number in our program."""
    return "line " + str(inspect.currentframe().f_back.f_lineno) + ": "
###

import functools
import sys

class LruCache(object):
    """ Decorator that caches a function's return values up to max_size """

    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {} # args : node
        self.queue = CircularDoublyLinkedList()

    def isFull(self):
        if len(self.cache) == self.max_size:
            return True
        return False

    def clear(self):
        self.cache.clear()
        self.queue = CircularDoublyLinkedList()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            inStuff = tuple((k, kwargs[k]) for k in sorted(kwargs.keys()))
            key = (args, inStuff)
            if key in self.cache:
                self.queue.promote(self.cache[key])
                return self.cache[key].value[1]

            # truncate the cache if it's full
            if self.isFull():
                del self.cache[self.queue.pop()[0]]

            val = func(*args, **kwargs)
            self.cache[key] = self.queue.insert((key, val))
            return val

        wrapper.cache = self.cache
        wrapper.max_size = self.max_size
        wrapper.queue = self.queue
        wrapper.clear = self.clear
        return functools.update_wrapper(wrapper, func)

class Node(object):
    """ Node object for our doubly linked list """
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode
    def __str__(self):
        return repr(self.value)
    def showLinks(self):
        ret = ''
        if self.prevNode is not None:
            ret += '{} '.format(self.prevNode.value)
        ret += '-> {} ->'.format(self.value)
        if self.nextNode is not None:
            ret += ' {}'. format(self.nextNode.value)
        return ret

class CircularDoublyLinkedList(object):
    """ Doubly linked list with defined root node as the 'head' """
    def __init__(self):
        self.root = None
        self.size = 0

    def asList(self):
        """ Returns the values in order as a list """
        ret = []
        if self.root == None:
            return ret
        n = self.root
        while n.nextNode is not self.root:
            ret.append(n.value)
            n = n.nextNode
        ret.append(n.value)
        return ret

    def insertNode(self, node):
        """ Inserts given node at the head position """
        if self.root == None:
            node.nextNode = node
            node.prevNode = node
        else:
            node.prevNode = self.root.prevNode
            node.nextNode = self.root
            self.root.prevNode.nextNode = node
            self.root.prevNode = node
        self.root = node

    def insert(self, value):
        """ Creates node and inserts at the head position, returns the node. """
        new = Node(value)
        self.insertNode(new)
        self.size += 1
        return new

    def promote(self, node):
        """ Promotes given node to the head  """
        # stich the adjoining nodes together
        node.prevNode.nextNode = node.nextNode
        node.nextNode.prevNode = node.prevNode
        # put our node at the head
        self.insertNode(node)

    def pop(self):
        """ Removes the last node, returns its value """
        toRemove = self.root.prevNode
        toRemove.prevNode.nextNode = self.root
        self.root.prevNode = toRemove.prevNode
        self.size -= 1
        return toRemove.value

if __name__ == '__main__':
    """ Demonstrate LRU cache implementation 
        Run without arguments to display help message. """

    if len(sys.argv) != 2:
        print("\nSupply desired cache size, e.g.: 'python cache.py 5'\nThe demo prints out the contents of the cache, so you may want to start small.\n")
        sys.exit()
    cacheSize = int(sys.argv[1])

    @LruCache(max_size=cacheSize)
    def add(x, y):
        return x + y

    def demo(i):
        print("Adding {} and {} -> {}".format(i, i+1, add(i, i+1)))
        print("Cache size is {}".format(len(add.cache)))
        stuff = ["{} -> {}".format(k[0], v) for k, v in add.cache.items()]
        print("Cache contains {}".format(stuff))
        print()

    print("Cache size is set to {}".format(cacheSize))
    print()

    for i in range(1, 3):
        demo(i)

    if int(cacheSize) > 2:
        print("...carry on...")
        print()

    for i in range(3, cacheSize+3):
        add(i, i+1)
    
    for i in range(cacheSize+3, cacheSize+5):
        demo(i)

    print("Now clear the cache: ")
    add.clear()
    print("Cache size is {}".format(len(add.cache)))
    stuff = ["{} -> {}".format(k[0], v) for k, v in add.cache.items()]
    print("Cache contains {}\n".format(stuff))

    print("Thanks for your time!\n")


###############

""" 
Alternatively, you could also just:

    from functools import lru_cache

    @lru_cache(max_size=100)
    def myFunction(x, y):
        doStuff()

...and move on with your life.

"""

