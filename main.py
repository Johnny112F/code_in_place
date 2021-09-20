import tkinter

import numpy as np

"""This program will take in an input from the user which will either be an 
addition, subtraction, multiplication, or division equation. 
The user will have the option to see examples from the Egyptian, Russian, 
or modern computing perspective of how this problem would be solved according to 
principles from the selected system."""


def detect_type(user):
    if "*" in user:
        print("You have entered a multiplication problem.")
    elif "/" in user:
        print("You have entered a division problem.")
    elif "+" in user:
        print("You have entered an addition problem.")
    elif "-" in user:
        print("You have entered a subtraction problem.")
    else:
        print("The type of math you have entered is not yet supported by this program.")


def pick_style():
    print('')
    print("Please enter what mathematical system you would like to use for your equation solution.")
    print("The styles are Egyptian, Russian Peasant, and Modern Computing")
    style = ['Egyptian', 'Russian Peasant', 'Modern Computing']
    choice = input()
    if choice in style:
        print("You have chosen to utilize the " + choice + " system.")

    return choice

def order_numbers(user):
    new = user.split("*", 2)
    numeral_one = (new[0])
    numeral_two = (new[1])
    numeral_one = int(numeral_one)
    numeral_two = int(numeral_two)

    if numeral_one < numeral_two:
        small_num = numeral_one
        big_num = numeral_two

        print((str(numeral_two)) + " is the bigger number, so we will divide it by two without saving the remainder till we have 1 as a result")

        print((str(numeral_one)) + " is the smaller number so we will multiply it by two till the number of multiplicands matches the number of results created by dividing the larger number.")
        return big_num, small_num

    else:
        big_num = numeral_one
        small_num = numeral_two

        print((str(numeral_one)) + " is the bigger number, so we will divide it by two without saving the remainder till we have 1 as a result")

        print((str(numeral_two)) + " is the smaller number so we will multiply it by two till the number of multiplicands matches the number of results created by dividing the larger number.")

        return big_num, small_num


def divide_larger(big_num):

    count = 0
    while big_num != 1:
        result = int(big_num) // 2
        print(result)
        count += 1
        big_num = result
        if big_num == 1:
            print("The bigger number was divided " + str(count) + " times to reach 1.")


    return count

def mult_smaller(small_num, count):
    print("We will now multiply the smaller number by two " + str(count) + " times.")
    time = 0
    print(small_num)
    while time != count:
        result = small_num * 2
        print(result)
        time += 1
        small_num = result



def division_list(big_num):
    list = []
    list.append(big_num)
    while big_num != 1:
        result = int(big_num) // 2
        list.append(result)
        big_num = result
    return list


def mult_list(small_num, count):
    mult = []
    mult.append(small_num)
    time = 0
    while time != count:
        result = small_num * 2
        mult.append(result)
        time += 1
        small_num = result
    return mult

def odd_list(ld):
    odd = []
    for i in range(len(ld)):

        element = ld[i]
        if element % 2 != 0:
            odd.append(i)
    return odd

def mult_two(small_num):
    print("We will first start with 1 and then find powers of two till we've created a list where the largest power will either be 1 or 2 less "
          "than the small number in our equation.")
    num = 1
    res = 1
    count = 0
    print(num)
    while num < small_num:
        num = res * 2
        count += 1
        if num > small_num:
            #count = count
            break
        print(num)
        res = num


def mult_big(big_num, count):
    print("We will now multiply the bigger number by two till the length of our list is that of our small number.")
    time = 0
    print(big_num)
    while time != (count-1):
        result = big_num * 2
        print(result)
        time += 1
        big_num = result
    
    

def mult_liste(big_num, count):

    time = 0
    list = []
    list.append(big_num)
    while time != (count - 1):
        result = big_num * 2
        list.append(result)
        time += 1
        big_num = result


    return list

def mult_listb(small_num):
    print('Our list of powers of two with one at the beginning whose greatest exponent is below the smaller number in the equation is below.')
    num = 1
    res = 1
    count = 0
    list = []
    list.append(num)
    while num < small_num:
        num = res * 2
        count += 1
        if num >= small_num:
            # count = count
            break
        list.append(num)
        res = num
    return list

def mult_listc(small_num):

    num = 1
    res = 1
    count = 0
    list = []
    list.append(num)
    while num < small_num:
        num = res * 2
        count += 1
        if num > small_num:
            # count = count
            break
        list.append(num)
        res = num
    return count

def even_index(list1):
    even = []
    for i in list1[::2]:
        even.append(i)
    return even

def even_index_list(list1):
    even = []
    for i in list1[::2]:

        even.append(i)
    return even

