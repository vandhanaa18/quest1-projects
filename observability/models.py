from dataclasses import dataclass, field
from typing import List


@dataclass
class WorkflowData:
    # User Request
    task: str

    # Planner
    plan: str = ""
    execution_plan: List[str] = field(default_factory=list)
    current_agent: str = ""
    status: str = "pending"

    # Research
    research: str = ""

    # Code Generation
    code: str = ""

    # Review
    review_comments: List[str] = field(default_factory=list)
    improvement_suggestions: List[str] = field(default_factory=list)
    review_status: str = ""

    # Testing
    test_report: List[str] = field(default_factory=list)
    detected_issues: List[str] = field(default_factory=list)
    test_status: str = ""

    # Errors
    errors: List[str] = field(default_factory=list)

    # Memory / Context
    conversation_history: List[str] = field(default_factory=list)