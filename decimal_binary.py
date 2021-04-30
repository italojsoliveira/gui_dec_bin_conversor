def DecBin(n):
    binary = ""
    while n > 1 :
        remainder = n % 2
        binary += str(remainder)
        n = n//2
    binary += str(n)
    return int(binary[::-1]) # return a string may not be bad for a binary number

#TEST
#for i in range(20):
#    print(i, DecBin(i))