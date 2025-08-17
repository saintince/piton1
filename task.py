import json
import os
class Task:
    def __init__(self, title, description, deadline, id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.id = id

    def __str__(self):
        return f"Task: {self.title}\n{self.description}\n{self.deadline}\n{self.id}"

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
    dl = str(input("Введите дедлайн (YY-MM-DD):\n"))
    i = int(input("Введите id: "))
    task = Task(t,d,dl)
    print(task)

    save_task(task)
    print("Задача добавлена!")





