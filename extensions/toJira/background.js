chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "createJiraTicket",
    title: "Create Jira Ticket from Selection",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === "createJiraTicket") {
    // 1. Check if we can actually talk to this tab
    try {
      await chrome.tabs.sendMessage(tab.id, { 
        action: "open_jira_modal", 
        selectedText: info.selectionText,
        sourceUrl: tab.url
      });
    } catch (e) {
      // 2. If the script isn't there, tell the user why
      chrome.notifications.create({
        type: 'basic',
        iconUrl: 'icon.png',
        title: 'Extension Not Ready',
        message: 'Please refresh this page once to enable Jira capture.'
      });
      console.error("Connection failed: ", e.message);
    }
  }
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "get_projects") {
    fetchProjects().then(sendResponse);
    return true; 
  }
  if (request.action === "submit_to_jira") {
    performJiraUpload(request.data).then(result => sendResponse(result));
    return true;
  }
});

async function fetchProjects() {
  const { jiraToken, jiraEmail, jiraDomain } = await chrome.storage.local.get();
  try {
    const response = await fetch(`https://${jiraDomain}/rest/api/3/project`, {
      headers: { 'Authorization': `Basic ${btoa(jiraEmail + ":" + jiraToken)}` }
    });
    return await response.json();
  } catch (err) {
    return [];
  }
}

async function performJiraUpload(data) {
  const { jiraToken, jiraEmail, jiraDomain } = await chrome.storage.local.get();
  try {
    const response = await fetch(`https://${jiraDomain}/rest/api/3/issue`, {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${btoa(jiraEmail + ":" + jiraToken)}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fields: {
          project: { key: data.projectKey },
          summary: data.summary,
          description: {
            type: "doc", version: 1,
            content: [{ type: "paragraph", content: [{ type: "text", text: data.description }] }]
          },
          issuetype: { name: "Task" }
        }
      })
    });
    return { success: response.ok };
  } catch (err) {
    return { success: false };
  }
}