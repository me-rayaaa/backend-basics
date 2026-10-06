from datetime import date

from src.models import Task
from src.services import create_task, get_task


def main() -> None:
    tasks_by_id: dict[int, Task] = {}
    task = create_task(
        tasks_by_id,
        title="Подготовить README",
        description="Добавить инструкцию запуска проекта",
        due_date=date(2027, 6, 30),
    )
    print(get_task(tasks_by_id, task.id))


if __name__ == "__main__":
    main()
