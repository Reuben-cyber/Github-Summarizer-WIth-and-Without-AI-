# THIS WILL WORK WHEN WE GET AI AFTER PAYMENT.
# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def summarize_issue(issue):
#     prompt = f"""
# Summarize this GitHub issue for an engineering manager.
# Max 5 bullet points.

# Title: {issue['title']}
# Description: {issue.get('body', '')}
# """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.3
#     )

#     return response.choices[0].message.content.strip()

def summarize_issue(issue):
    title = issue.get("title", "No title")
    body = issue.get("body", "").strip()
    url = issue.get("html_url")

    summary_lines = [
        f"Title: {title}",
        "",
        "Summary:",
        body if body else "No description provided.",
        "",
        f"Link: {url}"
    ]

    return "\n".join(summary_lines)

