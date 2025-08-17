import task
import function

while True:
    try:
        ch = int(input("1 - Создать\n2 - Показать\n3 - Найти\n4 - Удалить\nВыберите один из этих вариантов: "))

        if ch == 1: task.choose()
        if ch == 2: function.get_zad()
        if ch == 3: function.search()
        if ch == 4: function.delete()
    except ValueError:
        print("Ошибка: введите один из вариантов ответа!")



