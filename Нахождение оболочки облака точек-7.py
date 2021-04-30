# import time
# import timeit

import numpy as np
import matplotlib.pyplot as plt

count_of_points = 50
cloud_of_points = []


# Ручной ввод для проверки
# x_coordinates_of_points = np.array([30, 300, 30, 50, 210, 150, 40, 240, 80, 190, 240, 200, 30, 300])
# y_coordinates_of_points = np.array([150, 40, 80, 220, 60, 190, 50, 120, 170, 230, 50, 30, 230, 100])

# Генерация случайных координат
x_coordinates_of_points = np.random.randint(20, 300, count_of_points)
y_coordinates_of_points = np.random.randint(20, 300, count_of_points)
print('Старт! - Заданное облако точек (x_coordinates_of_points)', x_coordinates_of_points,
      type(x_coordinates_of_points))
print('Старт! - Заданное облако точек (y_coordinates_of_points)', y_coordinates_of_points,
      type(y_coordinates_of_points))


def draw_going_from_right_to_left_and_up_lines(x_array, y_array,
                                               min_x_coordinate, min_y_coordinate, start_point):
    print('Запуск функции "draw_going_from_left_to_down_lines"')
    print('min_y_coordinate', min_y_coordinate)
    print('min_x_coordinate', min_x_coordinate)

    x_output_array = np.array([start_point[0]])
    y_output_array = np.array([start_point[1]])

    print('!!! x_output_array < ', x_output_array, ' > !!!')
    print('!!! y_output_array < ', y_output_array, ' > !!!')

    next_point = np.array([])
    y_array_difference = np.delete(y_array, np.where(x_array > start_point[0]))
    x_array_difference = np.delete(x_array, np.where(x_array > start_point[0]))
    print('x_array_difference', x_array_difference)
    print('y_array_difference', y_array_difference)

    while True:
        if np.size(y_output_array) > 0:
            list_of_angle = list()
            for i in range(0, len(x_array_difference)):
                point_1 = (x_array_difference[i], y_array_difference[i])
                # print('point_1', point_1)
                point_2 = (np.max(x_array), y_output_array[0])
                # print('point_2', point_2)
                point_3 = (x_output_array[-1], y_output_array[-1])
                # print('point_3', point_3)
                list_of_angle.append(calculate_of_cos(point_1, point_2, point_3))
            print('list_of_angle', list_of_angle, type(list_of_angle))

            list_of_angle_in_degrees = np.arccos(list_of_angle) * 180 / np.pi
            print('list_of_angle_in_degrees', list_of_angle_in_degrees, type(list_of_angle_in_degrees))
            # print('Вывод максимального угла в градусах - ', np.max(list_of_angle_in_degrees))
            index_next_point = np.where(list_of_angle_in_degrees == np.max(list_of_angle_in_degrees))
            print('index_next_point', index_next_point)
            next_point = np.int(x_array_difference[index_next_point]), np.int(y_array_difference[index_next_point])
            print('next_point', next_point)

            # x_output_array = np.append(x_output_array, next_point[0])
            # y_output_array = np.append(y_output_array, next_point[1])
            # print('x_output_array', x_output_array)
            # print('y_output_array', y_output_array)

            # x_condition = np.size(np.where(x_array_difference == next_point[0]))
            # print('x_condition', x_condition)
            # y_condition = np.size(np.where(y_array_difference == next_point[1]))
            # print('y_condition', y_condition)
            if next_point[0] == min_x_coordinate:
                print('Зашли в проверку - next_point[0] == min_x_coordinate: сработал break')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                print('x_output_array при одном значении', x_output_array)
                print('y_output_array при одном значении', y_output_array)
                break
            else:
                print('Зашли в проверку else в условии - if next_point[0] == min_x_coordinate:')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                print('x_output_array при одном значении', x_output_array)
                print('y_output_array при одном значении', y_output_array)

    print('!!! x_output_array после проверки Х на максимум > ', x_output_array, ' > !!!')
    print('!!! x_output_array после проверки X на максимум > ', y_output_array, ' > !!!')

    start_point_for_next_step = np.array([x_output_array[-1], y_output_array[-1]])
    print('start_point_for_next_step', start_point_for_next_step, '\n')

    return x_output_array, y_output_array, start_point_for_next_step


