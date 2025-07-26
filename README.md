
    ███████╗ ██████╗  ██████╗ ██╗  ██╗███████╗████████╗    ██╗   ██ ║██║ 
    ██╔══██║██╔═══██╗██╔════╝ ██║ ██║ ██╔════╝╚══██╔══╝    ██║   ██ ║██║ 
    ██████╔╝██║   ██║██║      ████    █████╗     ██║       ██║   ██ ║██║ 
    ██╔═██║ ██║   ██║██║      ██╔═██║ ██╔══╝     ██║       ██║   ██ ║██║ 
    ██║ ██║  ██████╔╝╚ ██████╔██║  ██║███████╗   ██║       ████████ ║██║ 
    ╚═╝ ╚═╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚══╝
A modern Python framework for building beautiful and efficient desktop applications with a focus on user experience and developer productivity.

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Core Features](#core-features)
- [Configuration](#configuration)
- [Development](#development)
- [CLI Commands](#cli-commands)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo-rocketUI.git
cd todo-rocketUI
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

## Getting Started

1. Create your application structure in the `src` directory:
```
src/
├── components/          # Reusable UI components
│   ├── header_components.py
│   ├── todo_components.py
│   └── bottom_bar_component.py
├── helper/             # Helper functions and utilities
├── homepages.py        # Main page components
└── navigation_bar.py   # Navigation components
```

2. Create your main page components in `src/homepages.py`:
```python
from src.components.todo_components import todo_list
from src.components.bottom_bar_component import add_task
from src.navigation_bar import create_bottom_nav
from tkinter import Frame

def homepage(window) -> Frame:
    from src.components.header_components import todo_header
    
    # Create the main frame
    homepage_frame = Frame(window)
    
    # Add components
    todo_header(homepage_frame, "To-do List")
    todo_list(homepage_frame, "rocketdb", "tasks")
    add_task(homepage_frame)
    
    # Layout
    homepage_frame.pack(expand=True, fill="both")
    return homepage_frame
```

3. Set up navigation in `src/navigation_bar.py`:
```python
from customtkinter import *

def create_bottom_nav(window):
    from src.homepages import homepage, settings
    
    # Create navigation frame
    nav_frame = CTkFrame(window, fg_color="gray", height=100)
    nav_frame.pack(side="bottom", fill="x")
    
    # Add navigation buttons
    btn_home = CTkButton(
        nav_frame,
        text="New Form",
        fg_color="gray",
        hover_color="black",
        corner_radius=0,
        command=lambda: switcher(window, homepage, "homepage")
    )
    btn_home.pack(side="left", expand=True, fill="both")
```

4. Create reusable components in `src/components/`:
```python
# src/components/header_components.py
def todo_header(parent, title):
    # Create header component
    pass

# src/components/todo_components.py
def todo_list(parent, db_name, table_name):
    # Create todo list component
    pass

# src/components/bottom_bar_component.py
def add_task(parent):
    # Create add task component
    pass
```

5. Run your application:
```bash
python manage.py run
```

## Project Structure

```
todo-rocketUI/
├── src/               # Application source code
│   ├── components/    # Reusable UI components
│   ├── helper/        # Helper functions
│   ├── homepages.py   # Main page components
│   └── navigation_bar.py  # Navigation components
├── app/              # Framework core components
├── resources/        # Static resources
├── vendor/          # Third-party dependencies
├── rocketdb/        # Database related files
├── Rocket.py        # Framework configuration
├── manage.py        # Project management script
└── main.py          # Application entry point
```

## Core Features

- **Modern UI Components**: Built-in components for creating beautiful user interfaces
  - Buttons, Labels, Input Fields
  - Menus and Toolbars
  - Layout Management
  - Custom Styling
- **Database Integration**: Seamless database connectivity with rocketdb
  - SQLite support out of the box
  - Easy database migrations
  - ORM-like interface
- **Resource Management**: Easy handling of static resources
  - Image loading and caching
  - Style management
  - Asset bundling
- **Project Management**: Built-in tools for project management and deployment
  - Build system
  - Hot reloading
  - Package management

## Configuration

Configure your application in `Rocket.py`:

```python
# Basic Configuration
PROJECT_NAME = "your_app_name"
VERSION = "1.0.0"
RELEASE = False  # Set to True for production

# Additional Configuration Options
WINDOW_TITLE = "My Application"
WINDOW_SIZE = (800, 600)
THEME = "light"  # or "dark"
```

## Development

1. Activate the virtual environment:
```bash
pipenv shell
```

2. Run your application:
```bash
python main.py
```

## CLI Commands

The framework provides a powerful CLI tool through `manage.py`. Here are all available commands:

### Run Application
```bash
python manage.py run [options]
```
Options:
- `-c, --clean`: Clean up temporary files before running
- `-r, --hotreload`: Enable hot reloading for development
- `-f, --file`: Specify a Python file to run

Example:
```bash
python manage.py run --hotreload  # Run with hot reloading
python manage.py run --clean      # Clean and run
```

### Build Application
```bash
python manage.py built [options]
```
Options:
- `-o, --onefile`: Build a single-file executable

Example:
```bash
python manage.py built --onefile  # Create a single executable
```

### Cleanup
```bash
python manage.py cleanup
```
Removes temporary files and build artifacts:
- Deletes `main.spec`
- Removes `__pycache__`, `dist`, and `build` directories
- Cleans up `.spec` files

### Upgrade Dependencies
```bash
python manage.py upgrade
```
Upgrades all packages from requirements.txt

### Version Check
```bash
python manage.py version
```
Displays the current framework version

### Quick Clean
```bash
python manage.py Cleanbuilt
```
Quick cleanup of build files and cache

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the license included in the LICENSE file.
