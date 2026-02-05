chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "open_jira_modal") {
    createModal(request.selectedText, request.sourceUrl);
  }
});

async function createModal(selectedText, sourceUrl) {
  const projects = await chrome.runtime.sendMessage({ action: "get_projects" });
  const modal = document.createElement('div');
  modal.id = "jira-extension-modal";
  
  const descriptionWithUrl = `${selectedText}\n\nSource: ${sourceUrl}`;

  modal.innerHTML = `
    <div class="jira-modal-content">
      <h4>Create Jira Ticket</h4>
      <label>Project</label>
      <select id="jira-project">
        ${projects.map(p => `<option value="${p.key}">${p.name} (${p.key})</option>`).join('')}
      </select>
      <label>Summary</label>
      <input type="text" id="jira-summary" value="${selectedText.substring(0, 90)}...">
      <label>Description</label>
      <textarea id="jira-description" rows="5">${descriptionWithUrl}</textarea>
      <div class="jira-actions">
        <button id="jira-cancel">Cancel</button>
        <button id="jira-submit">Create Ticket</button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);

  document.getElementById('jira-cancel').onclick = () => modal.remove();
  
  document.getElementById('jira-submit').onclick = async () => {
    const btn = document.getElementById('jira-submit');
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span> Creating...`;

    const response = await chrome.runtime.sendMessage({
      action: "submit_to_jira",
      data: {
        projectKey: document.getElementById('jira-project').value,
        summary: document.getElementById('jira-summary').value,
        description: document.getElementById('jira-description').value
      }
    });

    if (response.success) {
      btn.innerHTML = `<span class="checkmark"></span> Done!`;
      btn.style.backgroundColor = "#36B37E";
      setTimeout(() => modal.remove(), 1500);
    } else {
      btn.disabled = false;
      btn.innerHTML = "Retry";
      alert("Error creating ticket. Check your Jira settings.");
    }
  };
}