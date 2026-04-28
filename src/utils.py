def format_task_title(title: str) -> str:
    """Formats the title to be capitalized."""
    return title.capitalize()

def validateTask(task):
    # Inconsistency: camelCase function name, no type hints
    if not task.title:
        return False
    if len(task.title) > 100:
        return False
    
    # Missing checks for description length, status validity, etc.
    return True
