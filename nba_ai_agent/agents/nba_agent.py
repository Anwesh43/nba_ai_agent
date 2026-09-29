from pydantic_ai import Agent 
from dotenv import load_dotenv 
from tools.nba_tools import getPlayerAdvanceStats, getTopNPlayersInASeason, getPlayerShotStats, getUpcomingGames, getPlayerImages
from prompts.nba_ai_prompt import SYSTEM_PROMPT
load_dotenv()

agent = Agent(
    system_prompt = SYSTEM_PROMPT, 
    tools = [getPlayerAdvanceStats, getTopNPlayersInASeason, getPlayerShotStats, getUpcomingGames, getPlayerImages],
    model = 'openai:gpt-5.2'
)

async def analyseNbaFacts(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')