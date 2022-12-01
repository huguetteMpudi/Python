
# better use case
counter1 = 0
usrPasswd = input("Please enter your password: ")
actPasswd = "P@ssword"
#
while usrPasswd != actPasswd:
    print("password was incorrect, try again!")
    counter1 += 1
    if counter1 < 3:
         usrPasswd = input("Please enter your password: ")
    else:
        print("Exceeded max attempts")
#       Exits the loop
    break
