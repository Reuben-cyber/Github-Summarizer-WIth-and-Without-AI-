import requests
import os


def fetch_issues():
    owner = os.getenv("GITHUB_OWNER")
    repo = os.getenv("GITHUB_REPO")

    if not owner or not repo:
        raise ValueError("GITHUB_OWNER or GITHUB_REPO not set in .env")

    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github+json"
    }

    params = {
        "state": "open",
        "per_page": 20
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise RuntimeError(
            f"GitHub API error {response.status_code}: {response.text}"
        )

    # Exclude pull requests
    issues = [
        issue for issue in response.json()
        if "pull_request" not in issue
    ]

    return issues