def draw_going_from_left_to_right_and_down_lines(x_array, y_array,
                                                 max_y_coordinate, max_x_coordinate, start_point):
    print('Запуск функции движения слева на права и вниз "draw_going_from_left_to_right_and_down_lines"')
    print('max_y_coordinate', max_y_coordinate)
    print('max_x_coordinate', max_x_coordinate)

    x_output_array = np.array([start_point[0]])
    y_output_array = np.array([start_point[1]])

    print('!!! x_output_array < ', x_output_array, ' > !!!')
    print('!!! y_output_array < ', y_output_array, ' > !!!')

    next_point = np.array([])
    x_array_difference = np.delete(x_array, np.where(x_array < start_point[0]))
    y_array_difference = np.delete(y_array, np.where(x_array < start_point[0]))
    print('x_array_difference', x_array_difference)
    print('y_array_difference', y_array_difference)

    while True:
        if np.size(y_output_array) > 0:
            list_of_angle = list()
            for i in range(0, len(x_array_difference)):
                point_1 = (x_array_difference[i], y_array_difference[i])
                # print('point_1', point_1)
                point_2 = (0, y_output_array[-1])
                # print('point_2', point_2)
                point_3 = (x_output_array[-1], y_output_array[-1])
                # print('point_3', point_3)
                list_of_angle.append(calculate_of_cos(point_1, point_2, point_3))
            print('list_of_angle', list_of_angle, type(list_of_angle))

            list_of_angle_in_degrees = np.arccos(list_of_angle) * 180 / np.pi
            print('list_of_angle_in_degrees', list_of_angle_in_degrees, type(list_of_angle_in_degrees))
            # print('Вывод максимального угла в градусах - ', np.max(list_of_angle_in_degrees))
            index_next_point = np.where(list_of_angle_in_degrees == np.max(list_of_angle_in_degrees))
            print('index_next_point', index_next_point)
            next_point = np.int(x_array_difference[index_next_point]), np.int(y_array_difference[index_next_point])
            print('next_point', next_point)

            x_drawing_array = np.append(x_output_array, next_point[0])
            y_drawing_array = np.append(y_output_array, next_point[1])
            print('x_output_array', x_output_array)
            print('y_output_array', y_output_array)

            # x_condition = np.size(np.where(x_array_difference == next_point[0]))
            # print('x_condition', x_condition)
            # y_condition = np.size(np.where(y_array_difference == next_point[1]))
            # print('y_condition', y_condition)
            if next_point[0] == max_x_coordinate:
                print('Зашли в проверку - if next_point[0] == max_x_coordinate:')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                # print('x_array_difference при одном значении', x_array_difference)
                print('x_output_array при одном значении', x_output_array)
                # print('y_array_difference при одном значении', y_array_difference)
                print('y_output_array при одном значении', y_output_array)
                break
            else:
                print('Зашли в проверку else в условии - if next_point[0] == max_x_coordinate:')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                # print('x_output_array при одном значении', x_output_array)
                # print('y_output_array при одном значении', y_output_array)

    # Отрисовка линий, без расчетов, если есть одинаковые крайние точки.
    print('Количество повторяющихся элементов с максимальным "Х" ', np.size(np.where(x_array == np.max(x_array))))
    if np.size(np.where(x_array == np.max(x_array))) > 0:
        x_array_difference = np.arange(0, np.size(np.where(x_array == np.max(x_array))))
        for j in range(0, np.size(y_array[np.where(x_array == np.max(x_array))])):
            x_array_difference[j] = max_x_coordinate
        y_array_difference = np.array(y_array[np.where(x_array == np.max(x_array))])
        y_array_difference = np.sort(y_array_difference)
        y_array_difference = y_array_difference[::-1]
        print('x_array_difference', x_array_difference)
        print('y_array_difference', y_array_difference)

        x_output_array = np.delete(x_output_array, -1)
        x_output_array = np.delete(x_output_array, 0)
        y_output_array = np.delete(y_output_array, -1)
        y_output_array = np.delete(y_output_array, 0)

        x_output_array = np.append(x_output_array, x_array_difference)
        y_output_array = np.append(y_output_array, y_array_difference)

    else:
        x_output_array = np.array(np.min(x_array))
        y_output_array = np.array(y_array[np.where(x_array == np.min(x_array))])

    print('!!! x_output_array после проверки Х на максимум > ', x_output_array, ' > !!!')
    print('!!! x_output_array после проверки X на максимум > ', y_output_array, ' > !!!')

    start_point_for_next_step = np.array([x_output_array[-1], y_output_array[-1]])
    print('start_point_for_next_step', start_point_for_next_step, '\n')

    return x_output_array, y_output_array, start_point_for_next_step


