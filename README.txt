Code homework for Senior Python Developer role
16 May 2017
Heather Wiencko
heather.l.wiencko@gmail.com

Introduction
------------

    Each solution is contained in two python files: solution.py and 
    solution_test.py. They are written and tested for python 3.6, and
    only modules from the standard library are used. 

    Tests use the unittest library, and can be run like this:
    $ python solution_test.py


Problem 1
---------

    "The Irish lottery draw takes place twice weekly on a Wednesday and a 
    Saturday at 8pm. Write a function that calculates and returns the next 
    valid draw date based on an optional supplied date time parameter. If no 
    supplied date is provided, assume current date time."

    Solution and tests:
        dateCalculation.py
        dateCalculation_test.py

    A demo can be run from the command line:
    $ python3 dateCalculation.py 

Problem 2
---------

    "Implement a least recently used (LRU) cache mechanism using a 
    decorator and demonstrate it use in a small script. The LRU 
    must be able to admit a ‘max_size’ parameter that by default 
    has to be 100."

    Solution and tests:
        cache.py
        cache_test.py

    A demo can be run from the command line:
    $ python3 cache.py [cacheSize]


Problem 3
---------

    "Write a function that accepts a word (string) and a list of words (list or 
    tuple of strings) and return back a list with the valid anagrams for
    the word inside the given words list."

    Solution and tests:
        anagramSolver.py
        anagramSolver_test.py

    A demo can be run from the command line, and may use the file 
    anagramSolverWordList.txt included in this tarball:
    $ python3 anagramSolver.py 
