import json
import yaml

class Utils:
  """
  Utility class with helper methods for file operations and data formatting.
  """

  @staticmethod
  def load_json(file_path: str) -> dict:
    """
    Loads a JSON file and returns its contents.

    Args:
      file_path (str): Path to the JSON file.

    Returns:
      dict: Parsed JSON data.
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
      return json.load(json_file)

  @staticmethod
  def save_json(file_path: str, data: dict):
    """
    Saves data to a JSON file.

    Args:
      file_path (str): Path to the JSON file.
      data (dict): Data to save.
    """
    with open(file_path, "w", encoding="utf-8") as json_file:
      json.dump(data, json_file, indent=2)
    print(f"JSON saved to: {file_path}")

  @staticmethod
  def load_yaml(file_path: str) -> dict:
    """
    Loads a YAML file and returns its contents.

    Args:
      file_path (str): Path to the YAML file.

    Returns:
      dict: Parsed YAML data.
    """
    with open(file_path, "r", encoding="utf-8") as yaml_file:
      return yaml.safe_load(yaml_file)

  @staticmethod
  def save_yaml(file_path: str, data: dict):
    """
    Saves data to a YAML file.

    Args:
      file_path (str): Path to the YAML file.
      data (dict): Data to save.
    """
    with open(file_path, "w", encoding="utf-8") as yaml_file:
      yaml.safe_dump(data, yaml_file, default_flow_style=False)
    print(f"YAML saved to: {file_path}")
