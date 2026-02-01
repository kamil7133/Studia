from enum import Enum

class Status(Enum):
    TODO = "Do zrobienia"
    IN_PROGRESS = "W trakcie"
    DONE = "Wykonane"

class Task:
    """
    Bazowa klasa reprezentująca zadanie.
    """
    def __init__(self, title: str, status: Status = Status.TODO):
        self.title = title
        self.status = status

class ToDo(Task):
    def __init__(self, title: str):
        super().__init__(title, Status.TODO)

class InProgress(Task):
    def __init__(self, title: str):
        super().__init__(title, Status.IN_PROGRESS)

class Done(Task):
    def __init__(self, title: str):
        super().__init__(title, Status.DONE)