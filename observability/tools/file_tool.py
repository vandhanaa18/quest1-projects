from pathlib import Path

WORKSPACE = Path("workspace").resolve()


def read_file(filename: str):
    file_path = (WORKSPACE / filename).resolve()

    if not str(file_path).startswith(str(WORKSPACE)):
        return "Access denied."

    if not file_path.exists():
        return "File not found."

    return file_path.read_text()


def write_file(filename: str, content: str):
    file_path = (WORKSPACE / filename).resolve()

    if not str(file_path).startswith(str(WORKSPACE)):
        return "Access denied."

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path.write_text(content)

    return f"Saved {filename}"