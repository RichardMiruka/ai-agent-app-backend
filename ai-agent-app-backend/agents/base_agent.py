import os
from typing import Optional
from agno.agent import Agent
from agno.models.groq import Groq


class BaseAgent:
    """
    A base class for AI agents utilizing the Agno framework with the Groq LLaMA 3.3 70B model.

    This class provides a foundational structure for specialized agents by handling model 
    initialization and response retrieval.

    Attributes:
        name (str): The name of the agent.
        description (str): A brief description of the agent's purpose.
        avatar (str): Path to the avatar image (default: "default_avatar.png").
        model (Groq): The Groq model instance.
        agent (Agent): The Agno AI agent instance.
    """

    def __init__(self, name: str, description: str, avatar: Optional[str] = "default_avatar.png"):
        """
        Initializes the BaseAgent with a name, description, and optional avatar.

        Args:
            name (str): The agent's name.
            description (str): A short description of the agent.
            avatar (Optional[str], optional): The avatar image path. Defaults to "default_avatar.png".
        """
        self.name = name
        self.description = description
        self.avatar = avatar
        self.model = Groq(id="llama-3.3-70b-versatile")
        self.agent = Agent(model=self.model, markdown=True)

    def get_response(self, query: str, stream: bool = False):
        """
        Retrieves the AI-generated response to a given query.

        Args:
            query (str): The user's input query.
            stream (bool, optional): Whether to return a streamed response. Defaults to False.

        Returns:
            str or generator: The AI-generated response (full or streamed).
        """
        return self.agent.get_response(query, stream=stream)

    def print_response(self, query: str, stream: bool = True):
        """
        Prints the AI-generated response to the console.

        Args:
            query (str): The user's input query.
            stream (bool, optional): Whether to print a streamed response. Defaults to True.

        Returns:
            None: This method prints output but does not return a value.
        """
        return self.agent.print_response(query, stream=stream)
