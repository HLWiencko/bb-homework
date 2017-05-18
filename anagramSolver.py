# coding=utf-8
# Errors should never pass silently. 

""" Code homework problem 3:
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

import os

def findAnagram(source, options):
    """ Takes a source string and a list/tuple of options and returns a list of 
        anagrams of the source from the options. """

    # The spec specified types, so check that here. 
    if not isinstance(source, str):
        raise TypeError('{} is not a string'.format(type(source)))
    for item in options: # will throw a TypeError if not iterable
        if not isinstance(item, str):
            raise TypeError('{} in options is not a string'.format(type(item)))

    ret = []

    sortedSource = "".join(sorted(source))
    
    for s in options:
        if "".join(sorted(s)) == sortedSource:
            ret.append(s)

    return [i for i in ret if i != source]

if __name__ == '__main__':
    """ Demonstrate anagram solver implementation. """

    inOptions = []
    inTarget = ''

    while(inTarget == ''):
        inTarget = input("Please enter a word to anagram-ise:\n> ")

    inFile = input("Please enter a filename containing options, one per line:\n> ")
    if not os.path.isfile(inFile.strip()):
        if inFile != '':
            print("{} not found.".format(inFile))
        print("Using default values from anagramSolverWordList.txt")
        inFile = 'anagramSolverWordList.txt'
    with open(inFile, 'r') as f:
        for line in f.readlines():
            inOptions.append(line.strip())

    print('Anagrams for "{}" from a list of {} options include:'.format(inTarget, len(inOptions)))

    print(findAnagram(inTarget, inOptions))
