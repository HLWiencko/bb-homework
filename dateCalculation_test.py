# coding=utf-8
# If the implementation is hard to explain, it's a bad idea. 

""" Test cases for code homework problem 1: 
    Date Calculation
    The Irish lottery draw takes place twice weekly on a Wednesday and a 
    Saturday at 8pm. Write a function that calculates and returns the next 
    valid draw date based on an optional supplied date time parameter. If no 
    supplied date is provided, assume current date time.
"""

## for me: breadcrumbs for debugging
import inspect
def lineno():
    """Returns the current line number in our program."""
    return "line " + str(inspect.currentframe().f_back.f_lineno) + ": "
###

import dateCalculation
import unittest
import datetime

def stringToDate(dt):
    """ Helper function for converting dates """
    fmt = '%Y-%m-%d %I:%M %p'
    return datetime.datetime.strptime(dt, fmt)

class TestFindLotto(unittest.TestCase):
    """ Contains test cases and tests for dateCalculation.findLotto() """

    # define test cases, first in a human-readable way, then convert
    caseStrings = [ 
            # distant past
            '1886-12-20 04:16 AM', '1942-01-12 04:21 PM', 
            # In the once-a-week era
            '1989-01-01 11:04 PM', '1990-02-04 03:30 PM',
            # recent past
            '2002-07-10 10:35 AM',
            '2006-04-15 04:39 AM',
            '1997-06-24 07:06 AM',
            '2015-05-24 10:36 PM',
            '2014-01-10 12:16 PM',
            # future
            '2137-10-04 05:57 AM', 
            '2110-01-17 03:22 PM',
            '2049-12-09 01:13 AM',
            '2020-09-17 09:41 PM',
            '2039-01-21 02:18 PM',
            # Saturday night example
            '2002-08-24 08:20 PM' 
            ]

    cases = [stringToDate(i) for i in caseStrings]

    # and on to the actual tests

    def test_findLottoIsAfterDateSupplied(self):
        """ findLotto() should return a date on or after the date supplied """
        for case in self.cases:
            res = dateCalculation.findLotto(case)
            self.assertTrue(res >= case.date())

    def test_findLottoIsWednesdayOrSaturday(self):
        """ findLotto() should return a date that is a Wednesday or Saturday """
        acceptableDays = [2, 5] # datetime is zero-indexed starting on Monday
        for case in self.cases:
            res = dateCalculation.findLotto(case)
            self.assertTrue(res.weekday() in acceptableDays)

    def test_findLottoSameDay(self):
        """ findLotto() should return today's date if it's a Saturday before 8 """
        for case in self.cases:
            if (case.hour < 20 and case.weekday() == 5):
                res = dateCalculation.findLotto(case)
                self.assertEqual(res, case.date())

    def test_findLottoJustMissedIt(self):
        """ findLotto() should not return same day if lotto draw has happened """
        for case in self.cases:
            if case.hour >= 20:
                res = dateCalculation.findLotto(case)
                self.assertTrue(res > case.date())

    def test_findLottoHistorialNoLotto(self):
        """ findLotto() should not return a date before Saturday 16 April 1988 """
        firstLotto = datetime.datetime(1988, 4, 16, 20) 
        for case in self.cases:
            if case < firstLotto:
                res = dateCalculation.findLotto(case)
                self.assertEqual(res, firstLotto.date())

    def test_findLottoHistoricalSaturdaysOnly(self):
        """ findLotto() should only return Saturdays before 30 May 1990 """
        for case in self.cases:
            if case < datetime.datetime(1990, 5, 26, 20): # last Sat-only draw
                res = dateCalculation.findLotto(case)
                self.assertEqual(res.weekday(), 5)

    def test_findLottoNonDatetimeInput(self):
        """ findLotto() should raise a TypeError if input is not a datetime """
        bad = ['donkey', 42, datetime.date.today(), None]
        for case in bad:
            self.assertRaises(TypeError, dateCalculation.findLotto, case)

if __name__ == '__main__':
    unittest.main()
