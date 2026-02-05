document.getElementById('save').addEventListener('click', () => {
  const data = {
    jiraDomain: document.getElementById('domain').value,
    jiraEmail: document.getElementById('email').value,
    jiraToken: document.getElementById('token').value
  };
  chrome.storage.local.set(data, () => {
    alert('Settings saved! You can now create tickets.');
  });
});

chrome.storage.local.get(['jiraDomain', 'jiraEmail', 'jiraToken'], (items) => {
  document.getElementById('domain').value = items.jiraDomain || '';
  document.getElementById('email').value = items.jiraEmail || '';
  document.getElementById('token').value = items.jiraToken || '';
});