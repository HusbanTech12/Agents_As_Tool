from agents import Runner,Agent 
from config import AgentConfig


spanish_agent = Agent(
    name = 'Spanish Agent',
    instructions= "You translate the user's message to Spanish"
)

korean_agent = Agent(
    name = 'korean Agent',
    instructions= "You translate the user's message to korean"
)

french_agent = Agent(
    name = 'French Agent',
    instructions= "You translate the user's message to french"
)
