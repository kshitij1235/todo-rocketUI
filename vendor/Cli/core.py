import os
import shutil
import subprocess
from tkinter import Tk, Label, PhotoImage
import sys
def cleanup_(files_to_remove : list = [], 
            dir_to_remove: list=[] , 
            file_end_with=[])->None :  
    """
    Cleans the given directories and files
    """
    for root, dirs, files in os.walk(os.getcwd()):
        # Remove files based on extensions or specific filenames
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(ext) for ext in file_end_with) or file in files_to_remove:
                try:
                    os.remove(file_path)
                    print(f"clean : {file_path}")
                except OSError as e:
                    print(f"Error removing file {file_path}: {e}")

        # Remove directories
        for dir_ in dirs:
            if dir_ in dir_to_remove:
                dir_path = os.path.join(root, dir_)
                try:
                    shutil.rmtree(dir_path)
                    print(f"clean dir: {dir_path}")
                except OSError as e:
                    print(f"Error removing directory {dir_path}: {e}")


def create_executable(script_path: str = "main.py", 
                      resource_dir: str = "resources/images",
                      onefile: bool = True,
                      output_dir: str = "./build"):
    """
    Creates a standalone executable from a given Python script using PyInstaller, 
    including all resources from a directory, and allows specifying output directory.

    Parameters:
    script_path (str): The path to the Python script to be converted into an executable.
    resource_dir (str): The path to the resources directory to be included in the executable.
    onefile (bool): Whether to create a single-file executable (default: True).
    output_dir (str): The directory to store the output executable (default: './dist').
    """
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The script file '{script_path}' does not exist.")
    
    if not os.path.isdir(resource_dir):
        raise FileNotFoundError(f"The resource directory '{resource_dir}' does not exist.")
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Build the PyInstaller command
    command = [
    'pyinstaller',
    '--onefile' if onefile else '',
    script_path,
    '--add-data',
    f'{resource_dir}{os.pathsep}resources/images',
    '--distpath',
    output_dir
    ]

    # Remove empty strings from the command list
    command = [arg for arg in command if arg]


    try:
        # Run PyInstaller with the constructed command
        subprocess.run(command, check=True)
        print(f"Executable created successfully for {script_path} in {output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the executable: {e}")
        return False

import os
import subprocess
# [TODO] yet to be executed for release bulit only
def create_executable_nuitka(script_path: str = "main.py", 
                             resource_dir: str = "resources/images",
                             onefile: bool = True,
                             output_dir: str = "./builts"):
    """
    Creates a standalone executable from a given Python script using Nuitka, 
    including all resources from a directory, and allows specifying the output directory.

    Parameters:
    script_path (str): The path to the Python script to be converted into an executable.
    resource_dir (str): The path to the resources directory to be included in the executable.
    onefile (bool): Whether to create a single-file executable (default: True).
    output_dir (str): The directory to store the output executable (default: './builts').
    """
    # Check if the Python script exists
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The script file '{script_path}' does not exist.")
    
    # Check if the resource directory exists
    if not os.path.isdir(resource_dir):
        raise FileNotFoundError(f"The resource directory '{resource_dir}' does not exist.")
    
    # Ensure the output directory exists, create it if it does not
    os.makedirs(output_dir, exist_ok=True)

    # Construct the Nuitka command
    command = [
        'nuitka',
        '--standalone',  # Ensures a standalone executable with all dependencies
        '--onefile' if onefile else '',  # Make it a single-file executable if requested
        '--output-dir', output_dir,  # Specify where the executable will be placed
        script_path  # The Python script to compile
    ]

    # Add resource files (images, etc.) to the build
    command.extend([
        '--include-data-dir',
        f'{resource_dir}=resources/images'  # Include resource directory into the executable
    ])

    # Remove any empty strings from the command list
    command = [arg for arg in command if arg]

    try:
        # Run Nuitka with the constructed command
        subprocess.run(command, check=True)
        print(f"Executable created successfully for {script_path} in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the executable: {e}")

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)