from agent import TinyAgent
from llm import LLM

agent = TinyAgent(llm=LLM(model="gemma4:e4b"))
print(agent.run("What is 2 + 2?"))
print(agent.trajectory.runs)

# from utils import TrajectoryViewer
# TrajectoryViewer(agent.trajectory)