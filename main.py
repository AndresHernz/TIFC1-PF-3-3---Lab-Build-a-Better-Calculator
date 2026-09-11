def addmultiplenumbers(numbers):
    total = 0.0

    for number in numbers:
        total = total + number

    return total


def multiplymultiplenumbers(numbers):
    total = 1.0

    for number in numbers:
        total = total * number

    return total


def isitaninteger(num):
    return num % 1 == 0


def isiteven(num):
    if isitaninteger(num) and num % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
