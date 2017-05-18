# coding=utf-8
# Namespaces are one honking great idea -- let's do more of those!

""" Test cases for code homework problem 2: 
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

import cache
import unittest

def makeAndPopulateCdll(size=5):
    """ Helper function for cdll test class """
    cdll = cache.CircularDoublyLinkedList()
    for i in range(1, size+1):
        cdll.insert(i)
    return cdll

class TestCircularDoublyLinkedList(unittest.TestCase):
    """ Test cases for CircularDoublyLinkedList class """

    def test_cdllAddResetHead(self):
        """ Node.insert() should reset the head """
        cdll = makeAndPopulateCdll()
        self.assertEqual(cdll.root.value, 5)
    def test_cdllAddChangeSize(self):
        """ Node.insert() should change the size of the list """
        cdll = makeAndPopulateCdll()
        self.assertEqual(cdll.size, 5)

    def test_cdllPromoteResetHead(self):
        """ Node.promote() should reset the head """
        cdll = makeAndPopulateCdll()
        promotedValue = cdll.root.nextNode.value
        cdll.promote(cdll.root.nextNode)
        self.assertEqual(cdll.root.value, promotedValue)
    def test_cdllPromoteKeepSize(self):
        """ Node.promote() should NOT change the size of the list """
        cdll = makeAndPopulateCdll()
        cdll.promote(cdll.root.nextNode)
        self.assertEqual(cdll.size, 5)

    def test_cdllGetSize(self):
        """ Node.size should report the actual size of the list """
        cdll = makeAndPopulateCdll()
        self.assertEqual(cdll.size, 5)
    def test_cdllAsList(self):
        """ Node.asList should also report the actual size of the list """
        cdll = makeAndPopulateCdll()
        self.assertEqual(cdll.size, len(cdll.asList()))

    def test_cdllPopChangeSize(self):
        """ Node.pop() should decrease the size of the list by 1 """
        cdll = makeAndPopulateCdll(5)
        cdll.pop()
        self.assertEqual(cdll.size, 4)
    def test_cdllPopKeepHead(self):
        """ Node.pop() should not change the head """
        cdll = makeAndPopulateCdll(5)
        head = cdll.root
        cdll.pop()
        self.assertEqual(cdll.root, head)

class TestLruCache(unittest.TestCase):
    """ Test cases for LruCache decorator """

    def test_lruCacheReturnsCachedItem(self):
        """ lruCache() should return an item if it's in the cache """
        @cache.LruCache()
        def add(x, y):
            return x + y
        add(1, 2)
        self.assertEqual(3, add(1, 2))

    def test_lruCacheActuallyCaches(self):
        """ lruCache() should store the item properly """
        @cache.LruCache(max_size=2)
        def add(x, y):
            return x + y
        add(1, 2)
        # is the value there? 
        self.assertTrue(3 in [v.value[1] for v in add.cache.values()])
        # is the key there? 
        self.assertTrue((1,2) in [i[0] for i in add.cache.keys()])

    def test_lruCacheMaintainsSize(self):
        """ lruCache() should not grow beyond its given size """
        @cache.LruCache(max_size=2)
        def add(x, y):
            return x + y
        for i in range(1, 5):
            add(i, i+1)
            self.assertTrue(add.queue.size < 3)
            self.assertTrue(len(add.cache) < 3)

    def test_lruCacheClears(self):
        """ lruCache.clear() should clear the cache """
        @cache.LruCache(max_size=2)
        def add(x, y):
            return x + y
        add(1, 3)
        self.assertEqual(len(add.cache), 1)
        add.clear()
        self.assertEqual(len(add.cache), 0)

    def test_lruCachePromotes(self):
        """ lruCache() should promote a node if it's found in the cache """
        @cache.LruCache(max_size=2)
        def add(x, y):
            return x + y
        add(1, 3)
        add(1, 4)
        add(1, 5)
        add(1, 4)
        self.assertEqual(add.queue.asList()[0][0][0], (1, 4))


if __name__ == '__main__':
    unittest.main()
