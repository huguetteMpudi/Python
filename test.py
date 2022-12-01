def same_first_last(nums):
    if (len(nums) >= 1):
        last = nums[len(nums) - 1]
        first = nums[0]
        if(last == first):
                print("the first and last item are the same")
        else:
            print("the first and last item are not the same")
    else:
        print("num should be empty")


nums = input("Enter a text: ")
same_first_last(nums)

def cars_open(a_open, b_open):
    if a_open == "yes" or b_open == "yes":
        print("There is danger")
        return True
    else :
        print("Doors are closed")
        return False



mycarA = input("is Car A door open? Yes or No ")
mycarB = input("is Car B door open? Yes or No ")

cars_open(mycarA,mycarB)


def make_out_word(ouput, word):
    l = list(output)
    l.insert(3,word)
    return print(''.join(l))

text = input("Enter your text ")
output = "((()))"
make_out_word(output, text)


def check_ticket(price):
    ticket = ""
    p = int(price)

    if (p <= 60 ):
        ticket = "no ticket"
    elif (61 <= p <= 80):
        ticket = "silver ticket"
    elif (p >= 81):
        ticket = "gold ticket"
    else:
        print("something else ")
    return print(ticket)

price = input("Ticket price : ")
check_ticket(price)