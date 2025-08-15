import json

def get_zad():
    with open("tasks.json","r", encoding="utf-8") as file:
        tasks = json.load(file)
    k = 1

    for task in tasks:
        print(f"[{k}] Название: {task['title']}")
        print(f"Описание: {task['description']}")
        print(f"Дедлайн: {task['deadline']}")
        print("-" * 30)
        k +=1

