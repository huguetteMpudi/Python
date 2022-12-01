def Passwordmaker(password):
    newPass = ""
    test = password.split(" ")
    print(test)
    for rt in test:
        print(rt[0])
        if rt[0] == "o":
            y = "0"
        elif rt[0] == "i":
            y = "1"
        elif rt[0] == "s":
            y = "5"
        else:
            y = rt[0]

        newPass += y
    return print(newPass)


password = input("Enter your pass phrase ")

Passwordmaker(password)
