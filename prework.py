#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the 
#input of the function.
def hello_name(user_name):
    """Prints a message to the username in the function input"""
    print('\nhello_' + user_name.upper() + '!')

hello_name('Kelsey')

#Question 2 Write a python function, first_odds that prints the odd 
#numbers from 1-100 and returns nothing
def first_odds():
    """prints a list of the odd numbers from 1-100 and returns nothing"""
    odds = list(range(1,100,2))
    print('\n' + str(odds))
first_odds()

#Question 3 Please write a Python function, max_num_in_list to return the
#max number of a given list. 
def max_num_in_list(a_list):
    """Returns the maximum number in a given list"""
    maximum = max(a_list)
    print('\n' + str(maximum))
a_list = [1, 2, 3, 4]
max_num_in_list(a_list)

#Question 4 Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    """Given a year, tells user if it is a leap year or not"""
    if int(a_year) % 4 != 0:
        print('\n' + str(a_year) + ' is a leap year = ' + str(bool(0)))
    elif int(a_year) % 100 != 0:
        print('\n' + str(a_year) + ' is a leap year = ' + str(bool(1)))
    elif int(a_year) % 400 == 0:
        print('\n' + str(a_year) + ' is a leap year = ' + str(bool(1)))
    else:
        print('\n' + str(a_year) + ' is not a leap year')
is_leap_year(2000)
is_leap_year(2020)
is_leap_year(2018)

print('\n')

#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. 
def is_consecutive(a_list):
    """print to see if all numbers in a list are consecutive"""
    compare = list(range(min(a_list), max(a_list)+1))
    return a_list == compare

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 7, 32, 64, 1, 94]
list3 = [45, 46, 47, 48, 49, 50]
list4 = [13, 14, 15, 16, 17, 19, 20, 21, 22]
print(is_consecutive(list1))
print(is_consecutive(list2))
print(is_consecutive(list3))
print(is_consecutive(list4))