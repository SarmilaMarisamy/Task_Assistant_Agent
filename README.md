# Task Assistant Agent

This is a beginner-friendly AI agent built from scratch using Python and OpenAI API.

## Features
- Takes a list of tasks
- Prioritizes the tasks
- Creates a simple plan for the day
- Works like a basic "concierge" assistant

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Add your OpenAI API key:
setx OPENAI_API_KEY "OPENAI_API_KEY"

3. Run the agent:
python agent.py

## Output

=== Task Assistant Agent ===

Enter your tasks for today (comma-separated):
Buy groceries, Finish report, Call manager, Clean room

--- Today’s Plan ---
1. Finish report  (High priority)
2. Call manager   (Medium priority)
3. Buy groceries  (Normal priority)
4. Clean room     (Low priority)

Suggestion:
Start with the most important tasks first.
Try to complete the top 2 tasks before afternoon.

