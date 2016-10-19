import datetime

def calcYear(curAge):
    '''
        pre: curAge is an int
        post: return year in which person becomes 100
    '''
    now = datetime.datetime.now()
    return now.year + (100 - curAge)

def queryAge():
    '''
        query user for age and print when person becomes 100
    '''

    curAge = input('Enter your current age: ')
    while curAge <= 0:
        print 'please input a valid age'
        curAge =  input('Enter your current age: ')

    print 'You will turn 100 in the year %d' % calcYear(curAge)

queryAge()
