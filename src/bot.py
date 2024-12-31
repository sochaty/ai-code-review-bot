# src/bot.py

import os
from github import Github
from src.code_analyzer.analyzer import CodeAnalyzer

# Initialize GitHub client (replace with your GitHub token)
github_token = os.getenv("GTHUB_TOKEN")
github_client = Github(github_token)

if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")

# Initialize code analyzer
analyzer = CodeAnalyzer()


def review_pull_request(repo_name, pr_number):
    repo = github_client.get_repo(repo_name)
    pull_request = repo.get_pull(pr_number)
    files = pull_request.get_files()

    comments = []
    for file in files:
        if file.filename.endswith(".py"):
            analysis_results = analyzer.analyze(file.patch)
            if analysis_results:
                comments.append(
                    f"Issues found in {file.filename}:\n" + "\n".join(analysis_results))

    # Add comments to PR
    for comment in comments:
        pull_request.create_issue_comment(comment)


if __name__ == "__main__":
    # Example usage (replace with your repo and PR number)
    review_pull_request("your-username/AI-Code-Review-Bot", 1)
