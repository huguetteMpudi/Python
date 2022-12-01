# Version 3.10
# Lucia Rosado-Fournier
# From https://pythonprinciples.com/challenges/Middle-letter/
# Write a script that takes a string as its
# input. Your script should extract and return the
# middle letter.
# Extra: If there is no middle letter, your function
# should return the empty string.
# For example, "abc" should return "b"
# Extra: "aaaa" should return "".

# Math library - provides extra math functions. Using it for the floor function
# import math

# 1. Take input from user
userInput = input("Please enter a string: ")
# 2. Get length of string
stringLength = len(userInput)
# 3. Divide by 2
midVal = stringLength/2

# TEST: Check length and mid val are correct (passed)
# print(stringLength, midVal)

# 4. Turn decimal value into int
# Note: strings are indexed starting at 0, so you want to round down
# Method 1:
# Note: when using int on a decimal value, it will just cut off the decimal part
midIndex = int(midVal)
# Method 2:
# midIndex = math.floor(midVal)

# TEST: Check the index is correct (passed)
# print(midIndex)

# Extra: Check if the string is odd
# Note: If a value is odd, the remainder when divided by 2 should be 1
# Note: I added quotes to be visible on the console, this isn't needed
if (stringLength % 2) == 1:
    # 5. If odd, Print the character at the middle index
    print('"' + userInput[midIndex] + '"')
# If it's even, print nothing
else:
    print('""')
