from azureml.core import Run
import argparse
from aml_setup.utils import aml_utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_arg", type=str, help='Pass in a Test Argument')
    args, _ = parser.parse_known_args()

    test_arg = eval(args.test_arg)
    print(f"test_arg: {test_arg}")
    print(f"type(test_arg): {type(test_arg)}")

    current_run = Run.get_context()
    ws = current_run.experiment.workspace
    print(f"Workspace: {ws}")
    
    final_string = aml_utils.join_string_list(test_arg)
    print(f"final_string: {final_string}")
    print(f"type(final_string): {type(final_string)}")
    current_run.complete()
