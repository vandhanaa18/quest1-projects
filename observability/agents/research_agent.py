class ResearchAgent:

    def run(self, workflow):

        try:

            print("\n===== Research Agent =====")

            task = workflow.task
            plan = workflow.plan

            research = f"""
Task: {task}

Research Notes:
- Follow the planner's steps carefully.
- Write clean and modular Python code.
- Use meaningful variable and function names.
- Include exception handling where required.
- Test the code before final submission.

Planner Output:
{plan}
"""

            workflow.research = research

            print("Research completed.")

            return workflow

        except Exception as e:

            workflow.errors.append(
                f"ResearchAgent: {str(e)}"
            )

            print("Research Agent failed.")

            raise