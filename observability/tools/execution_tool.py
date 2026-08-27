from google.adk.tools import FunctionTool
from pathlib import Path
import io
import contextlib
import subprocess
import sys


# ---------------------------------------------------------
# Shared workspace
# Must match file_tool.py
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = PROJECT_ROOT / "workspace"

# Create workspace if it does not already exist.
WORKSPACE.mkdir(parents=True, exist_ok=True)


def execute_code(
    code: str = "",
    filename: str = "",
) -> str:
    """
    Execute Python code or a Python file from the shared workspace.

    Test files are executed using Python's unittest runner.
    """

    try:

        # ---------------------------------------------------------
        # Execute a workspace file
        # ---------------------------------------------------------

        if filename:

            file_path = (WORKSPACE / filename).resolve()

            # Prevent access outside workspace
            if not file_path.is_relative_to(WORKSPACE):
                return (
                    "Execution Failed: "
                    "File must be inside the workspace."
                )

            if not file_path.exists():
                return (
                    "Execution Failed: "
                    f"File not found: {filename}"
                )

            if not file_path.is_file():
                return (
                    "Execution Failed: "
                    f"Not a file: {filename}"
                )

            # -----------------------------------------------------
            # Make workspace available for imports
            # -----------------------------------------------------

            env = None

            if str(WORKSPACE) not in sys.path:
                sys.path.insert(0, str(WORKSPACE))

            # -----------------------------------------------------
            # Test files
            # -----------------------------------------------------

            if (
                filename.startswith("test_")
                or filename.endswith("_test.py")
            ):

                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "unittest",
                        filename,
                        "-v",
                    ],
                    capture_output=True,
                    text=True,
                    cwd=str(WORKSPACE),
                    env=env,
                )

            # -----------------------------------------------------
            # Normal Python files
            # -----------------------------------------------------

            else:

                result = subprocess.run(
                    [
                        sys.executable,
                        str(file_path),
                    ],
                    capture_output=True,
                    text=True,
                    cwd=str(WORKSPACE),
                    env=env,
                )

            output = result.stdout.strip()
            error = result.stderr.strip()

            # unittest may write results to stderr
            combined_output = "\n".join(
                part
                for part in [output, error]
                if part
            )

            if result.returncode == 0:

                return (
                    "Execution Successful:\n"
                    f"{combined_output or 'No output.'}"
                )

            return (
                "Execution Failed:\n"
                f"{combined_output or 'Unknown execution error.'}"
            )

        # ---------------------------------------------------------
        # Execute Python code directly
        # ---------------------------------------------------------

        if code:

            output = io.StringIO()

            # Make workspace available for imports such as:
            # from fibonacci import generate_fibonacci

            if str(WORKSPACE) not in sys.path:
                sys.path.insert(0, str(WORKSPACE))

            with contextlib.redirect_stdout(output):

                exec(
                    code,
                    {
                        "__name__": "__main__",
                        "__file__": str(WORKSPACE),
                    },
                )

            result = output.getvalue().strip()

            if result:
                return (
                    "Execution Successful:\n"
                    f"{result}"
                )

            return "Execution Successful:\nNo output."

        # ---------------------------------------------------------
        # Nothing provided
        # ---------------------------------------------------------

        return (
            "Execution Failed: "
            "No code or filename provided."
        )

    except Exception as e:

        return (
            "Execution Failed:\n"
            f"{type(e).__name__}: {e}"
        )


# ---------------------------------------------------------
# ADK Tool
# ---------------------------------------------------------

execution_tool = FunctionTool(func=execute_code)