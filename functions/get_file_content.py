from pathlib import Path
from google.genai import types


def get_file_content(working_directory: str, file_path: str) -> str:
    root_folder = Path().parent.parent.resolve()
    work_dir_path = root_folder / Path(working_directory)

    file_path_path = work_dir_path / Path(file_path)
    if not file_path_path.is_relative_to(work_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not file_path_path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path_path.resolve()}"'

    try:
        with open(file_path_path, "r") as file:
            file_content = file.read(10000)

            if len(file_content) == 10000:
                file_content += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: {e}"

    return file_content


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets file content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of a file to get content from.",
            ),
        },
    ),
)
