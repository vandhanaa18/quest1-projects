from google.adk.agents import Agent

from ..providers.llm_provider import ModelProvider
from ..telemetry.callbacks import (
    before_agent,
    after_agent,
)

from ..tools.file_tool import (
    read_file_tool,
    write_file_tool,
)

from ..tools.code_editor_tool import (
    code_editor_tool,
)

code_generator_agent = Agent(
    name="code_generator_agent",
    model=ModelProvider.get_model(),
    description="Generates code from implementation requirements.",
    instruction="""
You are the Code Generator Agent.

Your responsibilities are:

1. Generate clean, maintainable code.
2. Follow best coding practices.
3. Add comments where appropriate.
4. Use the File Tool to read and write project files.
5. Use the Code Editor Tool when generating or modifying code.

Do not create implementation plans.
Do not research technologies.
Do not review code.
Do not test code.

Return only the implementation.
""",
    before_agent_callback=before_agent,
    after_agent_callback=after_agent,
    tools=[
        read_file_tool,
        write_file_tool,
        code_editor_tool,
    ],
)