"""
Program: multiply_string.py
Author: Lily Ellison
Last date modified: 02/05/2023

The purpose of this program is to accept a user's string and a number between 2 and 7 as parameters passed by the main.
The program will then repeat the user's string the number of times for the number the user entered.

"""

def multiply_string(string_in, number_in): #keyword def with function name and ():
    """
    Prompts user for name, hours worked, and hourly pay rate, calculates weekly pay
    :param string_in: string entered by user
    :param number_in: a number between 2 and 7, entered by user
    :returns a string with this info, info_from_function
    """

    return_string = string_in * number_in #Takes parameters and creates a new string to return

    return return_string #returns to main

if __name__ == '__main__':  #Calls the function from main.
    user_string = input("Enter your favorite class: ")
    if (len(user_string) <= 0): #checks for empty entries
        print("No entry given, \"Python\" will be used for your favorite class.")  #Informs user no valid entry given
        user_string = "Python" #Reassigns "Python" to user_string

    user_number = input("Enter a number between 2 and 7: ")

    try:
        user_number_as_int = int(user_number) #checks for int
        if (user_number_as_int <= 7 and user_number_as_int >= 2):  # Checks that input is within range
            user_number = user_number_as_int  # casts input as an integer if within range
        else:
            raise ValueError('Bad Input')  # throws an error for out of range entry
    except:
        print("Invalid entry, number will be 2.")  # Informs user of invalid input
        user_number = 2  # assigns 2 to user_number

    print(multiply_string(user_string, user_number)) #calls the functions and prints what it returns