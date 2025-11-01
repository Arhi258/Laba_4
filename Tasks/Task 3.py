#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввод кортежа
    a_tuple = tuple(map(int, input("Введите кортеж: ").split()))

    # Вычисление индекса начала вывода
    start_idx = 0
    for i in range(len(a_tuple) - 1):
        if a_tuple[i] == a_tuple[i + 1]:
            start_idx = i + 2
            break

    print(
        f"Элементы после первой пары одинаковых чисел:"
        f"{a_tuple[start_idx:]}"
    )
