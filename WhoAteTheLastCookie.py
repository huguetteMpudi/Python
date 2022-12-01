def whoatecookie(n):

    return print("Who ate the last cookie? It was "+ n)

l = input("Enter your name ")

try:
    if(isinstance(int(l), int )== True):
        name = "Monica"

except:
    try:
        if (isinstance(float(l), float) == True):
            name = "Monica"
    except:
        if(l.isalpha() == True):
            name = "Zach"
        else:
            name = "the dog"

whoatecookie(name)
