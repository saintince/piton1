import json

def get_zad():
    with open("tasks.json","r", encoding="utf-8") as file:
        tasks = json.load(file)
    k = 1

    for task in tasks:
        print(f"[{k}] Название: {task['title']}")
        k +=1
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
            print(f"Найдено!\n[{k}]Название: {task['title']}\nОписание: {task['description']}\nДедлайн: {task['deadline']}")


