from google.adk.tools import FunctionTool
from pathlib import Path

WORKSPACE = Path("workspace").resolve()


def read_file(filename: str) -> str:
    """
    Read a text file from the workspace directory.

    Args:
        filename: Relative path to the file inside the workspace.

    Returns:
        File contents or an error message.
    """

    try:
        file_path = (WORKSPACE / filename).resolve()

        if not str(file_path).startswith(str(WORKSPACE)):
            return "Access denied: File must be inside the workspace."

        if not file_path.exists():
            return f"File not found: {filename}"

        return file_path.read_text(encoding="utf-8")

    except Exception as e:
        return f"Error reading file: {e}"


def write_file(filename: str, content: str) -> str:
    """
    Write text to a file inside the workspace directory.

    Args:
        filename: Relative path to the destination file.
        content: Text content to write.

    Returns:
        Success or error message.
    """

    try:
        file_path = (WORKSPACE / filename).resolve()

        if not str(file_path).startswith(str(WORKSPACE)):
            return "Access denied: File must be inside the workspace."

        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

        return (
            f"File saved successfully.\n"
            f"Location: {filename}\n"
            f"Characters Written: {len(content)}"
        )

    except Exception as e:
        return f"Error writing file: {e}"


read_file_tool = FunctionTool(func=read_file)
write_file_tool = FunctionTool(func=write_file)