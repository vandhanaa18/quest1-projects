from adk_agents.planner_agent import PlannerAgent
from adk_agents.research_agent import ResearchAgent
from adk_agents.code_generator_agent import CodeGeneratorAgent
from adk_agents.reviewer_agent import ReviewerAgent
from adk_agents.test_agent import TestAgent


class Workflow:

    def __init__(self):
        self.planner = PlannerAgent()
        self.research = ResearchAgent()
        self.generator = CodeGeneratorAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TestAgent()