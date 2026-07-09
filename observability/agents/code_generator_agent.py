from ollama import chat


class CodeGeneratorAgent:

    def run(self, workflow):

        try:

            print("\n===== Code Generator Agent =====")

            prompt = f"""
You are an expert Python developer.

Task:
{workflow.task}

Planner Output:
{workflow.plan}

Research Notes:
{workflow.research}

Generate clean Python code.

Requirements:
- Use functions.
- Add comments.
- Handle errors using try-except where appropriate.
- Return only the Python code.
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

            workflow.code = response["message"]["content"]

            print("Code generated.")

            return workflow

        except Exception as e:

            workflow.errors.append(
                f"CodeGeneratorAgent: {str(e)}"
            )

            print("Code Generator Agent failed.")

            raise