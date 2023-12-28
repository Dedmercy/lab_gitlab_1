import os


def pow_(*, a: float, n: int) -> float:
    if n == 0:
        return 1

    counter: int = 0
    res: float = 1

    while n > counter:
        res = res * a
        counter += 1

    return res


def main():
    a = float(os.getenv('NUMBER', 2.0))
    n = int(os.getenv('POW', 2))

    result = pow_(a=a, n=n)

    with open('result/result.txt', 'w') as file:
        file.write(str(result))

    print('Файл записан!!!')


if __name__ == '__main__':
    main()
