class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self):
       self.llm = None # Chapter 2 & 3
       self.memory = None # Chapter 4
       self.tools = None # Chapter 5
       self.planner = None # Chapter 6

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step"""
        # Placeholder - will be implemented in later chapters
        return f"Received: {task}"

    def _execute_action(self, action: str) -> str:
        """Execute a tool action"""
        # Placeholder - will be implemented in later chapters
        return f"Executed action: {action}"