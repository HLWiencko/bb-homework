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
        self.assertTrue(3 in [v for v in add.cache.values()])
        # is the key there? 
        self.assertTrue((1,2) in [i[0] for i in add.cache.keys()])

    def test_lruCacheMaintainsSize(self):
        """ lruCache() should not grow beyond its given size """
        @cache.LruCache(max_size=2)
        def add(x, y):
            return x + y
        for i in range(1, 5):
            add(i, i+1)
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
        self.assertEqual(list(add.cache.items())[-1][0][0], (1, 4))

if __name__ == '__main__':
    unittest.main()
