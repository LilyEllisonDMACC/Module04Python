"""
Program: InputValidationTryAve.py
Author: Lily Ellison
Last date modified: 02/05/2023

The purpose of this program is to accept user's name (first and last), age, and a constant number of scores, validate
the input with try/except, calculate the average of the scores, and print out this information in a statement like:
Rodriguez, Linda age: 21 average grade: 92.50

"""

"""
Pseudo-code/comments included
"""

'#store a constant for the number of scores for user to input: 4'
NUMBER_OF_SCORES = 4

'#prompt user for last_name and store as last_name'

last_name = input("Please enter your last name: ")
#test for valid input by checking for incorrect input
try:
    last_name == int(last_name)
except:
    print("Last name accepted.")
else:
    print("Last name not recognized as a string.")

# prompt for first_name and store as first_name
first_name = input("Please enter your first name: ")
#test for valid input by checking for invalid input type
try:
    first_name == int(first_name)
except:
    print("First name accepted.")
else:
    print("First name not recognized as a string.")

# prompt for age and store as age
age = input("Please enter your age: ")

try:
    #test if input can be converted to integer
    age_as_int = int(age)
    #if input can be converted, check that it is in range
    if (age_as_int >= 0):
        print("Age accepted.")
    #throw exception if not in range
    else:
        raise ValueError('Bad Input')
#if exception thrown, message prints:
except:
    print("Input should be positive integer.")

# prompt user for scores - either separate or a running total - constant times
score01 = input("Please enter your first score: ")
try:
    #Same idea of testing for valid input
    #(float instead of int)
    score01_as_float = float(score01)
    #and within range (0-105 instead of positive) for all scores
    if (score01_as_float >= 0 and score01_as_float <= 105):
        #convert passing scores to floats so they can be used in average calculations
        score01 = score01_as_float
        print("Score accepted.")
    else:
        raise ValueError('Bad Input')
except:
    print("Input should be between 0 and 105.")

score02 = input("Please enter your second score: ")
try:
    score02_as_float = float(score02)
    if (score02_as_float >= 0 and score02_as_float <= 105):
        score02 = score02_as_float
        print("Score accepted.")
    else:
        raise ValueError('Bad Input')
except:
    print("Input should be between 0 and 105.")

score03 = input("Please enter your third score: ")
try:
    score03_as_float = float(score03)
    if (score03_as_float >= 0 and score03_as_float <= 105):
        score03 = score03_as_float
        print("Score accepted.")
    else:
        raise ValueError('Bad Input')
except:
    print("Input should be between 0 and 105.")

score04 = input("Please enter your fourth score: ")
try:
    score04_as_float = float(score04)
    if (score04_as_float >= 0 and score04_as_float <= 105):
        score04 = score04_as_float
        print("Score accepted.")
    else:
        raise ValueError('Bad Input')
except:
    print("Input should be between 0 and 105.")

# calculate average - sum and divide by number of values
#check for bad input from earlier that would cause a crash
try:
    average = (score01 + score02 + score03 + score04) / NUMBER_OF_SCORES

except:
    print("Bad input value caused error. Cannot calculate average.")

else:
# print output; like:
# Rodriguez, Linda age: 21 average grade: 92.50

    print(f'{last_name}, {first_name} age: {age} average grade: {average: 5.2f}')

"""
The final line still prints if the names and age have bad input, but the scores cannot be averaged if they are not 
the correct data type.

I tried this by concatination first and found that I needed to convert the float of average back to a string.
I didn't like that because I wanted to control the decimal precision at the print line. I much prefer this F
statement way of outputting info.
I ran several random inputs and got accurate results.
It does throw an error when a non-number is entered as a score, but I assume we will address this when we get
into loops. I imagine something that says "if score01 is not a number, ask for score01 again" written into the 
code would help.
"""
