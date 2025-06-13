from pathlib import Path
import subprocess
from google.genai import types


def run_python_file(working_directory: str, file_path: str, args=None):
    root_folder = Path(__file__).parent.parent.resolve()
    work_dir_path = root_folder / Path(working_directory)

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    file_path_path = work_dir_path / Path(file_path)
    if not file_path_path.resolve().is_relative_to(work_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not file_path_path.is_file():
        return f'Error: File "{file_path}" not found.'

    try:
        commands = ["python", str(file_path_path)]
        if args:
            commands.extend(args)

        subprocess_result = subprocess.run(
            commands, capture_output=True, timeout=30, text=True, cwd=work_dir_path
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    output = []
    if subprocess_result.stdout:
        output.append(f"STDOUT:\n{subprocess_result.stdout}")
    if subprocess_result.stderr:
        output.append(f"STDERR:\n{subprocess_result.stderr}")
    if subprocess_result.returncode != 0:
        output.append(f"Process exited with code {subprocess_result.returncode}")

    return "\n".join(output) or "No output produced."


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a file to execute.",
            ),
        },
    ),
)
