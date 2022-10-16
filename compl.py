def make_complex():
    while True:
        a = (input("Введите действительную часть числа: "))
        if not (a.isdigit()):
            print('Ошибка. Повторите ввод')
            continue
        a = float(a)
        break
    while True:
        b = (input("Введите мнимую часть числа: "))
        if not (b.isdigit()):
            print('Ошибка. Повторите ввод')
            continue
        b = float(b)
        break
    return complex(a, b)
