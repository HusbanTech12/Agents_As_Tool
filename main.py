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

# Main Agents That Routes To The Correct Translation To The Given Languages.

translation_agent = Agent(
    name='Translator Agent',
    instructions="""You are a translation assistant. Route the translation request to the correct laguages agent. Use the appropriate tool to convert English text into either Spanish , Korean or French based no the request.
    """,
    
    tools= [ 
            
          # Convert these Agents into Tools  
       spanish_agent.as_tool(
           tool_name='translate_to_spanish',
           tool_description="Translate the user's message to Spanish" 
       ),     
            
       korean_agent.as_tool(
           tool_name='translate_to_korean',
           tool_description="Translate the user's message to Korean" 
       ),
       french_agent.as_tool(
           tool_name='translate_to_french',
           tool_description="Translate the user's message to French" 
       ),     
    ]
    
    
    
    
)