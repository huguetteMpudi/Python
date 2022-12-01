def convertScore(phrase):
    a_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "nil"
    }

    m = phrase.split(" ")
    v = []
    for b in m:
        for k, value in a_dict.items():
            if b in value:
                v.append(k)

    return print(v)


score = input("Shout the score ")
convertScore(score)
