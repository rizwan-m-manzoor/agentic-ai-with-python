import os
import sys

def add_project_src_to_path():
    """
    Adds the project-level `src/` folder to sys.path, so imports like
    `from core import settings` work in notebooks.
    """
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.append(src_path)