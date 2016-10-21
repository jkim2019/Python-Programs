
def oddOrEven():
    '''
        prompts user for an integer
        determines whether integer is odd or even, and outputs appropriate response
    '''

    # method 1: assume user enters an int. Otherwise throw exception.
    # num = int(input("Enter a number: "))

    # method 2: does not assume type. Repeatedly queries user for valid arg if
    # not supplied.
    # additional specification: print a different message if divisible by 4
    num = input("Enter an integer: ")

    # raw_input accepts input as string. input reads as expression
    while type(num) != int:
        num = input("Please enter a valid integer")

    if num % 4 == 0:
        print "fun fact - %d is divisible by 4!" % num
    if num % 2 == 0:
        print "%d is an even number." % num
    else:
        print "%d is an odd number." % num
