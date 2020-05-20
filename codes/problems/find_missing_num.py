'''
Given an array of size n-1 and given that there are numbers from 1 to n with one missing, the missing number is to be found.

Input:

    The first line of input contains an integer T denoting the number of test cases.
    The first line of each test case is N.
    The second line of each test case contains N-1 input C[i],numbers in array.

Output:

    Print the missing number in array.

Constraints:

    1 <= T <= 200
    1 <= N <= 1000
    1 <= C[i] <= 1000

Example:

  Input
    2
    5
    1 2 3 5
    10
    1 2 3 4 5 6 7 8 10

  Output
    4
    9
'''


import random

# Take input from user for number of tests
T = raw_input("Enter a number denoting the number of test cases. Constraints (1<=T<=200) T = ")

if 1<=int(T)<=200:
    for test in range(int(T)):
        # Take input of user for array length
        N = raw_input("Enter a number. Constraints (1<=N<=1000) N = ")

        if 1<=int(N)<=1000:
            # Construct an array of given length
            given_array = []
            for i in range(1, int(N)+1):
                given_array.append(i)

            # Remove an element from the array at random
            index = random.randint(1, int(N)-1)
            given_array.pop(index)
            print "Array to find missing element from: {}".format(given_array)

            # Find the missing element
            previous_elem = 0
            missing_elem = 0
            while missing_elem == 0:
                for elem in given_array:
                    if elem-1 == previous_elem:
                        previous_elem += 1
                    else:
                        missing_elem = elem - 1
                        break
            print "Missing element in the array is {}".format(missing_elem)
        else:
            print "Entered value of N is not within the specified range!"
else:
    print "Entered value of T is not within the specified range!"
