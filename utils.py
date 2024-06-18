# type: ignore
from typing import TextIO
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv("config/.env")


def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    agent = create_csv_agent(
        llm, file, allow_dangerous_code=True, agent_type="tool-calling", verbose=False
    )

    result = agent.run(query)
    return result
