print('Добро пожаловать в Калькулятор!')


def create():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Работа с рациональными числами")
        print("2. Работа с комплексными числами")
        print("0. Выход")
        choice1 = int(input("Выберете раздел: "))

        if choice1 == 1:
            print("\nРАЦИОНАЛЬНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню")
            choice2 = int(input("Выберете операцию: "))

            if choice2 == 1:

                return 1.1

            elif choice2 == 2:

                return 1.2

            elif choice2 == 3:

                return 1.3

            elif choice2 == 4:

                return 1.4

            elif choice2 == 5:

                return 1.5

            elif choice2 == 6:

                return 1.6

            elif choice2 == 0:
                create()
            else:
                print("Ой! Ошибка ввода")

        if choice1 == 2:
            print("\nКОМПЛЕКСНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню")
            choice2 = int(input("Выберете операцию: "))

            if choice2 == 1:

                return 2.1

            elif choice2 == 2:

                return 2.2

            elif choice2 == 3:

                return 2.3

            elif choice2 == 4:

                return 2.4

            elif choice2 == 5:

                return 2.5

            elif choice2 == 6:

                return 2.6

            elif choice2 == 0:
                create()

            else:
                print("Ой! Ошибка ввода")

        if choice1 == 0:
            print('До скорых встреч!')
            quit()
