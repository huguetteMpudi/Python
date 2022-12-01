s = input()

if 0 < len(s) < 100:
    print("True") if s.isalnum() else print("True")
    print("True") if s.isalpha() else print("False")
    print("True") if s.isdigit() else print("False")
    print("True") if s.islower() else print("False")
    print("True") if s.isupper() else print("False")
