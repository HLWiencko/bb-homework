# coding=utf-8
# Complicated is better than complex. 

""" Code homework problem 1: 
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

import datetime

def findLotto(d=''):
    """ Calculate and return the next valid Irish Lotto draw date. 
        d = datetime object (optional, default value is current date/time) """
    
    # set default date/time
    if d == '':
        d = datetime.datetime.now()
    else:
        if not isinstance(d, datetime.datetime):
            raise TypeError('{} is not a datetime.datetime object'.format(type(d)))

    # after 19:59 you've missed today's draw, it's essentially tomorrow
    if d.hour > 19: 
        d += datetime.timedelta(days=1)

    # Historical case handling
    firstLotto = datetime.datetime(1988, 4, 16, 20) 
    if d < firstLotto: # before the first lottery, the 'next draw' is fixed
        return firstLotto.date()
    lastSaturdayLotto = datetime.datetime(1990, 5, 26, 20) # last Sat-only draw
    if firstLotto < d < lastSaturdayLotto: # Saturdays only between 1988 and 1990
        return nextWeekday(d, 5).date()

    # Everything else
    acceptableDays = [2, 5] # Wednesday, Saturday
    if d.weekday() in acceptableDays:
        return d.date()
    else:
        nextWed = nextWeekday(d, 2)
        nextSat = nextWeekday(d, 5)
        return min(nextWed, nextSat).date()

def nextWeekday(d, weekday):
    """ Returns the next weekday after date d
	0 = Monday, 1 = Tuesday... """
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

if __name__ == '__main__':
    """ Demonstrate Lottery Finder implementation. """

    inputDate = ''
    while(inputDate == ''):
        prompt = "Please enter a date in YYYY-MM-DD format [today]:\n> "
        fromUser = input(prompt)

        if fromUser == '':
            inputDate = datetime.datetime.now()
        else:
            try: 
               inputDate = datetime.datetime.strptime(fromUser, '%Y-%m-%d')
            except ValueError:
                print("Input didn't make sense, please try again.")

    outFormat = '%A %d %B %Y'
    inDateString = datetime.datetime.strftime(inputDate, outFormat)
    outDateString = datetime.datetime.strftime(findLotto(inputDate), outFormat)
    print("The next lottery draw after {} is {}.".format(inDateString, outDateString))

