import user_interface
import model_div


def value_err():
    try:
        user_interface.get_value()
    except ValueError:
        return print('Это не целое число. Попробуйте снова...')


def zero_err():
    try:
        model_div.div()
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
