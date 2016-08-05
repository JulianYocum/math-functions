    #!/usr/local/bin python
    #interface.py

    import sys

    def error():
        print("Invalid entry: Please enter an integer greater than 1")
    def usage():
        print("usage: python3 factor.py [a] [b] ...")
        print()
        sys.exit()

    # gets polynomial from user
    def getpoly():
        # reset polynomial if assigned before
        polynomial = []

        if(len(sys.argv) > 2):
            for i in sys.argv[1:]:
                try:
                    int(i)
                except ValueError:
                    usage()
            polynomial = list(map(int, sys.argv[1:]))

        elif(len(sys.argv) == 1):
            # gets number of terms of [int]polynomial
            terms = 0
            while(True):
                try:
                    terms = int(input("# of terms: "))
                    #checks for value 0
                    if(terms <= 1):
                        error()
                        continue
                    break
                except ValueError:
                    error()
            terms = int(terms)
            # collects [int] for each index of polynomial
            for i in range(terms):
                val = 0
                while(True):
                    try:
                        val = int(input("Enter value of term " + str(i+1) + ": "))
                        break
                    except ValueError:
                        error()
                polynomial.append(val)

        else:
            usage()


        # check that user submission is correct.
        while(True):
            # show user input
            print("The polynomial you entered is:\t", end='')
            printpoly(polynomial)
            print()
            proceed = input("Would you like to proceed? y/n: ")
            if(proceed == "y" or proceed == "Y"):
                return polynomial
                break
            elif(proceed == "n" or proceed == "N"):
                sys.argv = []
                return getpoly()
                break
            else:
                print("Please enter y or n")


    # prints [readable]polynomial for user
    def printpoly(poly):
        for i in range(len(poly)):
            if(i == len(poly)-1):
                print(str(poly[i]), end='')
            elif(i < len(poly) - 1):
                coefficient = str(poly[i])
                if(poly[i] == 1):
                    coefficient = ""

                if(i == len(poly)-2):
                    print(coefficient + "x", end='')
                else:
                    print(coefficient + "x^" + str(len(poly) - 1 - i), end='')
                print(" + ", end='')
