import heapq
import uuid
from datetime import datetime

class Task:
    def __init__(self, title, priority, deadline=None):
        self.id = str(uuid.uuid4())  
        self.title = title
        self.priority = priority  # lower number = higher priority
        self.deadline = deadline if deadline else datetime.now()

    def __lt__(self, other):
        """Compare tasks by priority, then deadline."""
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.title}, Priority={self.priority}, Deadline={self.deadline})"


class TaskManager:
    def __init__(self):
        self.task_heap = []  # min-heap for priority scheduling
        self.task_map = {}   # dictionary for quick lookup

    def add_task(self, task):
        heapq.heappush(self.task_heap, task)
        self.task_map[task.id] = task

    def get_next_task(self):
        """get the highest priority task."""
        if self.task_heap:
            task = heapq.heappop(self.task_heap)
            self.task_map.pop(task.id, None)
            return task
        return None

    def peek_next_task(self):
        """View the next task without removing it."""
        return self.task_heap[0] if self.task_heap else None

    def remove_task(self, task_id):
        """Remove a task by ID ."""
        if task_id in self.task_map:
            task = self.task_map.pop(task_id)
            # Rebuild heap without the removed task
            self.task_heap = [t for t in self.task_heap if t.id != task_id]
            heapq.heapify(self.task_heap)
            return task
        return None

    def list_tasks(self):
        """Return all tasks sorted by priority."""
        return sorted(self.task_heap)


#  usage
if __name__ == "__main__":
    manager = TaskManager()

    t1 = Task("Finish report", 1, datetime(2025, 12, 6))
    t2 = Task("Email client", 2, datetime(2025, 12, 7))
    t3 = Task("Team meeting", 1, datetime(2025, 12, 5))

    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)

    print("All tasks:", manager.list_tasks())
    print("")
    print("Next task:", manager.peek_next_task())
    print("")
    print("Completing:", manager.get_next_task())
    print("")

    print("Remaining tasks:", manager.list_tasks())
