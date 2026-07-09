from models import WorkflowData


class ReviewerAgent:

    def review(self, workflow: WorkflowData) -> WorkflowData:

        try:

            comments = []
            suggestions = []

            code = workflow.code.strip()

            critical_issue = False

            # Check 1 - Code exists
            if not code:
                comments.append("No code was generated.")
                suggestions.append("Generate the required implementation.")
                critical_issue = True

            # Check 2 - Return statement
            if "return" not in code:
                comments.append("Missing return statement.")
                suggestions.append("Add an appropriate return statement.")
                critical_issue = True

            # Check 3 - Exception handling
            if "try:" not in code:
                comments.append("Exception handling is missing.")
                suggestions.append("Use try-except blocks for error handling.")
                critical_issue = True

            # Check 4 - TODO comments
            if "TODO" in code:
                comments.append("Pending TODO comments found.")
                suggestions.append("Complete all pending TODO items.")

            # Check 5 - Documentation
            if '"""' not in code and "'''" not in code:
                comments.append("Documentation/comments are missing.")
                suggestions.append("Add comments or docstrings for better readability.")

            # Final Review Status
            if critical_issue:
                workflow.review_status = "Needs Rework"
            else:
                workflow.review_status = "Approved"

                if len(comments) == 0:
                    comments.append("Code review completed successfully.")

            workflow.review_comments = comments
            workflow.improvement_suggestions = suggestions

            return workflow

        except Exception as e:

            workflow.errors.append(
                f"ReviewerAgent: {str(e)}"
            )

            print("Reviewer Agent failed.")

            raise