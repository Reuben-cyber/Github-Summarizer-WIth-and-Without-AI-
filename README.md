GitHub Issue Priority Notifier

GitHub Issue Priority Notifier is a Python-based automation tool that monitors issues in a GitHub repository, identifies high-priority problems, generates concise summaries, and sends daily email notifications to keep teams informed of critical developments.

The project was originally designed as an AI-powered system that leverages large language models to intelligently assess issue priority and generate human-readable summaries based on issue context, impact, and urgency. However, since AI model usage requires a paid API plan, the current implementation runs in a deterministic, rule-based mode while preserving the architecture for seamless AI re-enablement in the future.

Current Functionality

Fetches open issues from a specified GitHub repository using the GitHub REST API

Classifies issue priority using deterministic rules (keywords, labels, severity indicators, and impact-related terms)

Generates clear, readable summaries of issues

Sends email alerts for HIGH-priority issues via Gmail SMTP

Operates without dependency on paid AI services

AI-First Architecture (Currently Disabled)

Priority classification using natural language understanding

Context-aware issue summarization

Flexible prompt-driven logic for evolving priority definitions

⚠️ AI-based classification and summarization are temporarily disabled due to API cost constraints, but the codebase is structured to allow instant reactivation by enabling the AI modules and providing valid API credentials.

Tech Stack

Python

GitHub REST API

Gmail SMTP

Optional AI Integration (OpenAI / LLM-based — currently disabled)

Use Case

This tool is ideal for engineering teams that want to proactively track critical GitHub issues without manually monitoring repositories, while retaining the flexibility to upgrade to AI-driven intelligence when needed.
