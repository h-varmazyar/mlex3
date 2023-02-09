import math


def read_passwords(*passwords):
    for password in passwords:
        print("The complexity of \"{}\" is {}".format(password, calculate_complexity(password)))


def calculate_complexity(password):
    r_parameter = calculate_r_parameter(password)
    r_log = math.log(r_parameter, 2)

    complexity = len(password) * r_log

    return complexity


def calculate_r_parameter(password):
    has_upper = False
    has_lower = False
    has_numeric = False
    has_magic = False

    for c in password:
        if 'A' <= c <= 'Z':
            has_upper = True
        elif 'a' <= c <= 'z':
            has_lower = True
        elif '0' <= c <= '9':
            has_numeric = True
        else:
            has_magic = True

    r_parameter = 0
    if has_magic:
        r_parameter += 33

    if has_numeric:
        r_parameter += 10

    if has_upper:
        r_parameter += 26

    if has_lower:
        r_parameter += 26

    return r_parameter

if __name__ == '__main__':
    read_passwords("pass1", "Pass2", "p@ss", "P@ss", "P@ss5")
