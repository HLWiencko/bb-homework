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
from collections import OrderedDict

class LruCache(object):
    """ Decorator that caches a function's return values up to max_size """

    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = OrderedDict()

    def clear(self):
        self.cache.clear()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            processedArgs = tuple((k, kwargs[k]) for k in sorted(kwargs.keys()))
            key = (args, processedArgs)
            if key in self.cache:
                val = self.cache[key]
                del self.cache[key]
                self.cache[key] = val
                return val

            # trim the cache if it's full
            if len(self.cache) == self.max_size:
                self.cache.popitem(last=False)

            val = func(*args, **kwargs)
            self.cache[key] = val
            return val

        wrapper.cache = self.cache
        wrapper.max_size = self.max_size
        wrapper.clear = self.clear
        return functools.update_wrapper(wrapper, func)

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

