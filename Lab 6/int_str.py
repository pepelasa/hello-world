
def int_to_str(number):

    if not isinstance(number, int):
        return "Not a number"

    negative = False
    if number == 0:
        string = '0'
    elif number < 0:
        negative = True
        number *= -1
        string = ''
    else:
        string = ''

    while number != 0:
        rnumber = number % 10
        number //= 10

        if rnumber == 0:
            string = '0' + string
        elif rnumber == 1:
            string = '1' + string
        elif rnumber == 2:
            string = '2' + string
        elif rnumber == 3:
            string = '3' + string
        elif rnumber == 4:
            string = '4' + string
        elif rnumber == 5:
            string = '5' + string
        elif rnumber == 6:
            string = '6' + string
        elif rnumber == 7:
            string = '7' + string
        elif rnumber == 8:
            string = '8' + string
        elif rnumber == 9:
            string = '9' + string
        else:
            string = "Not a number"
            break

    if negative:
        return '-' + string
    else:
        return string


def str_to_int(string):

    if not isinstance(string, str):
        return "Not a string"

    if string == "":
        return "Not a number"

    number = 0
    sign = 1
    i = 0

    for character in string:
        number *= 10
        if character == '1':
            number += 1
        elif character == '2':
            number += 2
        elif character == '3':
            number += 3
        elif character == '4':
            number += 4
        elif character == '5':
            number += 5
        elif character == '6':
            number += 6
        elif character == '7':
            number += 7
        elif character == '8':
            number += 8
        elif character == '9':
            number += 9
        elif character == '-':
            if i == 0:
                sign = -1
            else:
                return "{} is not a number".format(string)
        elif character == '+':
            if i != 0:
                return "{} is not a number".format(string)
        elif character != '0':
            return "Error {} not a number".format(character)
        i += 1

    return sign*number


# zero
str_0 = int_to_str(0)
int_0 = str_to_int("0")
print(f"str_to_int(\"0\") = {int_0} and int_to_str(0) = \"{str_0}\"")

# regular number
str_1 = int_to_str(1234)
int_1 = str_to_int("1234")
print(f"str_to_int(\"1234\") = {int_1} and int_to_str(1234) = \"{str_1}\"")

# Invalid options (string for int and int for string)
str_2 = int_to_str('a')
int_2 = str_to_int(9)
print(f"str_to_int(9) = {int_2} and int_to_str('a') = \"{str_2}\"")

# Negative ints
str_3 = int_to_str(-50)
int_3 = str_to_int("-50")
print(f"str_to_int(\"-50\") = {int_3} and int_to_str(-50) = \"{str_3}\"")

# Negative used wrong
str_4 = int_to_str(555555)
int_4 = str_to_int("5-")
print(f"str_to_int(\"5-\") = {int_4} and int_to_str(555555) = \"{str_4}\"")

# Double negative in string
str_5 = int_to_str(-0)
int_5 = str_to_int("5-50-")
print(f"str_to_int(\"5-50-\") = {int_5} and int_to_str(-0) = \"{str_5}\"")

# Implicit positive value
str_6 = int_to_str(+0)
int_6 = str_to_int("+40")
print(f"str_to_int(\"+40\") = {int_6} and int_to_str(+0) = \"{str_6}\"")

# Double use of + and -
str_7 = int_to_str(987654321)
int_7 = str_to_int("+-10")
print(f"str_to_int(\"+-10\") = {int_7} "
      f"and int_to_str(987654321) = \"{str_7}\"")

# Use of wildcards
str_8 = int_to_str(10101)
int_8 = str_to_int("*")
print(f"str_to_int(\"*\") = {int_8} and int_to_str(10101) = \"{str_8}\"")

# Empty string
str_9 = int_to_str(-10101)
int_9 = str_to_int("")
print(f"str_to_int(\"\") = {int_9} and int_to_str(-10101) = \"{str_9}\"")
