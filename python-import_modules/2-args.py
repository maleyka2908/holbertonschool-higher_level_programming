#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Proqramın adını (argv[0]) siyahıdan çıxarırıq
    count = len(argv)

    # Başlıq hissəsinin çapı
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Arqumentlərin siyahısı
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