def even_indices(list1):
  odd_indices_lst=[]
  for index, element in enumerate(list1):
    if index % 2 == 0:
        odd_indices_lst.append(index)
  return odd_indices_lst


def main():

    print("Please enter an arithmetic equation of your choosing. ")

    # The user enters a problem
    user = input()

    # The program then detects the problem type.
    # Multiplication, division, addition, and subraction are supported.
    # The users equation must include a "+", "/"", "*", or "-"
    # symbol to qualify for calculation.
    detect_type(user)

    # The User then specifies what style of solution they would like to see.


    choice = pick_style()

    # This function finds the larger and smaller number on either side of the operator.


    new = user.split("*", 2)
    numeral_one = (new[0])
    numeral_two = (new[1])
    numeral_one = int(numeral_one)
    numeral_two = int(numeral_two)

    if choice == 'Russian Peasant':
        if numeral_one < numeral_two:
            small_num = numeral_one
            big_num = numeral_two

            print((str(
                numeral_two)) + " is the bigger number, so we will divide it by two without saving the remainder till we have 1 as a result")

            print((str(
                numeral_one)) + " is the smaller number so we will multiply it by two till the number of multiplicands matches the number of results created by dividing the larger number.")
            print("The division list results are below.")
            print(str(numeral_two))

        else:
            big_num = numeral_one
            small_num = numeral_two

            print((str(
                numeral_one)) + " is the bigger number, so we will divide it by two without saving the remainder till we have 1 as a result")

            print((str(
                numeral_two)) + " is the smaller number so we will multiply it by two till the number of multiplicands matches the number of results created by dividing the larger number.")

            print("")
            print(str(numeral_one))

            # This function divides the larger number by two till the result is one.
        count = divide_larger(big_num)

        # This function multiplies the smaller number till the number of times
        # it has been multiplied equals the number of times the big number was
        # divided by to reach one.
        mult_smaller(small_num, count)
        # first column
        list_d = division_list(big_num)
        # second column
        list_m = mult_list(small_num, count)

        print('We will now collect the results of division into a list')
        print(list_d)
        print('We will now collect the results of multiplication into a list')
        print(list_m)
        print(
            "We will line up the two lists next to eachother in an array to record where uneven numbers are located in the first list "
            "and then find the number directly across in the next column.")
        arr_dm = np.column_stack((list_d, list_m))
        print(arr_dm)

        # indices = [i for i, x in enumerate(list_d) if x % 2 != 0]
        indices = odd_list(list_d)
        print("We will record the indices of all uneven numbers in the first column into a list.")
        print(indices)

        result_list = [list_m[i] for i in indices]

        print("We will use the list of indices of uneven numbers in division as an index for our multiplication list to "
              "extract the numbers which when added should give us our result.")
        print(result_list)
        print(
            "The sum of all numbers in the multiplication list which are directly across from uneven numbers in the division "
            "list should be reliably found using this method.")
        result = sum(result_list)
        print(result)


    elif choice == 'Egyptian':

        new = user.split("*", 2)
        numeral_one = (new[0])
        numeral_two = (new[1])
        numeral_one = int(numeral_one)
        numeral_two = int(numeral_two)

        small_num = numeral_one

        big_num = numeral_two

        mult_two(small_num)

        count = mult_listc(small_num)
        print("The multilication of powers of two took place " + str(count-1) + " times.")
        mult_big(big_num, count)
        list1 = mult_listb(small_num)
        list2 = mult_liste(big_num, count)


        print(list1)

        print("Our list of the bigger number doubled is below.")
        print(list2)
        even_index(list1)
        even_index(list2)

        el = even_index_list(list1)
        print(" The numbers at these indices added together will equal the smaller number in our equation. ")
        print(el)

        arr_em = np.column_stack((list1, list2))

        print(arr_em)

        even = even_indices(list1)
        print("This is a list of indices starting at 0 and returning every other number till the max of the list is reached. ")
        print(even)
        print("We will use this list as an index for the list beneath our bigger number.")
        nums_e_sol = [list2[i] for i in even]
        print(nums_e_sol)
        print("These numbers when added together will produce our result.")
        print(sum(nums_e_sol))


    elif choice == 'Modern Computing':

        print("The computer makes a list of 0's and 1's. ")
        print("If a number will be used to reach our sum we can think of the computer marking it with a 1.")
        print("If a number is part of reaching the process, but does not create the sum it will be marked with a 0.")
        print("Please go through our previous results and mark where the 0's and 1's would be on your own.")


    else:

        print('Your choice is not yet supported by this program, but please try researching on your own.')

if __name__ == '__main__':
    main()
