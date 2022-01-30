import subprocess
import os
import os.path
from pytest import mark

PYTHON_CMD = os.environ.get("HACKERRANK_PYTHON_CMD", "python")
TESTCASES_PATH = os.path.join("tests", "testcases")


def get_testcase_filenames(problem_id):
    def _get_filenames_from_folder(folder_name):
        return sorted(
            filename
            for filename in os.listdir(get_testcase_folder_path(problem_id, folder_name))
            if filename.endswith(".txt")
        )

    return list(zip(_get_filenames_from_folder("input"), _get_filenames_from_folder("output")))


def get_testcase_folder_path(problem_id, folder_name):
    return os.path.join(os.path.join(TESTCASES_PATH, f"{problem_id}-testcases"), folder_name)


class TestRunTestcases:
    @mark.parametrize(["input_filename", "output_filename"], get_testcase_filenames("electronics-shop"))
    def test_electronics_shop(self, input_filename, output_filename):
        PROBLEM_FILEPATH = os.path.join("problems", "easy", "electronics_shop.py")
        TESTCASE_FOLDERNAME = "electronics-shop"

        input_text = _get_file_content(input_filename, TESTCASE_FOLDERNAME, "input")
        output_text = _get_file_content(output_filename, TESTCASE_FOLDERNAME, "output")

        result = _run_cmd(PROBLEM_FILEPATH, input_text)
        assert result == output_text

    @mark.parametrize(["input_filename", "output_filename"], get_testcase_filenames("matrix-rotation-algo"))
    def test_matrix_rotation_algo(self, input_filename, output_filename):
        PROBLEM_FILEPATH = os.path.join("problems", "hard", "matrix_rotation_algo.py")
        TESTCASE_FOLDERNAME = "matrix-rotation-algo"

        input_text = _get_file_content(input_filename, TESTCASE_FOLDERNAME, "input")
        output_text = _get_file_content(output_filename, TESTCASE_FOLDERNAME, "output")

        result = _run_cmd(PROBLEM_FILEPATH, input_text)
        assert result == output_text


def _get_file_content(filename, problem_id, folder_name):
    with open(os.path.join(get_testcase_folder_path(problem_id, folder_name), filename), "r") as f:
        return f.read() + "\n"


def _run_cmd(problem_filepath, input_text):
    result = subprocess.run([PYTHON_CMD, problem_filepath], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()
