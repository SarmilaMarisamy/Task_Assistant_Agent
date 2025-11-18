import os
import json
from openai import OpenAI

client = OpenAI(api_key="OPEN_API_KEY") 

DB_FILE = "task_db.json"

def read_db():
    """Read tasks from JSON file; create if missing or empty."""
    if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) == 0:
        write_db([])
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        write_db([])
        return []

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)



def classify_priority(title):
    """Decide priority using LLM, fallback to rules if short task."""
    title_lower = title.lower()
    
    # Simple heuristics
    if any(word in title_lower for word in ["submit", "assignment", "deadline", "report", "urgent"]):
        return "high"
    elif any(word in title_lower for word in ["exercise", "clean", "read", "cook"]):
        return "low"
    elif len(title) < 5:
        return "low"
    else:
        return "medium"




def add_task(title, priority=None):
    tasks = read_db()
    if priority is None:
        priority = classify_priority(title)
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "status": "pending"
    }
    tasks.append(task)
    write_db(tasks)
    return f"Task added: {title} (priority: {priority})"

def update_task(task_id, new_title=None, new_priority=None):
    tasks = read_db()
    for task in tasks:
        if task["id"] == task_id:
            if new_title:
                task["title"] = new_title
            if new_priority:
                task["priority"] = new_priority
            write_db(tasks)
            return f"Task {task_id} updated."
    return f"Task {task_id} not found."

def delete_task(task_id):
    tasks = read_db()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    write_db(new_tasks)
    return f"Task {task_id} deleted."

def complete_task(task_id):
    tasks = read_db()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            write_db(tasks)
            return f"Task {task_id} marked as completed."
    return f"Task {task_id} not found."

def list_tasks():
    tasks = read_db()
    if not tasks:
        return "No tasks found."
    return "\n".join([f"{t['id']}. {t['title']} ({t['priority']}, {t['status']})" for t in tasks])

def prioritize_tasks():
    tasks = read_db()
    priority_order = {"high": 1, "medium": 2, "low": 3}
    tasks_sorted = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 2))
    if not tasks_sorted:
        return "No tasks found."
    return "\n".join([f"{t['id']}. {t['title']} ({t['priority']}, {t['status']})" for t in tasks_sorted])



def task_agent(user_input):
    """Parse user input and call the right function."""
    user_lower = user_input.lower()

    if user_lower.startswith("add task"):
        parts = user_input.split(":", 1)
        if len(parts) < 2:
            return "Provide task title after 'add task:'."
        title = parts[1].strip()
        return add_task(title)

    elif user_lower.startswith("update task"):
        try:
            segments = user_input.split(",")
            task_id = int(segments[0].split()[2])
            new_title = None
            new_priority = None
            for seg in segments[1:]:
                key, val = seg.split(":")
                key = key.strip().lower()
                val = val.strip()
                if key == "title":
                    new_title = val
                elif key == "priority":
                    new_priority = val.lower()
            return update_task(task_id, new_title, new_priority)
        except:
            return "Use format: update task <id>, title: New Title, priority: high/medium/low"

    elif user_lower.startswith("delete task"):
        try:
            task_id = int(user_input.split()[2])
            return delete_task(task_id)
        except:
            return "Use format: delete task <id>"

    elif user_lower.startswith("complete task"):
        try:
            task_id = int(user_input.split()[2])
            return complete_task(task_id)
        except:
            return "Use format: complete task <id>"

    elif "list tasks" in user_lower:
        return list_tasks()

    elif "prioritize tasks" in user_lower:
        return prioritize_tasks()

    return "Unknown command. Try add/update/delete/complete/list/prioritize."



if __name__ == "__main__":
    # Ensure DB file exists
    if not os.path.exists(DB_FILE):
        write_db([])

    print("AI Task Agent Ready!")
    print("Commands:")
    print(" - add task: Task title here")
    print(" - update task <id>, title: New Title, priority: high/medium/low")
    print(" - delete task <id>")
    print(" - complete task <id>")
    print(" - list tasks")
    print(" - prioritize tasks")

    while True:
        query = input("\nYou: ")
        print("Agent:", task_agent(query))
