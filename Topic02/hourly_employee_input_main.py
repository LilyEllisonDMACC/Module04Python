"""
Program: hourly_employee_input.py
Author: Lily Ellison
Last date modified: 02/05/2023

The purpose of this program is to intake a user's for a name (string), hours worked (int) and an hourly pay rate (
float) and print a string including the information.

Exceptions are handled in main.

"""

def hourly_employee_input(): #keyword def with function name and ():
    """Prompts user for name, hours worked, and hourly pay rate. prints a string with this info"""

    name = input("Please enter your name: ")
    if (len(name) <= 0): #I could not get the try... except to throw an error when len(name) == 0, so I used an if
        raise ValueError('Bad Input')

    hours_worked = input("Please enter your hours worked: ")
    try:
        hours_worked_as_int = int(hours_worked)  #Checks that input is an integer
        if(hours_worked_as_int >= 0): #Checks that input is positive or zero
            hours_worked = hours_worked_as_int #casts input as an integer if positive or zero
        else:
            raise ValueError('Bad Input') #throws an error for negative entry
    except:
        raise ValueError('Bad Input')

    hourly_rate = input("Please enter your hourly pay rate: ")
    try:
        hourly_rate_as_float = float(hourly_rate) #checks that input can be a float
        if(hourly_rate_as_float >= 0): #checks that input is positive or zero
            hourly_rate = "{:.2f}".format(hourly_rate_as_float) #casts input as a float with 2 decimals if positive or 0
        else:
            raise ValueError('Bad Input') #throws error if negative
    except:
        raise ValueError('Bad Input')

    print(name, "worked for", hours_worked, "hours at a rate of", hourly_rate, "per hour.")

if __name__ == '__main__':  #Calls the function from main.
   try:
    hourly_employee_input()
   except:
    print("ValueError encountered!")
