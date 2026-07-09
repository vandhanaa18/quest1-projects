from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.code_generator_agent import CodeGeneratorAgent
from agents.reviewer_agent import ReviewerAgent
from agents.test_agent import TestAgent
from models import WorkflowData

def execute_with_retry(agent_name, agent_function, workflow=None, retries=3):

    for attempt in range(1, retries + 1):

        try:
            print(f"\nRunning {agent_name} (Attempt {attempt})")

            if workflow:
                return agent_function(workflow)
            else:
                return agent_function()

        except Exception as e:

            print(f"Error: {e}")

            if workflow:
                workflow.errors.append(
                    f"{agent_name}: {str(e)}"
                )

            if attempt == retries:
                print("Maximum retries reached.")
                raise


def main():

    task = input("Enter task: ")

    # Planner Agent
    planner = PlannerAgent()
    planner_data = execute_with_retry(
    "PlannerAgent",
    planner.run,
    task
)
    print("\n" + "=" * 50)
    print("PLANNER OUTPUT")
    print("=" * 50)
    print(planner_data["plan"])

    # Create WorkflowData object
    workflow = WorkflowData(
        task=planner_data["task"],
        plan=planner_data["plan"],
        research="",
        code=""
    )

    # Research Agent
    researcher = ResearchAgent()
    workflow = execute_with_retry(
    "ResearchAgent",
    researcher.run,
    workflow
)

    print("\n" + "=" * 50)
    print("RESEARCH OUTPUT")
    print("=" * 50)
    print(workflow.research)

    # Code Generator Agent
    generator = CodeGeneratorAgent()
    workflow = execute_with_retry(
    "CodeGeneratorAgent",
    generator.run,
    workflow
)

    print("\n" + "=" * 50)
    print("CODE OUTPUT")
    print("=" * 50)
    print(workflow.code)

    # Reviewer Agent
    reviewer = ReviewerAgent()
    workflow = execute_with_retry(
    "ReviewerAgent",
    reviewer.review,
    workflow
)

    print("\n" + "=" * 50)
    print("REVIEW OUTPUT")
    print("=" * 50)
    print("Status:", workflow.review_status)
    print("Comments:", workflow.review_comments)
    print("Suggestions:", workflow.improvement_suggestions)

    # Test Agent
    tester = TestAgent()
    workflow = execute_with_retry(
    "TestAgent",
    tester.run_tests,
    workflow
)

    print("\n" + "=" * 50)
    print("TEST OUTPUT")
    print("=" * 50)
    print("Status:", workflow.test_status)
    print("Report:", workflow.test_report)

    if workflow.detected_issues:
        print("Detected Issues:", workflow.detected_issues)


if __name__ == "__main__":
    main()