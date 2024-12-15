import sys
import math


def read_coef_from_input(name):
    while True:
        try:
            coef = float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка. Введите действительное число")
        else:
            break
    return coef


def read_coef(index, name):
    try:
        coef = float(sys.argv[index])
    except IndexError:
        coef = read_coef_from_input(name)
    return coef


def get_coefs():
    a = read_coef(1, "A")
    b = read_coef(2, "B")
    c = read_coef(3, "C")
    return a, b, c


def get_roots(a, b, c):
    if a == 0:
        if b == 0:
            return []
        else:
            return [-1 * c / b, ]
    result = []

    d = b**2 - 4*a*c
    print(f"Дискриминант: {d}")
    if d > 0:
        d_sqrt = math.sqrt(d)
        root1 = (-b + d_sqrt) / (2.0 * a)
        root2 = (-b - d_sqrt) / (2.0 * a)
        if root1 > 0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        elif root1 == 0:
            result.append(root1)
        if root2 > 0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
        elif root2 == 0:
            result.append(math.fabs(root2))
    elif d == 0:
        root = -b / (2.0 * a)
        if root > 0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
        elif root == 0:
            result.append(0)

    return sorted(result)


def print_roots(roots):
    roots_number = len(roots)
    if roots_number == 0:
        print("Нет корней")
    elif roots_number == 1:
        print(f"Один корень: {roots[0]}")
    elif roots_number == 2:
        print(f"Два корня: {roots[0]}, {roots[1]}")
    elif roots_number == 3:
        print(f"Три корня: {roots[0]}, {roots[1]}, {roots[2]}")
    elif roots_number == 4:
        print(f"Четыре корня: {roots[0]}, {roots[1]}, {roots[2]}, {roots[3]}")


def main():
    a, b, c = get_coefs()
    roots = get_roots(a, b, c)
    print_roots(roots)


if __name__ == "__main__":
    main()
