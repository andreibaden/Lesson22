def count_even_values(ls):
    count = 0

    for item in ls:
        if item % 2 == 0:
            count += 1

    return count


def test():
    print(count_even_values([1, 2, 3, 4]) == 2)
    print(count_even_values([6, 8, 34, 4]) == 4)
    print(count_even_values([1, 5, 3, 7]) == 0)


if __name__ == "__main__":
    test()
