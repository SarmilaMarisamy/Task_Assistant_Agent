Project Overview

Managing daily tasks manually can be tedious and often leads to missed deadlines or mis-prioritized work. The Task Assistant Agent is an intelligent assistant that helps users add, update, delete, complete, and prioritize tasks efficiently. The agent uses AI reasoning to automatically decide the priority of tasks and organizes them for the user.

Key Features

Add tasks: Users can add tasks in natural language, e.g., "add task: Buy groceries". The agent assigns a priority automatically (high, medium, low).

Update tasks: Change the title or priority of existing tasks.

Delete tasks: Remove tasks from the system.

Complete tasks: Mark tasks as completed.

List tasks: View all tasks with their title, priority, and status.

Prioritize tasks: Sort tasks by priority automatically.

Persistent memory: Tasks are stored in task_db.json to keep track of them between sessions.

How It Works

The agent reads your natural language input.

If needed, it calls a tool function (add_task, update_task, etc.) to act on the task database.

Uses a language model (LLM) to analyze the task description and classify priority.

Updates the JSON database and responds back to the user.

This loop allows the agent to reason, act, and remember, which makes it a simple yet effective AI Agent.

Getting Started

Clone the repository or download the project folder.

Install dependencies:

pip install -r requirements.txt


Run the agent:

python main.py


First run: task_db.json will be automatically created if it doesn’t exist.

Commands examples:

add task: Finish report

update task Finish report set priority high

delete task Finish report

complete task Finish report

list tasks

prioritize tasks

Value Proposition

Reduces manual effort in task management.

Helps users focus on high-priority tasks.

Improves productivity by automating task prioritization.

Demonstrates AI reasoning, tool usage, and memory management.

Optional Demo
You: add task: Buy groceries
Agent: Task added: Buy groceries (priority: medium)

You: add task: Submit assignment
Agent: Task added: Submit assignment (priority: high)

You: list tasks
Agent:
- Buy groceries (priority: medium, pending)
- Submit assignment (priority: high, pending)


This README.md is ready for GitHub or Kaggle submission and clearly explains your project for judges.
