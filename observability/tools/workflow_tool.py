from google.adk.tools import FunctionTool
from .memory_tool import _memory_store


def update_workflow_status(
    task: str,
    current_agent: str,
    status: str,
) -> str:
    """
    Update the current execution status of a workflow.

    Args:
        task: The task identifier.
        current_agent: Name of the agent currently processing the task.
        status: Current execution status (e.g., RUNNING, COMPLETED, FAILED).

    Returns:
        A confirmation message or an error if the workflow is not found.
    """

    workflow = _memory_store.get(task)

    if workflow is None:
        return (
            f"Workflow not found.\n"
            f"Task: {task}"
        )

    workflow.current_agent = current_agent
    workflow.status = status

    return (
        "Workflow Status Updated\n"
        f"Task: {workflow.task}\n"
        f"Current Agent: {workflow.current_agent}\n"
        f"Status: {workflow.status}"
    )


update_workflow_status_tool = FunctionTool(func=update_workflow_status)