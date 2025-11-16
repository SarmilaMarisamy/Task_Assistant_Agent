import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_task_agent(tasks):
    """
    Very simple agent: prioritizes and plans tasks.
    """

    prompt = f"""
You are a simple productivity assistant.
Given these tasks: {tasks}

1. Prioritize them (High, Medium, Low)
2. Create a step-by-step plan for the day
3. Keep it short and clear
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content

# ---------- MAIN APP ----------
if __name__ == "__main__":
    print("Task Assistant Agent")
    tasks = input("Enter tasks separated by commas: ")
    tasks_list = [t.strip() for t in tasks.split(",")]

    result = simple_task_agent(tasks_list)
    print("\n----- Agent Output -----")
    print(result)
