from strands.models import BedrockModel
from strands import Agent, tool
import subprocess

# Bedrock
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    region_name="us-east-1"
)

@tool
def run_command_in_shell(command: str) -> str:
    """
    Executes a shell command and returns its output or error message.

    Parameters:
    - command (str): The shell command to execute.

    Returns:
    - str: The standard output or error message from the command execution.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

agent = Agent(
    model=model,
    tools=[run_command_in_shell],
    )
    
message = input("Enter a message: ")
print('\n'+"-"*60+'\n')
while message !="exit":
    response = agent(message)
    print('\n'+"-"*60+'\n')
    message = input("Enter a message: ")
    print('\n'+"-"*60+'\n')
