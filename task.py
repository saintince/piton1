import json
import os
import re
class Task:
    def __init__(self, title, description,deadline, id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.id = id

    def __str__(self):
        return f"Задача: №{self.id}\n{self.title}\n{self.description}\n{self.deadline}"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "id": self.id
        }

def save_task(task):
    filename = "tasks.json"

    if os.path.exists(filename):
        with open(filename,"r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks =[]

    tasks.append(task.to_dict())

    with open(filename,"w", encoding="utf-8") as f:
        json.dump(tasks,f,indent=4,ensure_ascii=False)



def choose():
    t = str(input("Введите название:\n"))
    d = str(input("Введите описание:\n"))

    while True:
        dl = str(input("Введите дедлайн (YY.MM.DD):\n"))
        dl_pattern = r"\d{2}\.\d{2}\.\d{2}"
        if re.fullmatch(dl_pattern,dl): break
        else: print("Ошибка: введите корректную дату в формате YY.MM.DD")


    while True:
        try:
            i = int(input("Введите id: "))
            break
        except ValueError: print("Ошибка: id должен быть числом!")

    task = Task(t,d,dl,i)
    print(task)

    save_task(task)
    print("Задача добавлена!")
    return task





