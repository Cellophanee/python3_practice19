import os
import sys
class Worker:
    workers = dict()
    n = int(input("Скільки працівників ви хочете додати:"))
    for i in range(n):
        nm = input("Введіть ім'я:")
        vd = input("Введіть назву відділу:")
        ps = input("Введіть посаду:")
        ag = int(input("Введіть рік народження:"))
        sr = input("Введіть стаж роботи (в місяцях):")
        workers[nm] = vd, ps, ag, sr
        print('Додано!\n')
    while True:
        f = input('Що зробити?\n 1. Пошук працівника\n 2. Додати працівника\n 3. Видалити працівника\n 4. Вийти\n')
        if f == '1':
            if workers == {}:
                print('Спочатку додайте працівників!\n')
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                s = input("Впишіть будь-які дані працівника:")
                if s in workers:
                    print('Знайдено:\n',"Ім'я: {}\nНазва відділу: {}\nПосада: {}\nРік Народження: {}\nСтаж роботи: {}".format(nm, vd, ps, ag, sr))
                else:
                    print('Такого праціника не знайдено!\n')
                    os.execl(sys.executable, sys.executable, *sys.argv)
        elif f == '2':
            n = int(input("Скільки працівників ви хочете додати:"))
            for i in range(n):
                nm = input("Введіть ім'я:")
                vd = input("Введіть назву відділу:")
                ps = input("Введіть посаду:")
                ag = int(input("Введіть рік народження:"))
                sr = input("Введіть стаж роботи (в місяцях):")
                workers[nm] = vd, ps, ag, sr
                print('Додано!\n')
        if f == '3':
            if workers == {}:
                print('Спочатку додайте працівників!\n')
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                d = input("Якого працівника видалити?\n(введіть ім'я):")
                if d in workers:
                    del workers[d]
                    print('Працівника видалено!')
                else:
                    print('Такого праціника не існує!\n')
                    os.execl(sys.executable, sys.executable, *sys.argv)
        if f == '4':
            break
        if f >= '5':
            print('Такої команди не існує.\n')
            os.execl(sys.executable, sys.executable, *sys.argv)