def draw_going_from_right_to_left_and_down_lines(x_array, y_array,
                                                 max_x_coordinate, min_y_coordinate, start_point):
    print('Запуск функции движения с права на лево вниз "draw_going_from_right_to_down_lines"')
    print('max_x_coordinate', max_x_coordinate)
    print('min_y_coordinate', min_y_coordinate)

    x_output_array = np.array([start_point[0]])
    y_output_array = np.array([start_point[1]])

    print('!!! x_output_array < ', x_output_array, ' > !!!')
    print('!!! y_output_array < ', y_output_array, ' > !!!')

    next_point = np.array([])
    x_array_difference = np.delete(x_array, np.where(y_array > start_point[1]))
    y_array_difference = np.delete(y_array, np.where(y_array > start_point[1]))
    print('x_array_difference', x_array_difference)
    print('y_array_difference', y_array_difference)

    while True:
        if np.size(y_output_array) > 0:
            list_of_angle = list()
            for i in range(0, len(x_array_difference)):
                point_1 = (x_array_difference[i], y_array_difference[i])
                # print('point_1', point_1)
                point_2 = (x_output_array[0], np.max(y_array))
                # print('point_2', point_2)
                point_3 = (x_output_array[-1], y_output_array[-1])
                # print('point_3', point_3)
                list_of_angle.append(calculate_of_cos(point_1, point_2, point_3))
            print('list_of_angle', list_of_angle)

            list_of_angle_in_degrees = np.arccos(list_of_angle) * 180 / np.pi
            print('list_of_angle_in_degrees', list_of_angle_in_degrees, type(list_of_angle_in_degrees))
            # print('Вывод максимального угла в градусах - ', np.max(list_of_angle_in_degrees))
            index_next_point = np.where(list_of_angle_in_degrees == np.max(list_of_angle_in_degrees))
            print('index_next_point', index_next_point)
            next_point = np.int(x_array_difference[index_next_point]), np.int(y_array_difference[index_next_point])
            print('next_point', next_point)

            # x_output_array = np.append(x_output_array, next_point[0])
            # y_output_array = np.append(y_output_array, next_point[1])
            # print('x_output_array', x_output_array)
            # print('y_output_array', y_output_array)

            # x_condition = np.size(np.where(x_array_difference == next_point[0]))
            # print('x_condition', x_condition)
            # y_condition = np.size(np.where(y_array_difference == next_point[1]))
            # print('y_condition', y_condition)
            if next_point[0] == x_array[0] and next_point[1] == y_array[0]:
                print('Координата следубщей точки равна минимальному Y.')
                break

            elif next_point[1] == min_y_coordinate:
                print('Зашли в проверку - elif next_point[1] == min_y_coordinate')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                # print('x_array_difference при одном значении', x_array_difference)
                print('x_output_array при одном значении', x_output_array)
                # print('y_array_difference при одном значении', y_array_difference)
                print('y_output_array при одном значении', y_output_array)
                break

            else:
                print('Зашли в проверку else в условии - next_point[1] != min_y_coordinate')
                x_output_array = np.append(x_output_array, next_point[0])
                y_output_array = np.append(y_output_array, next_point[1])
                print('x_output_array при одном значении', x_output_array)
                print('y_output_array при одном значении', y_output_array)

    # Отрисовка линий, без расчетов, если есть одинаковые крайние точки.
    print('Количество повторяющихся элементов с минимальным "Y" ', np.size(np.where(y_array == np.min(y_array))))
    if np.size(np.where(y_array == np.min(y_array))) > 1:
        y_array_difference = np.arange(0, np.size(np.where(y_array == np.min(y_array))))
        for j in range(0, np.size(y_array[np.where(y_array == np.min(y_array))])):
            y_array_difference[j] = min_y_coordinate
        x_array_difference = np.array(x_array[np.where(y_array == np.min(y_array))])
        x_array_difference = np.sort(x_array_difference)
        x_array_difference = x_array_difference[::-1]
        print('x_array_difference', x_array_difference)
        print('y_array_difference', y_array_difference)

        x_output_array = np.delete(x_output_array, -1)
        x_output_array = np.delete(x_output_array, 0)
        y_output_array = np.delete(y_output_array, -1)
        y_output_array = np.delete(y_output_array, 0)

        x_output_array = np.append(x_output_array, x_array_difference)
        y_output_array = np.append(y_output_array, y_array_difference)

    else:
        np.append(x_output_array, next_point[0])
        np.append(y_output_array, next_point[0])

    print('!!! x_output_array после проверки Х на минимум < ', x_output_array, ' > !!!')
    print('!!! x_output_array после проверки X на минимум < ', y_output_array, ' > !!!')

    start_point_for_next_step = np.array([x_output_array[-1], y_output_array[-1]])
    print('start_point_for_next_step', start_point_for_next_step, '\n')

    return x_output_array, y_output_array, start_point_for_next_step


