number = 7


def calc(num):
    if num % 2 == 0:
        return calc(num / 2)
    else:
        return calc(num * 3 + 1)


calc(number)