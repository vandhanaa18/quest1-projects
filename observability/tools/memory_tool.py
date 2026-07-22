from google.adk.tools import FunctionTool

from ..models import WorkflowData

# Temporary in-memory storage
_memory_store: dict[str, WorkflowData] = {}


def save_workflow(task: str, workflow: WorkflowData) -> str:
    """
    Save the workflow for a given task.
    """
    _memory_store[task] = workflow
    return f"Workflow saved for task: {task}"


def load_workflow(task: str):
    """
    Load the workflow for a given task.
    """
    return _memory_store.get(task, None)


save_workflow_tool = FunctionTool(save_workflow)
load_workflow_tool = FunctionTool(load_workflow)