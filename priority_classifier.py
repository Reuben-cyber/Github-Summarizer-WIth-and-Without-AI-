# THIS WILL WORK WHEN WE GET AI AFTER PAYMENT.
# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def classify_priority(issue):
#     prompt = f"""
# Classify the priority of this GitHub issue as one of:
# LOW, MEDIUM, HIGH, CRITICAL.

# Title: {issue['title']}
# Description: {issue.get('body', '')}
# Labels: {[l['name'] for l in issue['labels']]}
# Comments: {issue['comments']}

# Return only the priority.
# """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0
#     )

#     return response.choices[0].message.content.strip()


def classify_priority(issue):
    title = (issue.get("title") or "").lower()
    body = (issue.get("body") or "").lower()
    labels = [l["name"].lower() for l in issue.get("labels", [])]

    # 🚨 Explicit HIGH priority labels
    high_priority_labels = {
        "critical",
        "high-priority",
        "production",
        "bug",
        "security"
    }

    if any(label in high_priority_labels for label in labels):
        return "HIGH"

    # 🚨 High-impact keywords
    high_priority_keywords = [
        "crash",
        "crashes",
        "crashing",
        "outage",
        "down",
        "production",
        "all users",
        "unable to login",
        "cannot login",
        "payment failure",
        "data loss",
        "security",
        "blocked",
        "blocking",
        "core functionality",
        "system failure",
        "urgent",
        "immediate attention"
    ]

    combined_text = f"{title} {body}"

    if any(keyword in combined_text for keyword in high_priority_keywords):
        return "HIGH"

    return "LOW"
