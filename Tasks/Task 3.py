#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввод кортежа
    a_tuple = tuple(map(int, input("Введите кортеж: ").split()))

    # Вычисление индекса начала вывода
    start_idx = 0
    a_start = a_tuple[1:]
    a_end = a_tuple[:-1]
    for i, (a1, a2) in enumerate(zip(a_start, a_end)):
        if a1 == a2:
            start_idx = i + 2
            break

    print(
        f"Элементы после первой пары одинаковых чисел:"
        f"{a_tuple[start_idx:]}"
    )
