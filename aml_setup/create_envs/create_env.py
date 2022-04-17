import os
import re
import shutil
from typing import Any, Optional
from azureml.core import Environment
from azureml.core.conda_dependencies import CondaDependencies
from datetime import datetime


def create_env(ws: Any,
               env_name: str,
               wheel_path: Optional[str] = None) -> Any:
    """Function for creating an environment for an Azure ML Experiment

    Args:
        ws (Any): The aml workspace used
        env_name (str): A name for the environment
        wheel_path (str, optional): The optional path of a wheel file to be included in the
                                    environment. Defaults to None.

    Returns:
        Any: A created Azure environment.
    """
    if wheel_path:
        wheel_url = Environment.add_private_pip_wheel(workspace=ws, file_path=wheel_path, exist_ok=True)

    env = Environment(name=env_name)

    cd = CondaDependencies()
    cd.set_python_version("3.8.5")
    cd.add_pip_package("azureml-pipeline")
    cd.add_pip_package("numpy")
    cd.add_pip_package("pandas")
    cd.add_pip_package("scipy==1.6.3")
    cd.add_pip_package("scikit-learn==0.23.1")
    cd.add_pip_package("lightgbm")
    cd.add_pip_package("shap")

    if wheel_path:
        cd.add_pip_package(wheel_url)

    env.python.conda_dependencies = cd

    return env


def get_hash() -> str:
    """Function to generate a datetime based hash.

    Returns:
        str: A string Hash (function of the `now` datetime)
    """
    return datetime.now().strftime("%Y%m%d%H%M%S")


def get_new_version(version: str) -> str:
    """Create ne hash string version. This is because Azure ML cannot upload and overwrite
        existing wheel versions

    Args:
        version (str): Add a datetime based hash to the input version

    Returns:
        str: A new version string.
    """
    new_version = f"{version}-{get_hash()}"
    return new_version

def clone_wheel(wheel_path: str,
                new_version: str) -> str:
    """Clone the wheel file provided to a new version identifier

    Args:
        wheel_path (str): Path to Wheel File
        new_version (str): New datetime based version string

    Returns:
        str: Path to new wheel file
    """
    new_wheel_path = re.sub(r"(\d+.\d+.\d+)", new_version, wheel_path)
    shutil.copy(wheel_path, new_wheel_path)
    return new_wheel_path


def create_env_dir(ws: Any,
                   env_name: str,
                   env_out_dir: str,
                   version: str,
                   overwrite: bool = True,
                   wheel_path: Optional[str] = None) -> str:
    """Function to create the environment files required to run an experiment with
        required packages.

    Args:
        ws (Any): The aml workspace used
        env_name (str): Environment Name
        env_out_dir (str): Path to output directory of the environment created.
        version (str): Version of code
        overwrite (bool, optional): If True, overwrite the environment local path. Defaults to True.
        wheel_path (_type_, optional): The optional wheel path to include local code in the environment.
                                       If None, skip this step. Defaults to None.

    Returns:
        str: Output environment full path i.e. env_out_dir/{environment_name_and_version}
    """
    new_version = get_new_version(version)
    env_name_ = f"{env_name}-{new_version}"
    if wheel_path:
        wheel_path = clone_wheel(wheel_path, new_version)
    env = create_env(ws, env_name_, wheel_path)
    env_out_path = os.path.join(env_out_dir, env_name)
    env.save_to_directory(env_out_path, overwrite=overwrite)
    print(f"save to: {env_out_path}")
    return env_out_path
