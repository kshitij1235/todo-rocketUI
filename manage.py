import click
from vendor.Cli.core import *
from Rocket import *
from main import MainApp
import os
import sys
import subprocess



@click.group()
def cli():
    pass

@cli.command()
def cleanup():
    "Clean up app temporary files"

    # Files that you want to delete
    files_to_remove = ["main.spec"]
    
    # Directories that you want to delete
    dir_to_remove = ["__pycache__", "dist", "build"]
    
    file_end_with = [".spec"]
    
    cleanup_(files_to_remove, dir_to_remove, file_end_with)

@cli.command()
def Cleanbuilt() -> None:
    cleanup_(["main.spec"], ["__pycache__", "build"])
    return 


@cli.command()
@click.option('-o', '--onefile', is_flag=True, help="Build a single-file executable.")
def built(onefile: bool) -> None:
    """
    Build the application as an executable. Optionally build a single-file executable.
    """
    try:
        create_executable(onefile=onefile, output_dir="./build")
        click.echo("Build completed successfully.")
    except Exception as e:
        click.echo(f"Build failed: {e}")
    return


@click.option('-c', '--clean', is_flag=True, help="Clean up before running the application.")
@click.option('-f', '--file', type=str, help="Specify a Python file to run.")
@cli.command()
def run(clean: bool, file: str) -> None:
    """
    Run the application. Optionally clean up or execute a Python file.
    """
    if clean:
        cleanup_([], ["__pycache__", "build"])
    
    if file:
        try:
            print(f"Running the specified file: {file}")
            with open(file, 'r') as f:
                code = f.read()
                exec(code)  # Execute the Python file content
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except Exception as e:
            print(f"Error while executing the file: {e}")
    else:
        MainApp()

@cli.command()
def upgrade() -> None:
    """
    Upgrade all the packages by installing dependencies from requirements.txt.
    """
    # Check if requirements.txt exists
    if os.path.exists("requirements.txt"):
        click.echo("Upgrading packages from requirements.txt...")
        try:
            # Run pip install command to install/upgrade packages
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"])
            click.echo("All packages upgraded successfully.")
        except subprocess.CalledProcessError as e:
            click.echo(f"Failed to upgrade packages: {e}")
    else:
        click.echo("requirements.txt file not found. Please add the file and try again.")
    return
@cli.command()
def version() -> None:
    click.echo(f"Version: {VERSION}")
    return

if __name__ == "__main__":
    cli()
