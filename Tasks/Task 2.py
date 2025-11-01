#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввод элементов списка
    a_list = list(map(float, input("Введите элементы списка: ").split()))

    # Границы сжатия списка
    print("Введите значения для сжатия списка: ")
    left_border = float(input("Левая граница списка: "))
    right_border = float(input("Правая граница списка: "))

    # Проверка корректности границ
    if left_border == right_border:
        print("Неверно введённые границы", file=sys.stderr)
        exit(1)

    print(f"Максимальный элемент списка до сжатия: {max(a_list)}")

    # Вычисление индекса последнего положительного элемента
    stop_index = 0
    for idx in reversed(range(len(a_list))):
        if a_list[idx] > 0:
            stop_index = idx + 1
            break

    # Вычисление суммы списка до последнего положительного элемента
    total_sum = sum(a_list[:stop_index])
    print(
        f"Сумма элементов списка до сжатия, расположенных до "
        f"последнего положительного элемента: {total_sum}"
    )

    # Цикл сжатия списка
    n = len(a_list)
    processed = 0
    i = 0
    while processed < n:
        if left_border <= a_list[i] <= right_border:
            a_list.pop(i)
            a_list.append(0)
        else:
            i += 1
        processed += 1

    print(f"Сжатый список: {a_list}")
