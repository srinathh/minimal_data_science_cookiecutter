# Minimal Data Science Project Cookiecutter Template

This is a minimal cookiecutter template to create a project structure for
a data science project that can serve for both data exploration, model
development and be containerized as a deployable stand-alone application
with Docker.

## Usage

### 1. Create your project with Cookiecutter
The below command creates a project using this cookiecutter template on your 
development machine. Visit the [Cookiecuter](https://www.cookiecutter.io/) website
for more details.
```
pipx run cookiecutter gh:srinathh/minimal_data_science_cookiecutter
```

### 2. [Recommended] Create your environment
You may want to use [Conda](https://conda-forge.org/), [venv](https://docs.python.org/3/library/venv.html)
or [Pyenv](https://github.com/pyenv/pyenv) etc to create isolated environment for your project

### 3. Install for local development
Change to the project directory & run the below to install the packages and the 
executable in the project for local development. See the README.md inside the 
project for more information. You may note that the Dockerfile does the same
to build an application image for deployment.

```
pip install -e .
```

If you'll be using Jupyter notebooks & chose the appropriate option to add
development dependencies during creation, use the following:
```
pip install -e ".[dev]"
```

### 4. [Recommended] Create your git repository
Create an empty git repository in your platform of choice and push the contents
to ensure you can version control.
```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <remote path>
git push -u origin main
```

To install development dependencies like Jupyter, 

## FAQ

### Where is `requirements.txt` and `setup.py`
The Python ecosystem standardized on `pyproject.toml` as a build-system independent
format for packaging specification with [PEP 517](https://peps.python.org/pep-0517/)
and [PEP 518](https://peps.python.org/pep-0518/). 

While legacy packages still use a mish-mash of `setup.py` or `requirements.txt` to
specify dependencies, the modern Pythonic approach is to directly encode both 
dependencies and all other app package related information such-as entry-points,
preferred build system, python version dependency etc directly in `pyproject.toml`

For more information on how to customize `pyproject.toml`, see the 
[official tutorial](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### What does answering yes to `use_standard_ds_pkgs` do?
It adds the following standard data science packages as project 
dependencies in `pyproject.toml`
- `pandas`
- `numpy`,
- `scikit-learn`,
- `matplotlib`,
- `python-dotenv`,{% endif %}

### What does answering yes to `use_slim_docker_img` do?
The [official Python docker](https://hub.docker.com/_/python) image comes
in two flavors, the regular and slim. The slim versions are much lighter
but may be missing some debian packages. Always test before deploying.

## Project Organization

```
├── .gitignore                  <- to indicate which files to ignore by git
├── LICENSE                     <- Open-source license if one is chosen
├── README.md                   <- The top-level README for developers using this project.
├── data                        <- Folder for data. Any file inside this is ignored by Git
├── notebooks                   <- Jupyter notebooks. Suggested naming convention is a number (for ordering),
│                                  the creator's initials, and a short `-` delimited description, e.g.
│                                  `1.0-jqp-initial-data-exploration`.
├── Dockerfile                  <- Dockerfile to build the package with app as a Docker Image
├── pyproject.toml              <- Project configuration file with package metadata and dependency management
└── src                         <- Source code for use in this project.
    │
    ├── app 
    │   ├── __init__.py 
    │   └── app.py              <- contains the entry point for the sample Hello World application
    │
    ├── {{ cookiecutter.project_slug }}              <- the package for this project
    │   └── __init__.py 
    │
    └── utils 
        ├── __init__.py 
        ├── sample.py           <- A sample utility function example
        ├── singleton.py        <- A utility implementation of Singleton pattern for Python
        └── test_utils.py       <- An example of how to write tests
```
