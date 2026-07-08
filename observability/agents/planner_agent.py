from ollama import chat


class PlannerAgent:

    def run(self, task):

        try:

            prompt = f"""
You are a Supervisor Planner Agent.

User Task:
{task}

Your job is to create a detailed execution plan and assign work to:

1. Research Agent
2. Code Generator Agent
3. Reviewer Agent
4. Test Agent

Rules:
- Give 3 to 5 tasks for each agent
- Tasks must be short and specific
- Number each task
- Return only the plan
- Do not explain anything

Format:

Research Agent
1. Task
2. Task
3. Task

Code Generator Agent
1. Task
2. Task
3. Task

Reviewer Agent
1. Task
2. Task
3. Task

Test Agent
1. Task
2. Task
3. Task
"""

            response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            planner_output = response["message"]["content"]

            return {
                "task": task,
                "plan": planner_output
            }

        except Exception as e:

            print(f"Planner Agent failed: {e}")

            raise


if __name__ == "__main__":

    planner = PlannerAgent()

    task = input("Enter task: ")

    data = planner.run(task)

    print("\n" + "=" * 50)
    print("PLANNER EXECUTION PLAN")
    print("=" * 50 + "\n")

    print(data["plan"])