def calculate_of_cos(point_one, point_two, point_base):
    print('Запуск функции "calculate_of_cos"')
    # print('point_one, point_two, point_base', point_one, point_two, point_base)
    vector_one = (point_one[0] - point_base[0], point_one[1] - point_base[1])
    # print('vector_one', vector_one)
    vector_two = (point_two[0] - point_base[0], point_two[1] - point_base[1])
    # print('vector_two', vector_two)
    scalar_multiplication = np.int(np.inner(vector_one, vector_two))
    # print('-- scalar_multiplication', scalar_multiplication, type(scalar_multiplication))
    length_of_vector_one = (((point_one[0] - point_base[0]) ** 2) + (point_one[1] - point_base[1]) ** 2) ** 0.5
    length_of_vector_two = (((point_two[0] - point_base[0]) ** 2) + (point_two[1] - point_base[1]) ** 2) ** 0.5
    multiply_of_vector = length_of_vector_one * length_of_vector_two
    # print('-- multiply_of_vector ', multiply_of_vector)
    if multiply_of_vector != 0 and scalar_multiplication != 0:
        cos_between_points = scalar_multiplication / multiply_of_vector
    else:
        cos_between_points = 0
    # print('-- cos_between_points ', cos_between_points)

    return cos_between_points


def draw_going_from_left_to_right_and_up_lines(x_array, y_array, min_x_coordinate, max_y_coordinate):
    print('Запуск функции движения слева на право вверх - "draw_going_from_left_to_right_and_up_lines"')
    print('min_x_coordinate', min_x_coordinate)
    print('max_y_coordinate', max_y_coordinate)

    # Отрисовка линий, без расчетов, если есть одинаковые крайние точки.
    print('Количество повторяющихся элементов с минимальным "Х" ', np.size(np.where(x_array == np.min(x_array))))
    if np.size(np.where(x_array == np.min(x_array))) > 1:
        x_output_array = np.arange(0, np.size(np.where(x_array == np.min(x_array))))
        for j in range(0, np.size(y_array[np.where(x_array == np.min(x_array))])):
            x_output_array[j] = min_x_coordinate
        y_output_array = np.array(y_array[np.where(x_array == np.min(x_array))])
        y_output_array = np.sort(y_output_array)

    else:
        x_output_array = np.array([np.min(x_array)])
        y_output_array = np.array(y_array[np.where(x_array == np.min(x_array))])

    print('!!! x_output_array после проверки Х на минимум < ', x_output_array, ' > !!!')
    print('!!! y_output_array после проверки X на минимум < ', y_output_array, ' > !!!')

    # Закончили с определением крайних экстремумов, дальше расчитываем следующие точки, где угол будет максимальным

    print('np.size(x_output_array - ) ', np.size(x_output_array))
    next_point = np.array([])
    x_array_difference = np.copy(x_array)
    y_array_difference = np.copy(y_array)
    print('np.where(x_array == min_x_coordinate)', np.where(x_array == min_x_coordinate))
    x_array_difference = np.delete(x_array_difference, np.where(x_array == min_x_coordinate))
    y_array_difference = np.delete(y_array_difference, np.where(x_array == min_x_coordinate))
    print('x_array_difference', x_array_difference)
    print('y_array_difference', y_array_difference)

    while True:
        if np.size(y_output_array) > 0:
            list_of_angle = list()
            for i in range(0, len(x_array_difference)):
                point_1 = (x_array_difference[i], y_array_difference[i])
                # print('point_1', point_1)
                point_2 = (x_output_array[-1], 0)
                # print('point_2', point_2)
                point_3 = (x_output_array[-1], y_output_array[-1])
                # print('point_3', point_3)
                list_of_angle.append(calculate_of_cos(point_1, point_2, point_3))
            print('list_of_angle', list_of_angle, type(list_of_angle))

            list_of_angle_in_degrees = np.arccos(list_of_angle) * 180 / np.pi
            print('list_of_angle_in_degrees', list_of_angle_in_degrees, type(list_of_angle_in_degrees))
            # print('Вывод максимального угла в градусах - ', np.max(list_of_angle_in_degrees))
            index_next_point = np.where(list_of_angle_in_degrees == np.max(list_of_angle_in_degrees))
            print('index_next_point', index_next_point)
            next_point = np.int(x_array_difference[index_next_point]), np.int(y_array_difference[index_next_point])
            print('next_point', next_point)

            x_output_array = np.append(x_output_array, next_point[0])
            y_output_array = np.append(y_output_array, next_point[1])
            print('x_output_array', x_output_array)
            print('y_output_array', y_output_array)

        x_condition = np.size(np.where(x_array_difference == next_point[0]))
        print('x_condition', x_condition)
        y_condition = np.size(np.where(y_array_difference == next_point[1]))
        print('y_condition', y_condition)
        if np.size(y_array_difference) == 1:
            break
        elif x_condition > 1:
            x_array_difference = np.delete(x_array_difference, np.where(y_array_difference == next_point[1]))
            y_array_difference = np.delete(y_array_difference, np.where(y_array_difference == next_point[1]))
            print('x_array_difference при больше чем одно значении у Х ', x_array_difference)
            print('y_array_difference при больше чем одно значении у Х ', y_array_difference)
        elif y_condition > 1:
            print('x_array_difference', x_array_difference)
            print('y_array_difference', y_array_difference)
            print('np.where(x_array_difference == next_point[0]) = ', np.where(x_array_difference == next_point[0]))
            print('np.delete(y_array_difference, np.where(x_array_difference == next_point[0]))',
                  np.delete(y_array_difference, np.where(x_array_difference == next_point[0])))
            print(next_point[0])
            print(next_point[1])
            y_array_difference = np.delete(y_array_difference, np.where(x_array_difference == next_point[0]))
            x_array_difference = np.delete(x_array_difference, np.where(x_array_difference == next_point[0]))
            print('x_array_difference при больше чем одно значении у Y ', x_array_difference)
            print('y_array_difference при больше чем одно значении у Y ', y_array_difference)
        else:
            x_array_difference = np.delete(x_array_difference, np.where(x_array_difference == next_point[0]))
            y_array_difference = np.delete(y_array_difference, np.where(y_array_difference == next_point[1]))
            print('x_array_difference при одном значении', x_array_difference)
            print('y_array_difference при одном значении', y_array_difference)
        if next_point[1] == max_y_coordinate:
            break

    print('Количество повторяющихся элементов с максимальным "Y" ', np.size(np.where(y_array == np.max(y_array))))
    if np.size(np.where(y_array == np.max(y_array))) > 1:
        x_storage_of_extremum = np.arange(0, np.size(np.where(y_array == np.max(y_array))))
        y_storage_of_extremum = np.arange(0, np.size(np.where(y_array == np.max(y_array))))
        for k in range(0, np.size(x_array[np.where(y_array == np.max(y_array))])):
            y_storage_of_extremum[k] = np.max(y_array)
            x_storage_of_extremum = np.array(x_array[np.where(y_array == np.max(y_array))])
            # x_storage_of_extremum = np.sort(x_storage_of_extremum)
        print('Массив X до удаления повторяющихся элементов x_storage_of_extremum - ', x_storage_of_extremum)
        print('Массив Y до удаления повторяющихся элементов y_storage_of_extremum', y_storage_of_extremum)
        for m in x_storage_of_extremum:
            print('Значение m - ', m)
            print('Проверка на нахождение алогичных точек в двух массивах - ',
                  m in x_output_array)
            if m in x_output_array:
                print('Зашли в цикл удаления повторяющихся элементов.')
                y_storage_of_extremum = np.delete(y_storage_of_extremum, 0)
                x_storage_of_extremum = np.delete(x_storage_of_extremum, np.where(x_storage_of_extremum == m))
        print('Массив X после удаления повторяющихся элементов x_storage_of_extremum', x_storage_of_extremum)
        print('Массив Y после удаления повторяющихся элементов y_storage_of_extremum', y_storage_of_extremum)
        x_output_array = np.sort(x_output_array)
        print('Отсортированный массив x_storage_of_extremum - ', x_storage_of_extremum)

        x_output_array = np.concatenate([x_output_array, x_storage_of_extremum])
        y_output_array = np.concatenate([y_output_array, y_storage_of_extremum])

    else:
        y_output_array = np.append(y_output_array, next_point[1])
        x_output_array = np.append(x_output_array, next_point[0])

    print('!!! x_output_array после проверки Y на минимум < ', x_output_array, ' > !!!')
    print('!!! y_output_array после проверки Y на минимум < ', y_output_array, ' > !!!')

    start_point_for_next_step = np.array([x_output_array[-1], y_output_array[-1]])
    print('start_point_for_next_step', start_point_for_next_step, '\n')

    return x_output_array, y_output_array, start_point_for_next_step


