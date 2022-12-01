def print_full_name(first, last):
    if len(last) <= 10 and len(first) <= 10:
        return print("Hello" + first + last + "! You just delved into python.")
    else:
        return print("Your name is too long")



first_name = input("What is your first name")
last_name = input("What is your last name")
print_full_name(first_name, last_name)
