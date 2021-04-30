import sys
def BinDec(n):
    for i in str(n):
        if i in '23456789':
            return print('Error:', n, 'is not a binary number')
            #sys.exit('BinDec(n) must receive a binary number n as argument')

    decimal = 0
    exponent = 0
    n = str(n)
    for digit in n[::-1]:
        digit = int(digit) * (2**exponent)
        decimal += digit
        exponent += 1
    return decimal

# TEST
# print(BinDec(11111010100))