// Popup Script
document.addEventListener('DOMContentLoaded', function() {
  const toggleButton = document.getElementById('toggleButton');
  const statusDiv = document.getElementById('status');
  
  // Danh sách các toggle cho từng loại form
  const formToggles = {
    'toggleFollowers': 't-followers-menu',
    'toggleHearts': 't-hearts-menu',
    'toggleCHearts': 't-chearts-menu',
    'toggleViews': 't-views-menu',
    'toggleShares': 't-shares-menu',
    'toggleFavorites': 't-favorites-menu',
    'toggleLivestream': 't-livestream-menu'
  };
  
  // Load trạng thái tổng
  chrome.storage.sync.get(['autoClickEnabled'], function(result) {
    const isEnabled = result.autoClickEnabled !== false; // Mặc định là true
    toggleButton.checked = isEnabled;
    updateStatus(isEnabled);
  });
  
  // Load trạng thái từng loại form
  chrome.storage.sync.get(['enabledForms'], function(result) {
    const enabledForms = result.enabledForms || ['t-hearts-menu']; // Mặc định bật Hearts
    
    Object.keys(formToggles).forEach(toggleId => {
      const toggle = document.getElementById(toggleId);
      const menuClass = formToggles[toggleId];
      toggle.checked = enabledForms.includes(menuClass);
      
      // Lắng nghe thay đổi
      toggle.addEventListener('change', function() {
        saveFormSettings();
      });
    });
  });
  
  // Lắng nghe thay đổi toggle tổng
  toggleButton.addEventListener('change', function() {
    const isEnabled = this.checked;
    
    // Lưu vào storage
    chrome.storage.sync.set({ autoClickEnabled: isEnabled }, function() {
      console.log('Auto click status saved:', isEnabled);
      updateStatus(isEnabled);
    });
  });
  
  // Lưu cài đặt từng loại form
  function saveFormSettings() {
    const enabledForms = [];
    
    Object.keys(formToggles).forEach(toggleId => {
      const toggle = document.getElementById(toggleId);
      const menuClass = formToggles[toggleId];
      if (toggle.checked) {
        enabledForms.push(menuClass);
      }
    });
    
    chrome.storage.sync.set({ enabledForms: enabledForms }, function() {
      console.log('Enabled forms saved:', enabledForms);
    });
  }
  
  function updateStatus(isEnabled) {
    if (isEnabled) {
      statusDiv.className = 'status enabled';
      statusDiv.textContent = '✅ Extension đang BẬT';
    } else {
      statusDiv.className = 'status disabled';
      statusDiv.textContent = '❌ Extension đang TẮT';
    }
  }
});
