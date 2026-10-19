import copy


def reverse_image(image):
    """Обычное преобразование в негатив."""
    # res = copy.deepcopy(image)
    # for i in range(len(image)):
    #     for j in range(len(image[0])):
    #         res[i][j] = 0 if image[i][j] else 1
    # return res

    # return [[0 if pixel else 1 for pixel in row] for row in image]

    res = []
    for row in image:
        new_row = list()
        for pixel in row:
            new_row.append(0 if pixel else 1)
        res.append(new_row)
    return res


def reverse_image_recursive(image):
    """Рекурсивное преобразование в негатив."""
    if not image:
        return []
    return [[0 if pixel else 1 for pixel in image[0]]] + reverse_image_recursive(image[1:])

# Пример входных данных
input_image = [
    [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [1, 0, 0],
        [1, 0, 0]
    ]
]
for index, item in enumerate(input_image):
    # Вывод результатов
    print("Пример №", index + 1)
    print("Обычный метод:", reverse_image(item))
    print("Рекурсивный метод:", reverse_image_recursive(item))
