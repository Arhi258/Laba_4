#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввод списка
    a_list = list(map(int, input("Введите 10 элементов списка: ").split()))

    # Проверка размера списка
    if len(a_list) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    s = sum(a for a in a_list if 3 < abs(a) < 8)
    print(f"Сумма элементов больших 3 и меньших 8 равна: {s}")
