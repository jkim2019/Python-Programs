import datetime

def calcYear(curAge):
    '''
        pre: curAge is an int
        post: returns year in which person becomes 100
    '''
    now = datetime.datetime.now()
    return now.year + (100 - curAge)

def queryDetails():
    '''
        queries user for name and age
    '''
    myName = input('Enter your name: ')
    curAge = input('Enter your current age: ')
    while curAge <= 0 or type(curAge) != int:
        print 'please input a valid age'
        curAge =  input('Enter your current age: ')

    year = calcYear(curAge)
    repeatAns(myName, year)

# additional specifications

def repeatAns(name, year):
    '''
        pre: year is a number
        queries user for a number and repeats message n times
    '''

    numRepeat = input('Enter the number of times you would like me to repeat myself: ')
    while numRepeat > 0:
        print "%s will turn 100 years old in the year %d." % (name, year)
        numRepeat -= 1

queryDetails()
