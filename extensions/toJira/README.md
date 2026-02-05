# Jira Quick Capture Browser Extension

A lightweight Chrome Extension (Manifest V3) that allows users to highlight text on any webpage and instantly convert it into a Jira ticket via the right-click context menu.

## Features
- **Instant Injection:** Works on already-open tabs without needing a page refresh.
- **Context Preservation:** Automatically appends the source URL to the Jira description.
- **Project Selector:** Dynamically fetches and lists available Jira projects.
- **Visual Feedback:** Includes a loading spinner and a success checkmark with a direct link to the new ticket.

## Installation

1. **Download/Clone** this repository to a local folder.
2. Open Chrome and navigate to `chrome://extensions`.
3. Enable **Developer mode** (toggle in the top right).
4. Click **Load unpacked** and select the project folder.

## Setup (Crucial)

Before first use, you must configure your Jira credentials:
1. Click the **Extensions puzzle icon** in Chrome.
2. Find **Jira Quick Capture** and go to **Options** (or right-click the icon > Options).
3. Enter your:
   - **Jira Domain:** (e.g., `yourcompany.atlassian.net`)
   - **Atlassian Email:** The email you use to log in.
   - **API Token:** Generated from [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
4. Click **Save Credentials**.

## How to Use
1. Highlight any text on a webpage.
2. Right-click the selection.
3. Select **"Create Jira Ticket from Selection"**.
4. In the pop-up modal, choose your project, edit the summary if needed, and hit **Create**.