def draw_spanning_line(x_array, y_array):
    # Рисуем восходящие линии слева на право
    max_x_coordinate = np.max(x_array)
    min_x_coordinate = np.min(x_array)
    max_y_coordinate = np.max(y_array)
    min_y_coordinate = np.min(y_array)

    x_array_output_points = np.array([])
    y_array_output_points = np.array([])

    x_array_output_points, y_array_output_points, start_point_for_next_step = \
        draw_going_from_left_to_right_and_up_lines(x_array, y_array, min_x_coordinate, max_y_coordinate)
    print('x_array_output_points после выполнения функции draw_going_from_left_to_up_lines',
          x_array_output_points)
    print('y_array_output_points после выполнения функции draw_going_from_left_to_up_lines',
          y_array_output_points, '\n')
    x, y, start_point_for_next_step = \
        draw_going_from_left_to_right_and_down_lines(x_array, y_array,
                                                     max_y_coordinate, max_x_coordinate, start_point_for_next_step)
    x_array_output_points = np.append(x_array_output_points, x)
    y_array_output_points = np.append(y_array_output_points, y)

    x2, y2, start_point_for_next_step = \
        draw_going_from_right_to_left_and_down_lines(x_array, y_array,
                                                     max_x_coordinate, min_y_coordinate, start_point_for_next_step)

    x_array_output_points = np.append(x_array_output_points, x2)
    y_array_output_points = np.append(y_array_output_points, y2)

    x3, y3, start_point_for_next_step = \
        draw_going_from_right_to_left_and_up_lines(x_array, y_array,
                                                   min_x_coordinate, min_y_coordinate, start_point_for_next_step)

    x_array_output_points = np.append(x_array_output_points, x3)
    y_array_output_points = np.append(y_array_output_points, y3)

    if start_point_for_next_step[0] != x_array_output_points[0] \
            and start_point_for_next_step[1] != y_array_output_points[1]:
        x_array_output_points = np.append(x_array_output_points, x_array_output_points[0])
        y_array_output_points = np.append(y_array_output_points, y_array_output_points[0])

    print('ФИНАЛ - x_array_output_points', x_array_output_points)
    print('ФИНАЛ - y_array_output_points', y_array_output_points)

    plt.plot(x_array_output_points, y_array_output_points)


