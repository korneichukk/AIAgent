import unittest
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file


# class TestGetFilesInfo(unittest.TestCase):
# def test_calculator_dot(self):
#     result = get_files_info("calculator", ".")
#     result_expected = [
#         "- main.py: file_size=576 bytes, is_dir=False",
#         "- pkg: file_size=66 bytes, is_dir=True",
#         "- tests.py: file_size=1343 bytes, is_dir=False",
#     ]
#     print(result)
#     self.assertEqual(result, result_expected)
#
# def test_calculator_pkg(self):
#     result = get_files_info("calculator", "pkg")
#     result_expected = [
#         "- calculator.py: file_size=1739 bytes, is_dir=False",
#         "- render.py: file_size=768 bytes, is_dir=False",
#         "- __pycache__: file_size=96 bytes, is_dir=True",
#     ]
#     print(result)
#     self.assertEqual(result, result_expected)
#
# def test_calculator_bin(self):
#     result = get_files_info("calculator", "/bin")
#     print(result)
#     self.assertEqual(
#         result,
#         'Error: Cannot list "/bin" as it is outside the permitted working directory',
#     )
#
# def test_calculator_parent_dir(self):
#     result = get_files_info("calculator", "../")
#     print(result)
#     self.assertEqual(
#         result,
#         'Error: Cannot list "../" as it is outside the permitted working directory',
#     )


# class TestGetFileContent(unittest.TestCase):
#     def test_lorem_file(self):
#         result = get_file_content("calculator", "lorem.txt")
#         print(result)
#
#     def test_main_py(self):
#         result = get_file_content("calculator", "main.py")
#         print(result)
#
#     def test_calculator_py(self):
#         result = get_file_content("calculator", "pkg/calculator.py")
#         print(result)
#
#     def test_bin_cat(self):
#         result = get_file_content("calculator", "/bin/cat")
#         print(result)
#

#
# class TestWriteFile(unittest.TestCase):
#     def test_lorem_write(self):
#         result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
#         expected_result = f'Successfully wrote to "lorem.txt" ({len("wait, this isn't lorem ipsum")} characters written)'
#         print(result)
#         self.assertEqual(result, expected_result)
#
#     def test_more_lorem(self):
#         result = write_file(
#             "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
#         )
#         expected_result = f'Successfully wrote to "pkg/morelorem.txt" ({len("lorem ipsum dolor sit amet")} characters written)'
#         print(result)
#         self.assertEqual(result, expected_result)
#
#     def test_tmp(self):
#         result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#         expected_result = f'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory'
#         print(result)
#         self.assertEqual(result, expected_result)


def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()
