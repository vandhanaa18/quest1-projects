from models import WorkflowData


class ReviewerAgent:

    def review(self, workflow: WorkflowData) -> WorkflowData:

        comments = []
        suggestions = []

        code = workflow.code.strip()

        critical_issue = False

        
        if not code:
            comments.append("No code was generated.")
            suggestions.append("Generate the required implementation.")
            critical_issue = True

        
        if "return" not in code:
            comments.append("Missing return statement.")
            suggestions.append("Add an appropriate return statement.")
            critical_issue = True

       
        if "try:" not in code:
            comments.append("Exception handling is missing.")
            suggestions.append("Use try-except blocks for error handling.")
            critical_issue = True

        
        if "TODO" in code:
            comments.append("Pending TODO comments found.")
            suggestions.append("Complete all pending TODO items.")

        if '"""' not in code and "'''" not in code:
            comments.append("Documentation/comments are missing.")
            suggestions.append("Add comments or docstrings for better readability.")

        
        if critical_issue:
            workflow.review_status = "Needs Rework"
        else:
            workflow.review_status = "Approved"

            if len(comments) == 0:
                comments.append("Code review completed successfully.")

        workflow.review_comments = comments
        workflow.improvement_suggestions = suggestions

        return workflow