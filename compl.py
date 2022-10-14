x = 0
y = 0


def get_parts():
    a = int(input("Введите действительную часть числа: "))
    b = int(input("Введите мнимую часть числа: "))
    global x
    global y
    x = a
    y = b
    return x, y


def make_complex(a, b):
    num = complex(a, b)
    return num



