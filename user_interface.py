import compl
import model_div
import model_sum
import model_pow
import model_sub
import model_mult
import model_sqrt

print('Добро пожаловать в Калькулятор!')


def create():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Работа с рациональными числами")
        print("2. Работа с комплексными числами")
        print("0. Выход")
        try:
            choice1 = int(input("Выберете раздел: "))
        except ValueError:
            print('Это не целое число. Попробуйте снова...')
            return create()

        if choice1 == 1:
            print("\nРАЦИОНАЛЬНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню")
            try:
                choice2 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не целое число. Попробуйте снова...')
                return create()

            if choice2 == 1:

                return 1.1

            elif choice2 == 2:

                return 1.2

            elif choice2 == 3:

                return 1.3

            elif choice2 == 4:
                print("\nДЕЛЕНИЕ ЧИСЛА")
                print("1. '/' - обычное деление")
                print("2. '//' - целочисленное деление")
                print("3. '%' - остаток от деления")
                print("0. Вернуться в главное меню")
                try:
                    choice3 = int(input("Выберете операцию: "))
                except ValueError:
                    print('Это не целое число. Попробуйте снова...')
                    return create()

                if choice3 == 1:
                    return 1.41
                elif choice3 == 2:
                    return 1.42
                elif choice3 == 3:
                    return 1.43
                elif choice3 == 0:
                    create()

            elif choice2 == 5:

                return 1.5

            elif choice2 == 6:

                return 1.6

            elif choice2 == 0:
                create()
            else:
                print("Ой! Ошибка ввода")
                create()

        if choice1 == 2:
            print("\nКОМПЛЕКСНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("6. Корень квадратный числа")
            print("0. Вернуться в главное меню")
            try:
                choice2 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не целое число. Попробуйте снова...')
                return create()

            if choice2 == 1:
                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_sum.init(c1, c2)
                result = model_sum.do_it()
                print(result)
                return result


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
                create()

        if choice1 == 0:
            print('До скорых встреч!')
            quit()


create()
