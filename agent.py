from llm import LLM
from trajectory import Trajectory


class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self, llm: LLM) -> None:
       self.llm = llm
       self.trajectory = Trajectory()
       self.memory = None # Chapter 4
       self.tools = None # Chapter 5
       self.planner = None # Chapter 6

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step"""
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """Execute a tool action"""
        # Placeholder - will be implemented in later chapters
        return f"Executed action: {action}"