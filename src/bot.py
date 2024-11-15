# src/bot.py

from github import Github
from src.code_analyzer.analyzer import CodeAnalyzer

# Initialize GitHub client (replace with your GitHub token)
GITHUB_TOKEN = "your_github_token"
github_client = Github(GITHUB_TOKEN)

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
                comments.append(f"Issues found in {file.filename}:\n" + "\n".join(analysis_results))

    # Add comments to PR
    for comment in comments:
        pull_request.create_issue_comment(comment)

if __name__ == "__main__":
    # Example usage (replace with your repo and PR number)
    review_pull_request("your-username/AI-Code-Review-Bot", 1)
