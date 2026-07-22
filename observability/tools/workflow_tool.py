from google.adk.tools import FunctionTool
from ..models import WorkflowData


def update_workflow_status(
    workflow: WorkflowData,
    current_agent: str,
    status: str,
) -> str:
    """
    Updates the workflow with the current agent and execution status.
    """
    workflow.current_agent = current_agent
    workflow.status = status

    return (
        f"Workflow updated: "
        f"current_agent={current_agent}, "
        f"status={status}"
    )


update_workflow_status_tool = FunctionTool(update_workflow_status)