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
    description="Generates code and performs file operations when requested.",

    instruction="""
You are the Code Generator Agent.

Generate or modify code based on the user's request.

Rules:
- Keep responses concise.
- Do not explain your reasoning.
- Do not plan, research, review, or test.
- Use tools only when required.
- Do not make unnecessary tool calls.

File handling:
- For normal code requests, return the code directly.
- If the user asks to create or save a file, use the Write File Tool.
- If the user asks to modify an existing file, read the file first if needed, then use the Code Editor Tool.
- Do not read files unless their contents are required.
- Do not rewrite unrelated code.
- After successfully creating or modifying a file, briefly state what was changed.
- Do not return the complete file after a file operation unless the user explicitly asks to see it.
""",

    before_agent_callback=before_agent,
    after_agent_callback=after_agent,

    tools=[
        read_file_tool,
        write_file_tool,
        code_editor_tool,
    ],
)