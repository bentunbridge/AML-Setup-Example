# AML-Setup-Example
A repository demonstrating a project setup using the Azure Machine Learning Cloud Infrastructure.  

The notebook `notebooks/pipeline-setup.ipynb` can be used to create a test AML pipeline which runs a simple test script on an AML hosted compute.  

### Local Environment 
A local environment will need to be created to correctly install the [Azure SKD packages](https://github.com/Azure/azure-sdk). We use `pipenv` environments to manage the local env.   
To install use the development environment run:   
`pipenv install --dev`

Alternatively the environment can be instaled from an existing lock file with:   
`pipenv sync`

### Create AML Pipeline 

To run the notebook an AML subscription is needed, a free 30 day trial is also available for testing. The subscription config should be exported to the config file, `config.json`. Follow the instructions on this page, [Set up a Python development environment for Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment).   

If run in debug mode a test experiment is run. We also include an option to publish the pipeline also which allows the pipeline to be triggered from the AML studio or api call with the azure SDK.  

### Create Hosted Environment 

Any experiment will need a created environment to run remotely on the Azure hosted computes. Running the function below will create a new environment. We can also provided a wheel file to include locally developed packages also.

```python
from aml_setup.create_envs import create_env

environment_dir_path = create_env.create_env_dir(ws,
                                                 env_out_dir="./envs/",
                                                 version="0.0.1",
                                                 overwrite=True,
                                                 wheel_path=wheel_path)
```


This repo is just a simple demo and can be used as a starting point to developing a project.

### Github Workflow
The Github Workflow is triggered upon a Pull Request into the main branch. This workflow includes:
- **[flake8](https://flake8.pycqa.org/en/latest/)**: which verifies PEP8 rules/coding standards are kept.
- **[pytest](https://docs.pytest.org/en/7.1.x/)**: which triggers the pytests included in the repo.
