'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
import argparse


def problem1():
    name = raw_input("Enter name: ")
    age  = raw_input("Enter age: ")

    assert name.isalpha(), "Invalid name given!"
    assert int(age), "Invalid age entry!"
    
    if int(age) > 100:
        print "Hi {}\n\tYou turned 100 in year {}"

    from datetime import datetime
    curr_year    = datetime.now().year

    years_to_100 = curr_year + (100 - int(age))
    print "Hi {}\n\tIn the year {} you will be 100 years old".format(name, years_to_100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--code', default=1, type=int, help='Code to run')
    args = parser.parse_args()
    if args.code:
        arg = ''
        func_name = 'problem' + str(args.code) + '(' + arg + ')'
        exec(func_name)
    else:
        print "Did not receive arguments indicating which code to run"
