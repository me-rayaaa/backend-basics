from datetime import date

from src.exceptions import TaskNotFoundError
from src.logger import logger
from src.models import Task


def create_task(
    tasks_by_id: dict[int, Task],
    title: str,
    description: str,
    due_date: date,
) -> Task:
    task_id = max(tasks_by_id, default=0) + 1
    task = Task(
        id=task_id,
        title=title,
        description=description,
        due_date=due_date,
    )
    tasks_by_id[task_id] = task
    logger.info("Created task", extra={"task_id": task_id})
    return task


def get_task(
    tasks_by_id: dict[int, Task],
    task_id: int,
) -> Task:
    if task_id not in tasks_by_id:
        raise TaskNotFoundError(task_id)
    return tasks_by_id[task_id]
