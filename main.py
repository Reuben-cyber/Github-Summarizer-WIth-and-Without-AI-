from dotenv import load_dotenv
load_dotenv()

from github_client import fetch_issues
from priority_classifier import classify_priority
from summarizer import summarize_issue
from mailer import send_email


def run():
    print("Starting GitHub Issue Summarizer...\n")

    issues = fetch_issues()
    print(f"Fetched {len(issues)} open issues.\n")

    report = []

    for idx, issue in enumerate(issues, start=1):
        print(f"--------------------------------------------------")
        print(f"Issue {idx}: {issue['title']}")

        priority = classify_priority(issue)
        print(f"Priority classified as: {priority}")

        if priority in ["HIGH", "CRITICAL"]:
            print("Summarizing issue...")
            summary = summarize_issue(issue)

            report.append(f"""
Issue: {issue['title']}
Priority: {priority}

Summary:
{summary}

Link:
{issue['html_url']}
""")
        else:
            print("Skipping (not high priority).")

    print("\n--------------------------------------------------")

    if report:
        print("High priority issues found.")
        print("Sending email...\n")
        send_email("\n\n".join(report))
        print("✅ Email sent successfully.")
    else:
        print("ℹ️ No HIGH or CRITICAL priority issues found.")
        print("No email sent.")

    print("\nGitHub Issue Summarizer finished.")


if __name__ == "__main__":
    run()
