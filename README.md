# Task Assistant Agent

**AI Task Management Agent** – Beginner-friendly agent built for the Kaggle 5-Day AI Agents Capstone (Freestyle Track).

---

## Project Overview
Managing daily tasks manually can be tedious and often leads to mis-prioritization or missed deadlines. The **AI Task Management Agent** is an intelligent assistant that helps users **manage, prioritize, and organize tasks efficiently**.  

It leverages a **language model (LLM)** to analyze task descriptions and automatically assign priority levels (high, medium, low), while allowing users to perform all task operations through simple natural language commands.

---

## Key Features
- **Add tasks**: Add a task in natural language; the agent analyzes and assigns priority automatically.
- **Update tasks**: Rename tasks or change priority.
- **Delete tasks**: Remove tasks from the system.
- **Complete tasks**: Mark tasks as completed.
- **List tasks**: View all tasks along with priority and status.
- **Prioritize tasks**: Sort tasks by priority automatically.
- **Memory & persistence**: Tasks are saved in `task_db.json` to retain information between sessions.

---

## Installation

1. Clone this repository:
```bash
git clone https://github.com/SarmilaMarisamy/Task_Assistant_Agent.git
cd Task_Assistant_Agent
2. Install dependencies:
pip install -r requirements.txt
Set your OpenAI API key in your environment:
export OPENAI_API_KEY="your_api_key_here"   # Linux/Mac
setx OPENAI_API_KEY "your_api_key_here"      # Windows

## Usage

1. Run the agent:
python main.py
2. Example Commands:
add task: Buy groceries
update task Buy groceries set priority high
delete task Buy groceries
complete task Buy groceries
list tasks
prioritize tasks


The agent will respond with the appropriate action, automatically reasoning about priority and updating the task database.

