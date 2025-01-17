import os

class ReadmeGenerator:
  """
  Generates a README.md file using the provided project metadata and template.
  """

  def __init__(self, template: str, output_dir: str = "."):
    """
    Initializes the ReadmeGenerator with a template and output directory.

    Args:
      template (str): The template for the README file.
      output_dir (str): Directory where the README.md file will be created (default: current directory).
    """
    self.template = template
    self.output_dir = output_dir

  def generate_readme(self, metadata: dict):
    """
    Generates the README.md file based on the provided metadata.

    Args:
      metadata (dict): A dictionary containing project metadata (e.g., name, author, description).
    """
    readme_content = self.template.format(**metadata)
    output_path = os.path.join(self.output_dir, "README.md")

    with open(output_path, "w", encoding="utf-8") as readme_file:
      readme_file.write(readme_content)
    print(f"README.md generated at: {output_path}")