# Прорисовка с использованием массивов Numpy
def draw_points_and_lines():
    # x_coordinates_of_points = np.random.randint(20, 300, count_of_points)
    # np.random.shuffle(x_coordinates_of_points)
    # y_coordinates_of_points = np.random.randint(20, 300, count_of_points)
    # np.random.shuffle(y_coordinates_of_points)
    plt.scatter(x_coordinates_of_points, y_coordinates_of_points)

    # Подписываем номера точек
    for i in range(np.size(x_coordinates_of_points)):
        s = i + 1
        plt.text(x_coordinates_of_points[i] + 2, y_coordinates_of_points[i] + 2, s, color='black', fontsize=20)

    draw_spanning_line(x_coordinates_of_points, y_coordinates_of_points)

    plt.show()

    return x_coordinates_of_points, y_coordinates_of_points

# Измерение времени модулем timer
# start_time = time.time()
# draw_points_and_lines()
# print ("{:g} s".format(time.time() - start_time))

# Измерение времени модулем timeit
# my_timer = timeit.timeit(draw_points_and_lines, number=10)
# print('my_timer', my_timer)


work_dict_of_points_cloud = draw_points_and_lines()
# print('work_dict_of_points_cloud', work_dict_of_points_cloud, type(work_dict_of_points_cloud))
