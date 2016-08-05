#!/usr/local/bin python
#factor.py

import interface
from math import log10
from fractions import Fraction

# greatest common divisor
def gcd(poly):
    # shift unused place values
    x = ""
    ex = 0
    for i in range(len(poly)-1,-1,-1):
        if(poly[i] == 0):
            if(x == ""):
                x = "x"
            elif(x == "x"):
                x = "x^"
            ex += 1
            poly.pop()
    if(ex > 1):
        x += str(ex)

    # Euclidian Algorithm
    divisor, temp = poly[0], poly[1]
    # get divisor for first 2 elements
    while(temp):
        divisor, temp = temp, divisor % temp
    # get divisor for rest of elements
    if(len(poly) > 2):
        for i in poly[2:]:
            temp = i
            while(temp):
                divisor, temp = temp, divisor % temp
    # if first term is negative -> divisor must be negative
    if(poly[0] < 0 and not (divisor < 0)):
        divisor *= -1

    if(divisor == 1):
        divisor = ""
    else:
        # factor out common divider
        for i in range(len(poly)):
            poly[i] = int(poly[i] / divisor)

    return str(divisor) + x

# rational zero test to extract zeros
def rzt(poly):
    # factors of constant
    p = []
    # factors of coefficient
    q = []
    # positive storage
    temppos = []
    # negative storage
    tempneg = []
    # make list of all possibile factors (negative inclusive)
    for i in range(1,poly[-1]+1):
        if(poly[-1] % i == 0):
            temppos.append(i)
            tempneg.insert(0,-i)
    p = tempneg + temppos

    # reset storage
    temppos = []
    tempneg = []
    # make list of all possibile factors (negative inclusive)
    for i in range(1,poly[0]+1):
        if(poly[0] % i == 0):
            temppos.append(i)
            tempneg.insert(0,-i)
    q = tempneg + temppos

    # find all possibile zeros
    zeros = []
    for i in p:
        for j in q:
            zero = Fraction(i,j)
            if(zero not in zeros):
                # sum of all terms
                sum = 0
                for k in range(len(poly)):
                    sum += poly[k] * int(zero) ** (len(poly) - 1 - k)
                # check if poly(zero) == 0
                if(sum == 0):
                    zeros.append(zero)
    return zeros

# synthetic divison to check zeros
def synthdiv():
    global remainder
    remainder = poly
    divisors = []
    temp = []
    while(True):
        factors = rzt(remainder)
        if(factors == []):
            #return factors
            break
        for i in range(len(factors)):
            for j in range(len(remainder)):
                if(j == 0):
                    temp.append(remainder[j])
                else:
                    temp.append(remainder[j] + temp[j - 1] * int(factors[i]))
            if(temp[-1] == 0):
                temp.pop()
            else:
                print("Error synthdiv")
                return
            divisors.append(int(factors[i]))
            remainder = temp
            temp = []
    return divisors



# gets polynomial from user
poly = interface.getpoly()

# common divisor
cdivisor = gcd(poly)



remainder = []
divisors = synthdiv()

#if(divisors == []):
#    print("Cannot be factored into rational numbers")
#    print()
#else:

if(cdivisor != ""):
    print(str(cdivisor),end='')
for i in range(len(divisors)):
    print("(x", end='')
    if(divisors[i] >= 0):
        print(" - ", end='')
    else:
        print(" + ", end='')
    print(str(divisors[i])[1:] + ")", end='')
if(remainder != [1]):
    print("(", end='')
    interface.printpoly(remainder)
    print(")", end='')
print("\n")

#while(True):
#    zeros = rzt(temppoly)
#    print(zeros)
#    if(len(zeros) == 0):
#        break
#    for i in zeros:
#        temppoly = polydiv([1,-int(i)],temppoly)
#        factors.append([1,-int(i)])
