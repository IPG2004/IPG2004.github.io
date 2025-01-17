from openai import OpenAI
from config.settings import OPENAI_API_KEY, BASE_URL

class OpenAIClient:
  """
  A client for interacting with the OpenAI API.
  Handles the generation of comments or other text using GPT models.
  """

  def __init__(self, api_key: str = OPENAI_API_KEY, base_url : str = BASE_URL , model: str = "gpt-4o-mini", max_tokens: int = 2000, temperature: float = 0.8):
    """
    Initializes the OpenAIClient with the given configuration.

    Args:
      api_key (str): The OpenAI API key.
      base_url (str): The base URL for the OpenAI API.
      model (str): The GPT model to use (default: gpt-4o-mini).
      max_tokens (int): Maximum tokens to use in a single request.
      temperature (float): Controls the creativity of the response (0.0-1.0).
    """

    self.model = model
    self.max_tokens = max_tokens
    self.temperature = temperature
    self.client = OpenAI(
      base_url=base_url,
      api_key=api_key
      )

  def generate_comment(self, prompt: str) -> str:
    """
    Generates a comment based on the provided prompt.

    Args:
      prompt (str): The input prompt for the GPT model.

    Returns:
      str: The generated comment.
    """
    try:
      response = self.client.chat.completions.create(
        model=self.model,
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        messages = [
          {
            "role": "user",
            "content": prompt,
          }
        ],
      )
      return response.choices[0].message.content
    except RuntimeError as e:
      raise RuntimeError(f"Error interacting with OpenAI API: {e}")