import task
import function
while True:
    ch = int(input("1 - Создать\n2 - Показать\n3 - Найти\n4 - Удалить\nВыберите один из этих вариантов: "))

    if ch == 1: print(task.choose())
    if ch == 2: print(function.get_zad())
    if ch == 3: print(function.search())
    if ch == 4: print(function.delete())


