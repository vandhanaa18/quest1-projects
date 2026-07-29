from google.adk.tools import FunctionTool
from pathlib import Path


WORKSPACE = Path("workspace").resolve()


def edit_code(file_path: str, old_code: str, new_code: str) -> str:
    """
    Replace existing code in a file inside the workspace.

    Args:
        file_path: Relative path to the file inside the workspace.
        old_code: Existing code to replace.
        new_code: New code to insert.

    Returns:
        Success or error message.
    """

    try:
        path = (WORKSPACE / file_path).resolve()

        if not path.is_relative_to(WORKSPACE):
            return "Access denied: File must be inside the workspace."

        if not path.exists():
            return f"Edit failed: File not found: {file_path}"

        if not path.is_file():
            return f"Edit failed: Not a file: {file_path}"

        content = path.read_text(encoding="utf-8")

        if old_code not in content:
            return f"Edit failed: specified code was not found in {file_path}."

        updated_content = content.replace(old_code, new_code, 1)

        path.write_text(updated_content, encoding="utf-8")

        return f"Successfully edited {file_path}"

    except Exception as e:
        return f"Edit failed: {e}"


code_editor_tool = FunctionTool(func=edit_code)