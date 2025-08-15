class Task:
    def __init__(self, title, description, deadline, status):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return f"Task: {self.title},\n{self.description},\n {self.deadline},\n {self.status}"
def choose():
    t = str(input("Введите название:\n"))
    d = str(input("Введите описание:\n"))
    dl = str(input("Введите дедлайн (YYYY-MM-DD):\n"))
    s = str(input("Введите статус вашей задачи(либо:\n"))
    func = Task(f"{t}",{d},{dl},{s})
    print(func)

choose()



