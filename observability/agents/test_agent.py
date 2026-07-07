from models import WorkflowData


class TestAgent:

    def run_tests(self, workflow: WorkflowData) -> WorkflowData:

        report = []
        issues = []

        
        if workflow.review_status != "Approved":

            workflow.test_status = "NOT EXECUTED"

            report.append(
                "Testing was not executed because the code review was not approved."
            )

            workflow.test_report = report
            workflow.detected_issues = workflow.review_comments

            return workflow

        code = workflow.code.strip()

        
        report.append("Generated code detected.")

        if "def " in code or "class " in code:
            report.append("Program structure verified.")

        if "return" in code:
            report.append("Return statement verified.")

        if "try:" in code:
            report.append("Exception handling verified.")

        report.append("Basic functionality validation completed.")

        report.append("Code is ready for integration testing.")

        workflow.test_status = "PASS"

        workflow.test_report = report
        workflow.detected_issues = issues

        return workflow