{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

## Features
* TODO

## Usage 

### Install package and application
```shell
pip install -e .
```

### To Run the application
```shell
{{ cookiecutter.project_slug }}
```

### Docker
```shell
docker build . -t {{ cookiecutter.project_slug }}
docker run {{ cookiecutter.project_slug }}
```

### To install with development dependencies
```shell
pip install -e ".[dev]"
```

### Changing Dependencies
- Make changes under `dependencies` in `pyproject.toml`

### Testing
```shell
pytest --cov
```


