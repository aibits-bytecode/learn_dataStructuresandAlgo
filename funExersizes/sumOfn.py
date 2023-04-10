def sumofN(number):
    if number == 1:
        return 1
    return number + sumofN(number-1)


if __name__ == "__main__":
    print(sumofN(4))