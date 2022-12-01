def capitalize(full):
    if 0 >= len(full) or len(full) >= 100:
        for i in full.split():
            a = i
        print(a)
        i = i.capitalize()

        full = full.replace(a, i)

    return print(full)



fullname = input("Enter Full name")

capitalize(fullname)
