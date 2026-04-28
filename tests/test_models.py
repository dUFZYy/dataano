from src.models import Task, User

def test_task_creation():
    t = Task("Buy milk")
    assert t.title == "Buy milk"
    assert t.status == "pending"

def test_task_complete():
    t = Task("Do laundry")
    t.complete()
    assert t.status == "completed"

# TODO: Add tests for User dataclass
# TODO: Add tests for Task.to_dict serialization
