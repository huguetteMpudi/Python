def CollatzConjectureLength(n):
    myList = [n]
    while n > 1:
        odd = n % 2
        if odd == 0:
            n = n // 2
            myList.append(n)

        else:
            n = (n * 3) + 1
            myList.append(n)

    return myList


number = input("Enter your number : ")
r = int(number)
print(len(CollatzConjectureLength(r)))
