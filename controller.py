# файл связующее звено всех файлов

import user_interface
import model_sum as model


def button_click():
    value_a = user_interface.get_value()
    value_b = user_interface.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    user_interface.view_data(result)

