// Load saved settings
document.addEventListener('DOMContentLoaded', () => {
  chrome.storage.sync.get(['isEnabled', 'enabledTypes', 'videoUrl'], (result) => {
    const isEnabled = result.isEnabled || false;
    const enabledTypes = result.enabledTypes || [];
    const videoUrl = result.videoUrl || '';

    // Set main toggle
    document.getElementById('toggleButton').checked = isEnabled;

    // Set individual toggles
    document.getElementById('toggleHearts').checked = enabledTypes.includes('hearts');
    document.getElementById('toggleViews').checked = enabledTypes.includes('views');

    // Set video URL
    document.getElementById('videoUrl').value = videoUrl;

    updateStatus();
  });

  // Main toggle handler
  document.getElementById('toggleButton').addEventListener('change', (e) => {
    const isEnabled = e.target.checked;
    chrome.storage.sync.set({ isEnabled }, () => {
      updateStatus();
      // Notify content script
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs[0]) {
          chrome.tabs.sendMessage(tabs[0].id, { action: 'toggle', enabled: isEnabled });
        }
      });
    });
  });

  // Individual toggle handlers
  document.getElementById('toggleHearts').addEventListener('change', (e) => {
    updateEnabledTypes();
  });

  document.getElementById('toggleViews').addEventListener('change', (e) => {
    updateEnabledTypes();
  });

  // Save URL button handler
  document.getElementById('saveUrl').addEventListener('click', () => {
    const videoUrl = document.getElementById('videoUrl').value.trim();
    chrome.storage.sync.set({ videoUrl }, () => {
      const button = document.getElementById('saveUrl');
      const originalText = button.textContent;
      button.textContent = 'Saved!';
      button.style.background = '#2e7d32';
      setTimeout(() => {
        button.textContent = originalText;
        button.style.background = '#4CAF50';
      }, 1500);
    });
  });
});

function updateEnabledTypes() {
  const enabledTypes = [];
  if (document.getElementById('toggleHearts').checked) {
    enabledTypes.push('hearts');
  }
  if (document.getElementById('toggleViews').checked) {
    enabledTypes.push('views');
  }

  chrome.storage.sync.set({ enabledTypes }, () => {
    updateStatus();
    // Notify content script
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs[0]) {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'updateTypes', enabledTypes });
      }
    });
  });
}

function updateStatus() {
  chrome.storage.sync.get(['isEnabled', 'enabledTypes'], (result) => {
    const isEnabled = result.isEnabled || false;
    const enabledTypes = result.enabledTypes || [];
    const statusDiv = document.getElementById('status');

    if (isEnabled) {
      if (enabledTypes.length > 0) {
        statusDiv.textContent = `Extension is ON - ${enabledTypes.join(', ')}`;
        statusDiv.className = 'status active';
      } else {
        statusDiv.textContent = 'Extension is ON - No types selected';
        statusDiv.className = 'status';
      }
    } else {
      statusDiv.textContent = 'Extension is OFF';
      statusDiv.className = 'status';
    }
  });
}

