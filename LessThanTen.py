# File name: LessThanTen.py
# Author: John Kim
# Email: john.j.kim@vanderbilt.edu
# Description: Single function .py which accepts a list of ints and returns a list of ints less than 10
# Last Changed: 10/21/16

def lessThanTen(intList):
    '''
    accepts a list of type int and returns a list of ints less than 10
    :param intList: list of type int
    :return: list of int less than 10
    '''
    return [i for i in intList if i < 10]

def altLessThanTen():
    '''
    queries user to enter a list of ints, one int at a time. Prints out list
    '''

    num = 0
    myList = []

    print "Type 'finished' when done."
    num = raw_input("Enter a number: ")

    while num != "finished":
        # if we enter this loop, we can safely assume num is of type int
        num = int(num)
        myList.append(num) if num < 10 else 0
        num = raw_input("Enter another number: ")

    print "Your list: {0}".format(str(myList))

def alt2LessThanTen():
    '''
    queries user to enter whole list of ints.
    '''

    myList = raw_input("Enter a list. Formatting: [#,#,...,#]: ")
    myList = map(int, myList[1:-1].split(','))
    print str(lessThanTen(myList))

def main():
    # lessThanTen()
    # altLessThanTen()
    alt2LessThanTen()

if __name__ == "__main__":
    main()