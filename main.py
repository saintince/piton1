import task
import function

ch = int(input("1 - Создать\n2 - Показать\n3 - Редактировать\n4 - Найти\n5 - Удалить\nВыберите один из этих вариантов: "))

if ch == 1: print(task.choose())
if ch == 2: print(function.get_zad())

