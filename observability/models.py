from dataclasses import dataclass, field
from typing import List


@dataclass
class WorkflowData:

    task: str
    plan: str
    research: str
    code: str

    review_comments: List[str] = field(default_factory=list)

    improvement_suggestions: List[str] = field(default_factory=list)

    review_status: str = ""

    test_report: List[str] = field(default_factory=list)

detected_issues: List[str] = field(default_factory=list)

test_status: str = ""

errors: List[str] = field(default_factory=list)