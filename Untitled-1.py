def is_palindrome(string):
    """Обычная проверка палиндрома."""
    result = ''.join(string.lower().split())
    return result == result[::-1]


def is_palindrome_recursive(string):
    """Рекурсивная проверка палиндрома."""
    result = ''.join(string.lower().split())
    if len(result) <= 1:
        return True
    if result[0] != result[-1]:
        return False
    return is_palindrome_recursive(result[1:-1])


# Получение ввода от пользователя
string_input = input("Введите строку: ")

# Вывод результатов
print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input))
