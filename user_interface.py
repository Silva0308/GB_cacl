import compl
import model_div
import model_sum
import model_pow
import model_sub
import model_mult
import model_sqrt
import excep

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
                r1 = excep.take_value()
                r2 = excep.take_value()
                model_sum.init(r1, r2)
                result = model_sum.do_it()
                print(result)
                return result


            elif choice2 == 2:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_sub.init(r1, r2)
                result = model_sub.do_it()
                print(result)
                return result

            elif choice2 == 3:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_mult.init(r1, r2)
                result = model_mult.do_it()
                print(result)
                return result

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
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    result = model_div.do_it()
                    print(result)
                    return result
                elif choice3 == 2:
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    result = model_div.do_it_w()
                    print(result)
                    return result
                elif choice3 == 3:
                    r1 = excep.take_value()
                    r2 = excep.take_value()
                    model_div.init(r1, r2)
                    result = model_div.do_it_r()
                    print(result)
                    return result
                elif choice3 == 0:
                    create()

            elif choice2 == 5:

                r1 = excep.take_value()
                r2 = excep.take_value()
                model_pow.init(r1, r2)
                result = model_pow.do_it()
                print(result)
                return result

            elif choice2 == 6:

                r1 = excep.take_value()
                result = model_sqrt.do_it(r1)
                print(result)
                return result

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


            elif choice2 == 2:

                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_sub.init(c1, c2)
                result = model_sub.do_it()
                print(result)
                return result

            elif choice2 == 3:

                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_mult.init(c1, c2)
                result = model_mult.do_it()
                print(result)
                return result

            elif choice2 == 4:

                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_div.init(c1, c2)
                result = model_div.do_it()
                print(result)
                return result

            elif choice2 == 5:

                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_pow.init(c1, c2)
                result = model_pow.do_it()
                print(result)
                return result

            elif choice2 == 6:

                c1 = compl.make_complex()
                result = model_sqrt.do_it_c(c1)
                print(result)
                return result

            elif choice2 == 0:
                create()

            else:
                print("Ой! Ошибка ввода")
                create()

        if choice1 == 0:
            print('До скорых встреч!')
            quit()


create()
