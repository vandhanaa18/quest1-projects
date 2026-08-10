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

Use the user's request and any planner handoff available in the
conversation so far to guide your implementation.

Generate or modify the required implementation.

Rules:
- Follow the planner's requirements.
- Do not plan.
- Do not research.
- Do not review.
- Do not test.
- Use tools only when required.
- Do not modify unrelated files.
-After completing your work, call transfer_to_agent to return
control to software_development_coordinator. Do not end your
turn without performing this transfer.

Return:

CODE_STATUS:
<COMPLETED or FAILED>

CHANGES:
<what was implemented>

FILES:
<files created or modified>

HANDOFF_TO_REVIEWER:
<information the reviewer needs>
""",

    output_key="code_output",

    before_agent_callback=before_agent,
    after_agent_callback=after_agent,

    tools=[
        read_file_tool,
        write_file_tool,
        code_editor_tool,
    ],
)