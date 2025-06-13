from pathlib import Path
from google.genai import types


def write_file(working_directory: str, file_path: str, content: str) -> str:
    root_folder = Path().parent.parent.resolve()
    work_dir_path = root_folder / Path(working_directory)

    file_path_path = work_dir_path / Path(file_path)
    if not file_path_path.is_relative_to(work_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(file_path_path, "w") as file:
            file.write(content)
            print(f"{len(content)} characters written")
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes into file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a file to write into.",
            ),
            "content": types.Schema(
                type=types.Type.STRING, description="Content to write into file."
            ),
        },
    ),
)
