def check_soft_asc(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for index in range(len(ls) - 1):
        if ls[index] >= ls[index + 1]:
            return False

    return True


def check_soft_desc(ls):
    if not isinstance(ls, (list, tuple)):
        return False

    for index in range(len(ls) - 1):
        if ls[index] <= ls[index + 1]:
            return False

    return True


def check(ls):
    return check_soft_desc(ls) or check_soft_asc(ls)


def test():
    print(check([1, 2, 3, 4, 5, 6]))
    print(check([6, 5, 4, 3, 2, 1]))
    print(check([1, 5, 3, 4, 5, 6]))
    print(check([1, 3, 3, 4, 5, 6]))


if __name__ == "__main__":
    test()
