import re


def rgb2hex(r=0, g=0, b=0):
    """
    Конвертирует значения RGB в шестнадцатеричную строку.

    Параметры:
    r, g, b (int): Значения цветовых компонент (0-255)

    Возвращает:
    str: Цвет в формате #rrggbb

    Выбрасывает:
    TypeError: Если компоненты не целые числа
    ValueError: Если значения вне диапазона 0-255
    """
    for name, val in (('r', r), ('g', g), ('b', b)):
        if type(val) is not int:
            raise TypeError(
                f"{name} component must be int, got {type(val).__name__}"
                )
        elif not 0 <= val <= 255:
            raise ValueError(
                f"{name} component {val} out of range 0..255"
                )

    return f"#{r:02x}{g:02x}{b:02x}"

    

def hex2rgb(hex_str):
    """
    Конвертирует шестнадцатеричную строку в словарь RGB.
    
    Поддерживаемые форматы:
    - #rrggbb
    - rrggbb
    - #rgb → расширяется в #rrggbb
    
    Параметры:
    hex_str (str): Шестнадцатеричное представление цвета
    
    Возвращает:
    dict: Словарь с ключами 'r', 'g', 'b' и значениями 0-255
    
    Выбрасывает:
    TypeError: Если вход не строка
    ValueError: При неверном формате или недопустимых символах
    """

    if not isinstance(hex_str, str):
        raise TypeError("hex value must be a string")

    pattern = r"^(#[0-9a-fA-F]{6}|[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})$"
    if not re.fullmatch(pattern, hex_str):
        raise ValueError("hex string must be in format rrggbb or rgb (with or without leading #)")

    hex_str = hex_str[1:] if '#' in hex_str else hex_str
    if len(hex_str) == 3:
        hex_str = ''.join(char*2 for char in hex_str)
    
    return {
        'r': int(hex_str[0:2], 16),
        'g': int(hex_str[2:4], 16),
        'b': int(hex_str[4:6], 16)
        }


if __name__ == '__main__':
    assert rgb2hex(15, 17, 21) == '#0f1115'
    assert rgb2hex(0, 0, 0) == '#000000'
    assert rgb2hex(255, 255, 255) == '#ffffff'

    # hex2rgb
    assert hex2rgb('#0f1115') == {'r': 15, 'g': 17, 'b': 21}
    assert hex2rgb('0f1115') == {'r': 15, 'g': 17, 'b': 21}
    assert hex2rgb('#abc') == {'r': 170, 'g': 187, 'b': 204}

    # Проверка некорректных значений
    try:
        rgb2hex(256, 0, 0)
        assert False, 'Expected ValueError'
    except ValueError:
        pass

    try:
        hex2rgb('#gggggg')
        assert False, 'Expected ValueError'
    except ValueError:
        pass

    print('All tests passed!')