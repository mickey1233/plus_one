def plusone(digits):
    di = 1
    sum = 0
    for i in digits[::-1]:
        sum = sum + (i * di)
        di = di * 10
    sum = sum + 1
    return list(map(int, str(sum)))


def main():
    x = []
    x.append(plusone([1, 2, 3]))
    x.append(plusone([4, 3, 2, 1]))
    x.append(plusone([0]))
    x.append(plusone([9]))
    print(x)


if __name__ == "__main__":
    main()
