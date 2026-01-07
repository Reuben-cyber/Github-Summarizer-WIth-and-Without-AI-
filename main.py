import os
from dotenv import load_dotenv

from github_client import fetch_open_issues
from priority_classifier import classify_priority
from summarizer import summarize_issue
from mailer import send_email


def main():
    # Load environment variables (.env locally, GitHub Secrets in Actions)
    load_dotenv()

    GITHUB_OWNER = os.getenv("GITHUB_OWNER")
    GITHUB_REPO = os.getenv("GITHUB_REPO")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # optional, but recommended

    EMAIL_TO = os.getenv("EMAIL_TO")

    if not GITHUB_OWNER or not GITHUB_REPO or not EMAIL_TO:
        raise ValueError("Missing required environment variables")

    # Fetch issues
    issues = fetch_open_issues(
        owner=GITHUB_OWNER,
        repo=GITHUB_REPO,
        token=GITHUB_TOKEN
    )

    if not issues:
        print("No open issues found.")
        return

    high_priority_issues = []

    for issue in issues:
        priority = classify_priority(issue)

        if priority == "HIGH":
            summary = summarize_issue(issue)
            high_priority_issues.append(summary)

    if not high_priority_issues:
        print("No HIGH priority issues today.")
        return

    # Prepare email content
    subject = f"[ALERT] {len(high_priority_issues)} High Priority GitHub Issues"
    body = "\n\n".join(high_priority_issues)

    send_email(
        subject=subject,
        body=body,
        recipient=EMAIL_TO
    )

    print("High priority issue email sent successfully.")


if __name__ == "__main__":
    main()
