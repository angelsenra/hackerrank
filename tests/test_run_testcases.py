import subprocess
import os
import os.path
from pytest import mark

PYTHON_CMD = os.environ.get("HACKERRANK_PYTHON_CMD", "python")
PROBLEMS_PATH = "problems"
TESTCASES_PATH = os.path.join("tests", "testcases")


def get_testcase_filenames(problem_id):
    def _get_filenames_from_folder(folder_name):
        return sorted(
            filename
            for filename in os.listdir(os.path.join(TESTCASES_PATH, f"{problem_id}-testcases", folder_name))
            if filename.endswith(".txt")
        )

    return list(zip(_get_filenames_from_folder("input"), _get_filenames_from_folder("output")))


problem_filenames = [
    filename for filename in os.listdir(PROBLEMS_PATH) if filename.endswith(".py") and filename != "__init__.py"
]
testcase_foldernames = [foldername for foldername in os.listdir(TESTCASES_PATH) if "." not in foldername]
solved_problem_ids = set(i.split(".py")[0].replace("_", "-") for i in problem_filenames)
testcased_problem_ids = set(i.split("-testcases")[0] for i in testcase_foldernames)

problem_id_and_testcase_filenames = [
    [problem_id, input_filename, output_filename]
    for problem_id in solved_problem_ids & testcased_problem_ids
    for input_filename, output_filename in get_testcase_filenames(problem_id)
]


class TestRunTestcases:
    @mark.parametrize(["problem_id", "input_filename", "output_filename"], problem_id_and_testcase_filenames)
    def test_testcase(self, problem_id, input_filename, output_filename):
        problem_filepath = os.path.join("problems", f"{problem_id.replace('-', '_')}.py")
        input_text = _get_file_content(input_filename, problem_id, "input")
        output_text = _get_file_content(output_filename, problem_id, "output")

        result = _run_cmd(problem_filepath, input_text)
        assert result == output_text

    @mark.parametrize("problem_id", solved_problem_ids - testcased_problem_ids)
    def test_there_are_no_untested_problems(self, problem_id):
        assert False, f"{problem_id} is not tested!"

    @mark.parametrize("problem_id", testcased_problem_ids - solved_problem_ids)
    def test_there_are_no_unassigned_testcases(self, problem_id):
        assert False, f"{problem_id} testcase is not being used!"


def _get_file_content(filename, problem_id, folder_name):
    with open(os.path.join(TESTCASES_PATH, f"{problem_id}-testcases", folder_name, filename), "r") as f:
        return f.read() + "\n"


def _run_cmd(problem_filepath, input_text):
    result = subprocess.run(
        [PYTHON_CMD, problem_filepath], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return result.stdout.decode()
