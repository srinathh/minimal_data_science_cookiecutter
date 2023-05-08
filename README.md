# Data Science DevContainer Github Template

## How to use

### 1. Use the Github template to create your project

### 2. Clone the generated repo to your development environment

### 3. Open the folder as a container in Visual Studio Code
- Ensure Docker is installed in your system
- Install the `Dev Containers` extension
- Press `F1` to pull up the Command Pallette
- Select `Dev Containers: Open Folder in Container...` and select cloned folder
- The Dev Container will get built and the `utils` package will be installed in python envt

### 4. Check that everything is working
- Press **Ctrl + Shift + \`** to to pull up a terminal
- Run `pytest`

### 5. Customize

#### `pyproject.toml`
- Change `name` and `description`

#### `utils` under `src`
- Change to whatever package you want

### `sample.ipynb` under `notebooks`
- You can delete as needed

