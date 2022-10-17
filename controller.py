# файл связующее звено всех файлов

import user_interface
import model_sum as model
import compl


def button_click_c():
    value_a = compl.make_complex()
    value_b = compl.make_complex()
    model.init(value_a, value_b)
    result = model.do_it()
    print(result)
