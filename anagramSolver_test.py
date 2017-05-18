# coding=utf-8
# If the implementation is easy to explain, it may be a good idea.

""" Test cases for code homework problem 3: 
    Write a function that accepts a word (string) and a list of words (list or 
    tuple of strings) and return back a list with the valid anagrams for
    the word inside the given words list.
"""

## for me: breadcrumbs for debugging
import inspect
def lineno():
    """Returns the current line number in our program."""
    return "line " + str(inspect.currentframe().f_back.f_lineno) + ": "
###

import anagramSolver
import unittest

class TestFindAnagram(unittest.TestCase):

    # define test cases

    optionsTuple = ('parties', 'party', 'shindig', 
            'pastier', 'greyer', 'stickier', 
            'pirates', 'ninjas', 'kittens', 
            'traipse', 'mosey', 'sashay',
            'thing')
    optionsList = list(optionsTuple)
    validResults = {
            'night' : ['thing'],    
            'parties' : ['pastier', 'pirates', 'traipse'], 
            'ninjas' : [], # self is in options list, should not be returned
            'lolcats' : [],  # no results
            }
                

    # and on to the actual tests

    def test_findAnagramReturnsSolutionsForListInput(self):
        """ findAnagram() should return all valid anagrams when given a list """
        for k, v in self.validResults.items():
            self.assertEqual(v, anagramSolver.findAnagram(k, self.optionsList))

    def test_findAnagramReturnsSolutionsForTupleInput(self):
        """ findAnagram() should return all valid anagrams when given a tuple """
        for k, v in self.validResults.items():
            self.assertEqual(v, anagramSolver.findAnagram(k, self.optionsTuple))

    def test_findAnagramReturnsSelf(self):
        """ findAnagram() should not return the input string """
        self.assertEqual([], anagramSolver.findAnagram('ninja', self.optionsTuple))

    def test_findAnagramReturnsOptionFromList(self):
        """ findAnagram() should not return a string not in the options """
        for case in self.validResults.keys():
            for s in anagramSolver.findAnagram(case, self.optionsTuple):
                self.assertTrue(s in self.optionsTuple)

    def test_findAnagramBadInType(self):
        bad = [1, ['horse', 'donkey', 42], (1, 2, 3)]
        for case in bad:
            self.assertRaises(TypeError, anagramSolver.findAnagram, case)

    def test_findAnagramNoInput(self):
        self.assertRaises(TypeError, anagramSolver.findAnagram)

if __name__ == '__main__':
    unittest.main()
