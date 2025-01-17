import os

class ProjectScanner:
  """
  Scans a project directory to find Python files for processing.
  """

  def __init__(self, project_dir: str):
    """
    Initializes the ProjectScanner with a target project directory.

    Args:
      project_dir (str): Path to the root directory of the project.
    """
    self.project_dir = project_dir

  def get_python_files(self) -> list[str]:
    """
    Retrieves all Python files in the project directory and its subdirectories.

    Returns:
      list[str]: A list of absolute paths to Python files.
    """
    python_files = []
    for root, _, files in os.walk(self.project_dir):
      for file in files:
        if file.endswith(".py"):
          python_files.append(os.path.join(root, file))
    return python_files
