from pathlib import Path
from typing import List, Optional, Union

from google.genai import types


def get_files_info(
    working_directory: str, directory: Optional[str] = None
) -> Union[List[str], str]:
    if not directory:
        return f'Error: "{directory}" is not a directory'

    root_folder = Path().parent.parent.resolve()
    work_dir_path = root_folder / Path(working_directory)
    dir_dir_path = (work_dir_path / Path(directory)).resolve()

    if not dir_dir_path.is_dir():
        return f'Error: "{directory}" is not a directory'

    if not dir_dir_path.is_relative_to(work_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        files_info = []
        for file in dir_dir_path.iterdir():
            file_name = file.name
            file_size = file.stat().st_size
            is_dir = file.is_dir()

            files_info.append(
                f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return files_info
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
