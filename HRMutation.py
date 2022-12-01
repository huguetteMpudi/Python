def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


print(mutate_string("mummy returned", 7, "p"))
string