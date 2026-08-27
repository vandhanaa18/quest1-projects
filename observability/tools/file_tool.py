from google.adk.tools import FunctionTool
from pathlib import Path


# Workspace is located inside the project directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = PROJECT_ROOT / "workspace"

# Create workspace if it does not already exist.
WORKSPACE.mkdir(parents=True, exist_ok=True)


def _safe_path(filename: str) -> Path:
    """
    Resolve a workspace-relative path safely.
    """

    file_path = (WORKSPACE / filename).resolve()

    if not file_path.is_relative_to(WORKSPACE):
        raise ValueError("Access denied: file must be inside the workspace.")

    return file_path


def read_file(filename: str) -> str:
    """
    Read a text file from the workspace directory.
    """

    try:
        file_path = _safe_path(filename)

        if not file_path.exists():
            return f"File not found: {filename}"

        if not file_path.is_file():
            return f"Not a file: {filename}"

        return file_path.read_text(encoding="utf-8")

    except Exception as e:
        return f"Error reading file: {e}"


def write_file(filename: str, content: str) -> str:
    """
    Write text to a file inside the workspace directory.
    """

    try:
        file_path = _safe_path(filename)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(
            content,
            encoding="utf-8",
        )

        return (
            "File saved successfully.\n"
            f"Location: {file_path}\n"
            f"Characters Written: {len(content)}"
        )

    except Exception as e:
        return f"Error writing file: {e}"


read_file_tool = FunctionTool(func=read_file)
write_file_tool = FunctionTool(func=write_file)