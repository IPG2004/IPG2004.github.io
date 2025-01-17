# import os
import argparse
# import sys
import config.settings as settings
from core.openai_client import OpenAIClient
from core.project_scanner import ProjectScanner
from core.file_processor import FileProcessor
from core.readme_generator import ReadmeGenerator

def main():
  """
  Main function to orchestrate the README generator workflow.
  Provides CLI arguments for flexibility in execution.
  """
  # Parse CLI arguments
  parser = argparse.ArgumentParser(
                      prog="ReadMeGenerator",
                      description="Automated README generator for Python projects.")
  parser.add_argument(
    "-p",
    "--project-dir", 
    type=str, 
    default=None, 
    help="Path to the project directory (overrides settings.PROJECT_DIR)."
  )
  parser.add_argument(
    "-c",
    "--do-comments", 
    action="store_true", 
    help="Add comments to Python files."
  )
  readme_arg = parser.add_argument_group("README Generation", "Options for generating README.md")
  readme_arg.add_argument(
    "-r",
    "--generate-readme", 
    action="store_true", 
    help="Generate README.md."
  )
  readme_arg.add_argument(
    "-n",
    "--project-name",
    type=str,
    default=settings.PROJECT_NAME,
    help="Title of the project (overrides settings.PROJECT_NAME)."
  )
  readme_arg.add_argument(
    "-a",
    "--author",
    type=str,
    default=settings.AUTHOR,
    help="Author of the project (overrides settings.AUTHOR)."
  )
  readme_arg.add_argument(
    "-t",
    "--template",
    default=settings.README_SETTINGS.get("default_template"),
    help="Path to the README template file."
  )
  readme_arg.add_argument(
    "-o",
    "--output-file",
    default=settings.README_SETTINGS.get("output_file"),
    help="Name of the output README file."
  )
  args = parser.parse_args()

  # Override project directory if provided in CLI
  project_dir = args.project_dir or settings.DEFAULT_PROJECT_DIR

  # Initialize components
  openai_client = OpenAIClient()
  scanner = ProjectScanner(project_dir=project_dir)
  processor = FileProcessor(openai_client=openai_client)

  if args.do_comments:
    print("Scanning project for Python files...")
    python_files = scanner.get_python_files()
    for file_path in python_files:
      print(f"Processing file: {file_path}")
      processor.process_file(file_path)
      print ("Comments on Python file: ", file_path, " added successfully.")
  
  if args.generate_readme:
    if (not args.title or not args.author):
      print("Error: When generating README, both project name (-n) and author (-a) must be provided.")

    else:
      print("Generating README.md...")

  # Process files unless skipped
  # if not args.skip_comments and not args.generate_readme_only:
  #   print("Scanning project for Python files...")
  #   python_files = scanner.get_python_files()
  #   for file_path in python_files:
  #     print(f"Processing file: {file_path}")
  #     processor.process_file(file_path)
  # elif args.skip_comments:
  #   print("Skipping comment addition to Python files.")

  # # Generate README unless skipped
  # if not args.skip_comments or args.generate_readme_only:
  #   print("Generating README.md...")
  #   template_path = os.path.join("templates", "readme_template.md")
  #   with open(template_path, "r", encoding="utf-8") as template_file:
  #     template = template_file.read()

  #   metadata = {
  #     "project_name": settings.PROJECT_NAME,
  #     "author": settings.AUTHOR,
  #     "description": settings.DESCRIPTION,
  #     "feature_1": "Automated docstring generation",
  #     "feature_2": "Customizable README templates",
  #     "feature_3": "Integration with OpenAI's GPT API",
  #     "usage_example": f"{project_dir}/main.py --help",
  #     "license_type": "MIT",
  #   }

  #   readme_generator = ReadmeGenerator(template=template, output_dir=project_dir)
  #   readme_generator.generate_readme(metadata)
  #   print("README.md generation complete!")
  # else:
  #   print("Skipping README generation.")

if __name__ == "__main__":
  main()

