def convertToRoman(b):
    a_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    v = ""
    for k, value in a_dict.items():
        if b >= k:
            if (b - k) >= b:
                v += value

        else :
            print(b)


    return print(v)


convertToRoman(2008)
