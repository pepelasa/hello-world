

def convert2b(test):

    if test == 0:
        bNumber = '0'
    else:
        bNumber = ''

    while test != 0:
        if test % 2:
            bNumber = "1" + bNumber
        else:
            bNumber = "0" + bNumber

        test = int(test/2) 

    return bNumber

def convert2x(test):

    if test == 0:
        xNumber = '0'
    else:
        xNumber = ''

    while test != 0:
        xDigit = test % 16

        if xDigit < 10:
            xNumber = str(xDigit) + xNumber
        else:
            xNumber = str(chr(55+xDigit)) + xNumber
        
        test = int(test/16)

    return xNumber


try:
    print("Please enter a positive number: ")
    entry = input()
    dNumber = int(entry)
    
    # Decimal to binary
    bNumber = convert2b(dNumber)

    #Decimal to hexadecimal
    xNumber = convert2x(dNumber)
  
    print(f'binary of {dNumber} is 0b{bNumber} and hexadecimal is 0x{xNumber}')

except ValueError:
    print(f"The input {entry} is not a number")
    exit
