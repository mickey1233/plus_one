def plusone(digits):
    di = 1
    sum = 0
    for i in digits[::-1]:
        sum = sum + (i * di)
        di = di * 10
    sum = sum + 1
    return (list(map(int, str(sum))))


def plusone1(digits):
    return list(map(int, str((int("".join(map(str, digits)))+1))))


def main():
    x = []
    y = []
    x.append(plusone([1, 2, 3]))
    y.append(plusone([1, 2, 3]))
    x.append(plusone([4, 3, 2, 1]))
    y.append(plusone1([4, 3, 2, 1]))
    x.append(plusone([0]))
    y.append(plusone([0]))
    x.append(plusone([9]))
    y.append(plusone([9]))
    print(x)
    print(y)


if __name__ == "__main__":
    main()

