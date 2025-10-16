
from google_adk.agent import LlmAgent, AgentConfig
from tool_definitions import TherapeuticComputeTool

# System instructions for the TxAgent
TX_AGENT_INSTRUCTIONS = """
As an expert therapeutic reasoning engine, your role is to analyze novel therapeutic ideas.

You must use multi-step, chain-of-thought reasoning in all your outputs to clearly explain your analytical process.

When a task requires heavy computation, such as molecular screening, you must use the `TherapeuticComputeTool`.

After calling this tool, confirm that you have offloaded the task and are awaiting the results, referencing the `job_name` returned by the tool for tracking purposes.
"""

class TxAgent(LlmAgent):
    """A specialized agent for therapeutic reasoning and analysis."""
    def __init__(self):
        # Configure the agent
        agent_config = AgentConfig(
            model="gemini-1.5-pro-001",
            instructions=[TX_AGENT_INSTRUCTIONS],
            tools=[TherapeuticComputeTool]
        )
        super().__init__(config=agent_config)

if __name__ == '__main__':
    # Instantiate the agent
    tx_agent = TxAgent()

    # Example prompt for local testing
    prompt = "We have a novel idea that molecule MOL-ABC-123 might be a high-affinity inhibitor for Protein-Z. Please conduct a full molecular screening."

    # Run the agent with the prompt
    for chunk in tx_agent.run(prompt):
        if chunk.text:
            print(chunk.text, end="")
        if chunk.tool_code:
            print(chunk.tool_code)
