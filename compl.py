x = 0
y = 0


def get_parts():
    global x
    global y
    while True:
        a = (input("Введите действительную часть числа: "))
        if not (a.isdigit()):
            print('Ошибка. Повторите ввод')
            continue
        x = int(a)
        break
    while True:
        b = (input("Введите мнимую часть числа: "))
        if not (b.isdigit()):
            print('Ошибка. Повторите ввод')
            continue
        y = int(b)
        break
    return x, y


def make_complex(a, b):
    num = complex(a, b)
    return num


