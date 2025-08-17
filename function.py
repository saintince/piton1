import json


def get_zad():
    with open("tasks.json","r", encoding="utf-8") as file:
        tasks = json.load(file)

    for task in tasks:
        print(f"[{task['id']}]Название: {task['title']}")
        print(f"Описание: {task['description']}")
        print(f"Дедлайн: {task['deadline']}")
        print("-" * 32)



def search():
    with open("tasks.json","r", encoding="utf-8") as file:
        tasks = json.load(file)

    a = str(input("Введите слово для поиска: "))
    ab = a.lower()

    for task in tasks:
        all_text = f"{task['title']} {task['description']}"

        if ab in all_text:
            print(f"Найдено!\n[{task['id']}]Название: {task['title']}\nОписание: {task['description']}\nДедлайн: {task['deadline']}")


def delete():
    try:
        with open("tasks.json","r",encoding="utf-8") as file:
            tasks = json.load(file)

        a = int(input("Введите id задачи, которую хотите удалить: "))
        tasks = [task for task in tasks if task.get("id") != a]

        with open("tasks.json","w",encoding="utf-8") as file:
            json.dump(tasks,file,indent=4,ensure_ascii=False)

        print(f"Задача №{a} - удалена!")

    except ValueError:
        print("Ошибка: введите id!")


