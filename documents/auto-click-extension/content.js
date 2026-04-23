// Auto Click Search Button - Content Script
// ⚠️ CHỈ CHẠY TRÊN ZEFOY.COM
if (!window.location.hostname.includes('zefoy.com')) {
  console.log('[Auto Click] ⚠️ Extension chỉ chạy trên zefoy.com');
  console.log('[Auto Click] Current site:', window.location.hostname);
  // Dừng extension ngay
  throw new Error('Extension only works on zefoy.com');
}

console.log('[Auto Click] ✅ Extension loaded on zefoy.com');
console.log('[Auto Click] ℹ️ Status bar sẽ hiển thị ở cuối trang (không cần F12)');

let isEnabled = true;
let enabledForms = ['t-hearts-menu']; // Mặc định bật Hearts
let isCountdownActive = false;
let checkInterval = null;
let statusBar = null;
let isClicking = false; // Flag để tránh spam click
let isWaitingForVideo = false; // Flag để biết đang chờ video button

// Load cài đặt từ storage
chrome.storage.sync.get(['autoClickEnabled', 'enabledForms'], function(result) {
  isEnabled = result.autoClickEnabled !== false; // Mặc định là true
  enabledForms = result.enabledForms || ['t-hearts-menu']; // Mặc định bật Hearts
  console.log('[Auto Click] ✅ Settings loaded - Enabled:', isEnabled, 'Forms:', enabledForms);
  
  // Hiển thị status bar
  if (isEnabled) {
    showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
    startMonitoring();
  } else {
    showStatusOnPage('❌ Extension DISABLED - Click icon to enable');
  }
});

// Lắng nghe thay đổi storage
chrome.storage.onChanged.addListener(function(changes, namespace) {
  if (changes.autoClickEnabled) {
    isEnabled = changes.autoClickEnabled.newValue;
    console.log('[Auto Click] 🔄 Extension', isEnabled ? 'ENABLED' : 'DISABLED');
    
    if (isEnabled) {
      showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
      startMonitoring();
    } else {
      showStatusOnPage('❌ Extension DISABLED - Click icon to enable');
      stopMonitoring();
    }
  }
  
  if (changes.enabledForms) {
    enabledForms = changes.enabledForms.newValue || ['t-hearts-menu'];
    console.log('[Auto Click] 🔄 Enabled forms updated:', enabledForms);
  }
});

// ========================================
// HUMAN-LIKE CLICK FUNCTION
// ========================================
function humanClick(element) {
  if (!element) {
    console.log('[Auto Click] ⚠️ humanClick: element is null');
    return false;
  }
  
  console.log('[Auto Click] 🤖 Simulating HUMAN click...');
  
  try {
    // Get element position
    const rect = element.getBoundingClientRect();
    const x = rect.left + rect.width / 2 + (Math.random() * 10 - 5);  // Random offset
    const y = rect.top + rect.height / 2 + (Math.random() * 10 - 5);
    
    // Create realistic mouse events - Sử dụng options đơn giản hơn để tránh lỗi
    const baseOptions = {
      bubbles: true,
      cancelable: true,
      view: window
    };
    
    // Sequence: mouseover → mousedown → mouseup → click
    try {
      // 1. Mouseover (hover)
      const mouseoverEvent = new MouseEvent('mouseover', {
        ...baseOptions,
        clientX: x,
        clientY: y,
        button: 0
      });
      element.dispatchEvent(mouseoverEvent);
      console.log('[Auto Click] 👆 Dispatched: mouseover');
    } catch (e) {
      console.log('[Auto Click] ⚠️ mouseover failed:', e);
    }
    
    // Small delay
    setTimeout(() => {
      try {
        // 2. Mousedown
        const mousedownEvent = new MouseEvent('mousedown', {
          ...baseOptions,
          clientX: x,
          clientY: y,
          button: 0,
          buttons: 1
        });
        element.dispatchEvent(mousedownEvent);
        console.log('[Auto Click] 👇 Dispatched: mousedown');
      } catch (e) {
        console.log('[Auto Click] ⚠️ mousedown failed:', e);
      }
      
      // Small delay (simulate human click duration)
      setTimeout(() => {
        try {
          // 3. Mouseup
          const mouseupEvent = new MouseEvent('mouseup', {
            ...baseOptions,
            clientX: x,
            clientY: y,
            button: 0,
            buttons: 0
          });
          element.dispatchEvent(mouseupEvent);
          console.log('[Auto Click] 👆 Dispatched: mouseup');
        } catch (e) {
          console.log('[Auto Click] ⚠️ mouseup failed:', e);
        }
        
        try {
          // 4. Click
          const clickEvent = new MouseEvent('click', {
            ...baseOptions,
            clientX: x,
            clientY: y,
            button: 0,
            buttons: 0,
            detail: 1
          });
          element.dispatchEvent(clickEvent);
          console.log('[Auto Click] 👆 Dispatched: click');
        } catch (e) {
          console.log('[Auto Click] ⚠️ click event failed:', e);
          // Fallback: use native click
          console.log('[Auto Click] 🔄 Fallback: Using native click()');
          element.click();
        }
        
        // 5. Focus (if focusable)
        try {
          if (element.focus) {
            element.focus();
          }
        } catch (e) {
          console.log('[Auto Click] ⚠️ focus failed:', e);
        }
        
        console.log('[Auto Click] ✅ Human-like click COMPLETED');
      }, 50 + Math.random() * 50); // 50-100ms
    }, 50 + Math.random() * 50); // 50-100ms
    
    return true;
  } catch (error) {
    console.error('[Auto Click] ❌ Human click failed:', error);
    console.error('[Auto Click] ❌ Error details:', error.message, error.stack);
    // Fallback to normal click
    try {
      element.click();
      console.log('[Auto Click] ✅ Fallback: Native click() succeeded');
      return true;
    } catch (fallbackError) {
      console.error('[Auto Click] ❌ Fallback click also failed:', fallbackError);
      return false;
    }
  }
}

// Function hiển thị status bar trên trang (không cần F12)
function showStatusOnPage(message) {
  // Tạo status bar nếu chưa có
  if (!statusBar) {
    statusBar = document.createElement('div');
    statusBar.id = 'auto-click-status-bar';
    statusBar.style.cssText = `
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 12px 20px;
      font-family: Arial, sans-serif;
      font-size: 14px;
      font-weight: bold;
      z-index: 9999999;
      box-shadow: 0 -2px 10px rgba(0,0,0,0.3);
      display: flex;
      align-items: center;
      justify-content: space-between;
    `;
    
    // Thêm nút đóng
    const closeBtn = document.createElement('span');
    closeBtn.textContent = '✕';
    closeBtn.style.cssText = `
      cursor: pointer;
      font-size: 18px;
      padding: 0 10px;
      opacity: 0.8;
    `;
    closeBtn.onclick = () => {
      statusBar.style.display = 'none';
    };
    
    statusBar.innerHTML = `<span id="status-message"></span>`;
    statusBar.appendChild(closeBtn);
    
    // Đợi DOM ready
    if (document.body) {
      document.body.appendChild(statusBar);
    } else {
      document.addEventListener('DOMContentLoaded', () => {
        document.body.appendChild(statusBar);
      });
    }
  }
  
  // Update message
  const messageEl = statusBar ? statusBar.querySelector('#status-message') : null;
  if (messageEl) {
    messageEl.textContent = '🤖 [Auto Click] ' + message;
  }
  
  // Show status bar
  if (statusBar) {
    statusBar.style.display = 'flex';
  }
}

// Hiển thị status bar ngay (sẽ được update sau khi load settings)

function startMonitoring() {
  console.log('[Auto Click] Starting countdown monitoring...');
  
  // Kiểm tra mỗi giây
  if (checkInterval) {
    clearInterval(checkInterval);
  }
  
  checkInterval = setInterval(() => {
    checkCountdownAndClick();
  }, 500); // Check mỗi 0.5s để nhanh hơn
}

function stopMonitoring() {
  console.log('[Auto Click] Stopping countdown monitoring...');
  if (checkInterval) {
    clearInterval(checkInterval);
    checkInterval = null;
  }
}

// ========================================
// COUNTDOWN HELPERS (dùng chung toàn file)
// ========================================
const FORM_CONTAINER_SELECTOR = '.t-followers-menu, .t-hearts-menu, .t-chearts-menu, .t-views-menu, .t-shares-menu, .t-favorites-menu, .t-livestream-menu';
const COUNTDOWN_SELECTOR = '.views-countdown, .hearts-countdown, span.br.views-countdown, span.br';

function parseCountdownText(text) {
  const trimmed = (text || '').trim();
  if (!trimmed) {
    return {
      text: '',
      hasCountdown: false,
      isReady: false,
      isActive: false,
      totalSeconds: null,
      minutes: null,
      seconds: null
    };
  }

  const minuteMatch = trimmed.match(/(\d+)\s*minute/i);
  const secondMatch = trimmed.match(/(\d+)\s*second/i);
  const minutes = minuteMatch ? parseInt(minuteMatch[1], 10) : 0;
  const seconds = secondMatch ? parseInt(secondMatch[1], 10) : 0;
  const hasNumbers = Boolean(minuteMatch || secondMatch);
  const totalSeconds = hasNumbers ? minutes * 60 + seconds : null;
  const hasReadyWord = /READY/i.test(trimmed);
  const zeroMinute = /0\s*minute/i.test(trimmed);
  const zeroSecond = /0\s*second/i.test(trimmed);
  const hasCountdownKeywords = /(wait|minute|second|submit|countdown)/i.test(trimmed);

  const isReady = hasReadyWord || (hasNumbers && totalSeconds === 0) || (zeroMinute && zeroSecond);
  const hasCountdown = hasReadyWord || hasNumbers || hasCountdownKeywords;
  const isActive = hasCountdown && !isReady && (totalSeconds === null || totalSeconds > 0);

  return {
    text: trimmed,
    hasCountdown,
    isReady,
    isActive,
    totalSeconds,
    minutes,
    seconds
  };
}

function getCountdownInfo(root) {
  if (!root || typeof root.querySelector !== 'function') {
    return null;
  }

  let countdownElement = null;

  if (root.matches && root.matches(COUNTDOWN_SELECTOR)) {
    countdownElement = root;
  } else {
    countdownElement = root.querySelector(COUNTDOWN_SELECTOR);
  }

  if (!countdownElement) {
    return null;
  }

  const text = (countdownElement.textContent || countdownElement.innerText || '').trim();
  if (!text) {
    return null;
  }

  const state = parseCountdownText(text);
  if (!state.hasCountdown) {
    return null;
  }

  return {
    ...state,
    element: countdownElement
  };
}

function formatCountdownInfo(info) {
  if (!info) {
    return '';
  }

  if (typeof info.totalSeconds === 'number' && info.totalSeconds >= 0) {
    const minutes = Math.floor(info.totalSeconds / 60);
    const seconds = info.totalSeconds % 60;
    const paddedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
    return `${minutes}m ${paddedSeconds}s`;
  }

  return info.text;
}

function getFormContainer(form) {
  if (!form || typeof form.closest !== 'function') {
    return null;
  }
  return form.closest(FORM_CONTAINER_SELECTOR);
}

function getActiveCountdownInfo(form, resultDiv) {
  const divCountdown = getCountdownInfo(resultDiv);
  if (divCountdown && divCountdown.isActive) {
    return {
      ...divCountdown,
      location: 'resultDiv'
    };
  }

  const formContainer = getFormContainer(form);
  const containerCountdown = getCountdownInfo(formContainer);
  if (containerCountdown && containerCountdown.isActive) {
    return {
      ...containerCountdown,
      location: 'container'
    };
  }

  return null;
}

// Hàm tìm và hiển thị countdown từ tất cả các form đã bật
function updateCountdownStatus() {
  if (!isEnabled || isClicking || isWaitingForVideo) {
    return; // Không cập nhật nếu extension tắt hoặc đang click
  }
  
  let bestCountdownSeconds = Infinity;
  let bestCountdownText = '';
  let bestMenuLabel = '';
  
  // Tìm countdown trong tất cả các form đã bật
  enabledForms.forEach(menuClass => {
    const container = document.querySelector(`.${menuClass}`);
    if (container) {
      const formsInContainer = container.querySelectorAll('form[action]');
      formsInContainer.forEach(form => {
        const formAction = form.getAttribute('action');
        if (formAction && !formAction.startsWith('http') && !formAction.startsWith('/')) {
          const resultDiv = container.querySelector(`div#${formAction}`) || document.getElementById(formAction);
          const countdownInfo = getCountdownInfo(resultDiv) || getCountdownInfo(container);
          if (countdownInfo && countdownInfo.isActive) {
            const seconds = typeof countdownInfo.totalSeconds === 'number' ? countdownInfo.totalSeconds : Infinity;
            const menuLabel = menuClass.replace('t-', '').replace('-menu', '');
            
            if (seconds < bestCountdownSeconds) {
              bestCountdownSeconds = seconds;
              bestCountdownText = countdownInfo.text;
              bestMenuLabel = menuLabel;
            } else if (seconds === Infinity && bestCountdownSeconds === Infinity && !bestCountdownText) {
              // Không parse được số giây → hiển thị nguyên text
              bestCountdownText = countdownInfo.text;
              bestMenuLabel = menuLabel;
            }
          }
        }
      });
    }
  });
  
  // Cập nhật status bar với countdown
  if (bestCountdownSeconds !== Infinity) {
    const minutes = Math.floor(bestCountdownSeconds / 60);
    const seconds = bestCountdownSeconds % 60;
    showStatusOnPage(`⏳ Waiting: ${minutes}m ${seconds < 10 ? '0' + seconds : seconds}s - ${bestMenuLabel}`);
  } else if (bestCountdownText) {
    showStatusOnPage(`⏳ Waiting: ${bestCountdownText} - ${bestMenuLabel}`);
  } else {
    // Không có countdown → hiển thị trạng thái monitoring
    showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
  }
}

function checkCountdownAndClick() {
  if (!isEnabled) {
    console.log('[Auto Click] 🔍 DEBUG: checkCountdownAndClick - isEnabled = false, returning');
    return;
  }

  // ✅ TRÁNH SPAM CLICK: Nếu đang click hoặc đang chờ video → DỪNG!
  if (isClicking || isWaitingForVideo) {
    console.log('[Auto Click] ⏸️ Already clicking or waiting for video - Skipping check');
    // ✅ Vẫn cập nhật countdown status ngay cả khi đang click
    updateCountdownStatus();
    return;
  }

  console.log('[Auto Click] 🔍 DEBUG: checkCountdownAndClick() called!');
  
  // ✅ Cập nhật countdown status trước khi check
  updateCountdownStatus();

  // ✅ ƯU TIÊN: TÌM VÀ CLICK SEARCH BUTTON ĐÚNG THEO FORM
  // Logic: Kiểm tra countdown trong div result của từng form
  // Chỉ click Search khi countdown trong div đó ready hoặc div trống
  // Logic: Form có action = id của div result
  // Tìm tất cả các form có action, kiểm tra div result tương ứng
  let targetForm = null;
  let targetResultDiv = null;
  let targetSearchButton = null;
  
  // Tìm tất cả các form có action (không phải URL đầy đủ)
  // CHỈ TÌM TRONG CÁC CONTAINER CÓ CLASS ĐÃ BẬT
  let allForms = [];
  enabledForms.forEach(menuClass => {
    const container = document.querySelector(`.${menuClass}`);
    if (container) {
      const formsInContainer = container.querySelectorAll('form[action]');
      formsInContainer.forEach(form => {
        // ✅ ĐẢM BẢO: Form phải trong container đúng class
        const formContainer = form.closest(`.${menuClass}`);
        if (formContainer) {
          allForms.push({ form: form, menuClass: menuClass });
          console.log('[Auto Click] 🔍 Found form in', menuClass, 'with action:', form.getAttribute('action'));
        }
      });
    }
  });
  
  console.log('[Auto Click] 🔍 Found', allForms.length, 'forms in enabled menus:', enabledForms);
  
  for (let { form, menuClass } of allForms) {
    const formAction = form.getAttribute('action');
    // Bỏ qua nếu action là URL đầy đủ
    if (formAction && !formAction.startsWith('http') && !formAction.startsWith('/')) {
      // ✅ ĐẢM BẢO: Form phải trong container đúng class đã bật
      const formContainer = form.closest(`.${menuClass}`);
      if (!formContainer) {
        console.log('[Auto Click] ⏭️ Form not in container', menuClass, '- skipping');
        continue;
      }
      
      // Tìm div có id = form.action (chỉ trong container này để tránh lấy nhầm)
      let resultDiv = formContainer.querySelector(`div#${formAction}`);
      // Nếu không tìm thấy trong container, thử tìm global
      if (!resultDiv) {
        resultDiv = document.getElementById(formAction);
        // Kiểm tra resultDiv có trong container đúng không
        if (resultDiv && !formContainer.contains(resultDiv)) {
          console.log('[Auto Click] ⚠️ Result div', formAction, 'not in container', menuClass, '- skipping');
          continue;
        }
      }
      
      if (resultDiv) {
        console.log('[Auto Click] 🔍 Found form with action:', formAction, 'in', menuClass, '→ result div:', resultDiv.id);
        
        // ✅ QUAN TRỌNG: Kiểm tra countdown trong result div này TRƯỚC
        const divCountdownInfo = getCountdownInfo(resultDiv);
        let divShouldClick = false;
        if (divCountdownInfo) {
          if (divCountdownInfo.isActive) {
            console.log('[Auto Click] ⏳ Countdown in div', formAction, ':', formatCountdownInfo(divCountdownInfo), '- WAITING... (SKIP THIS FORM)');
            continue; // Bỏ qua form này, chờ countdown xong
          }
          
          if (divCountdownInfo.isReady) {
            divShouldClick = true;
            console.log('[Auto Click] ✅ Countdown in div', formAction, 'is READY! Text:', divCountdownInfo.text);
          }
        } else {
          // ✅ QUAN TRỌNG: Không có countdown trong div → kiểm tra countdown ở cấp container/form
          // Countdown có thể ở nơi khác trong container, không chỉ trong resultDiv
          const containerCountdownInfo = getCountdownInfo(formContainer);
          if (containerCountdownInfo) {
            if (containerCountdownInfo.isActive) {
              console.log('[Auto Click] ⏳ Countdown in container', menuClass, ':', formatCountdownInfo(containerCountdownInfo), '- WAITING... (SKIP THIS FORM)');
              continue; // Bỏ qua form này, check form khác
            }
            // Nếu countdown ở container READY → xem như không còn countdown → tiếp tục logic bên dưới
          }
          
          // ✅ CHỈ KHI KHÔNG CÓ COUNTDOWN HOẶC COUNTDOWN = READY → mới kiểm tra button submit
          const htmlLength = resultDiv.innerHTML.trim().length;
          
          // Tìm button submit trong div (video/heart button)
          const submitButton = resultDiv.querySelector('.w1c button.wbutton, .w1f button.wbutton, button.wbutton, .w1c button[type="submit"], .w1f button[type="submit"]');
          
          if (submitButton) {
            // Có button submit → click button submit đó, không click Search
            console.log('[Auto Click] ✅ Found submit button in div', formAction, '→ Will click submit button!');
            const submitForm = submitButton.closest('form');
            if (submitForm) {
              // Click submit button (video/heart)
              isClicking = true;
              isWaitingForVideo = true;
              stopMonitoring();
              showStatusOnPage('✅ Clicking submit button...');
              
              setTimeout(() => {
                humanClick(submitButton);
                showNotification('✅ Clicked submit button!');
                
                // Đợi countdown xuất hiện sau khi click submit
                setTimeout(() => {
                  isClicking = false;
                  isWaitingForVideo = false;
                  if (isEnabled) {
                    console.log('[Auto Click] 🔄 Restarting monitoring after submit button click...');
                    showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
                    startMonitoring();
                  }
                }, 3000 + Math.random() * 1000); // Đợi 3-4s để countdown xuất hiện (giảm từ 5-7s)
              }, 200); // Giảm delay trước khi click từ 500ms xuống 200ms
              
              return; // Dừng, không tìm form khác
            } else {
              // Không có form, click button trực tiếp
              isClicking = true;
              isWaitingForVideo = true;
              stopMonitoring();
              showStatusOnPage('✅ Clicking submit button...');
              
              setTimeout(() => {
                humanClick(submitButton);
                showNotification('✅ Clicked submit button!');
                
                setTimeout(() => {
                  isClicking = false;
                  isWaitingForVideo = false;
                  if (isEnabled) {
                    console.log('[Auto Click] 🔄 Restarting monitoring after submit button click...');
                    showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
                    startMonitoring();
                  }
                }, 3000 + Math.random() * 1000); // Đợi 3-4s để countdown xuất hiện (giảm từ 5-7s)
              }, 200); // Giảm delay trước khi click từ 500ms xuống 200ms
              
              return; // Dừng
            }
          } else if (htmlLength === 0) {
            // Div trống VÀ không có countdown → click Search
            divShouldClick = true;
            console.log('[Auto Click] ✅ Div', formAction, 'is empty and no countdown - can click Search!');
          } else {
            // Div có nội dung nhưng không có button submit VÀ không có countdown → có thể có error, click Search lại
            divShouldClick = true;
            console.log('[Auto Click] ✅ Div', formAction, 'has content but no submit button and no countdown - can click Search!');
          }
        }
        
        // Nếu div này ready để click Search → chọn form này
        if (divShouldClick) {
          // Tìm search button trong form này
          const searchBtn = form.querySelector('button.disableButton, button[type="submit"]');
          if (searchBtn) {
            const text = searchBtn.textContent || searchBtn.innerText || '';
            const html = searchBtn.innerHTML || '';
            const hasSearchText = text.includes('Search') || text.includes('search');
            const hasSearchIcon = html.includes('fa-search');
            
            if (hasSearchText || hasSearchIcon) {
              const isEnabled = !searchBtn.disabled && !searchBtn.classList.contains('disabled');
              const hasDisableButtonClass = searchBtn.classList.contains('disableButton');
              
              if (isEnabled || hasDisableButtonClass) {
                targetForm = form;
                targetResultDiv = resultDiv;
                targetSearchButton = searchBtn;
                console.log('[Auto Click] ✅ Selected form with action:', formAction, 'in', menuClass, '→ Search button ready!');
                break; // Tìm thấy form phù hợp → dừng
              }
            }
          }
        }
      }
    }
  }
  
  // Nếu tìm được form và search button → Click NGAY!
  if (targetSearchButton && targetForm && targetResultDiv) {
    console.log('[Auto Click] ✅ PRIORITY: Found correct form and Search button → CLICKING!');
    console.log('[Auto Click] 🔍 Form action:', targetForm.getAttribute('action'), '→ Result div id:', targetResultDiv.id);
    
    // ✅ TRÁNH SPAM CLICK: Set flag và dừng monitoring
    isClicking = true;
    isWaitingForVideo = true;
    stopMonitoring(); // Dừng monitoring để tránh spam click
    
    showStatusOnPage('✅ Clicking Search...');
    console.log('[Auto Click] 🔍 DEBUG: Calling clickSearchButton() with correct form!');
    clickSearchButton(targetSearchButton, targetForm, targetResultDiv);
    return; // DỪNG Ở ĐÂY
  } else {
    console.log('[Auto Click] ⚠️ No ready form found to click Search button');
  }
}

function clickSearchButtonWithRetry(retryCount = 0, form = null, resultDiv = null) {
  console.log(`[Auto Click] 🔄 Retry ${retryCount}: Clicking Search button...`);
  showStatusOnPage(`🔄 Retry ${retryCount}: Clicking Search...`);
  
  // ✅ Set flag khi retry
  isClicking = true;
  isWaitingForVideo = true;
  
  // Nếu không có form/resultDiv, tìm từ searchButton
  let searchButton = null;
  if (form) {
    // ✅ Tìm searchButton trong form đã cho
    searchButton = form.querySelector('button.disableButton, button[type="submit"]');
  } else {
    // Nếu không có form, tìm searchButton trong container đã bật
    enabledForms.forEach(menuClass => {
      const container = document.querySelector(`.${menuClass}`);
      if (container && !searchButton) {
        searchButton = container.querySelector('button.disableButton, button[type="submit"]');
        if (searchButton) {
          form = searchButton.closest('form');
        }
      }
    });
    // Nếu vẫn không tìm thấy, tìm global
    if (!searchButton) {
      searchButton = document.querySelector('button.disableButton');
    }
  }
  
  if (!form && searchButton) {
    form = searchButton.closest('form');
  }
  
  if (!resultDiv && form) {
    const formAction = form.getAttribute('action');
    if (formAction && !formAction.startsWith('http') && !formAction.startsWith('/')) {
      const formContainer = getFormContainer(form);
      if (formContainer) {
        resultDiv = formContainer.querySelector(`div#${formAction}`);
        if (!resultDiv) {
          resultDiv = document.getElementById(formAction);
          if (resultDiv && !formContainer.contains(resultDiv)) {
            console.log('[Auto Click] ⚠️ Result div', formAction, 'not in form container in retry - may be wrong form');
            resultDiv = null;
          }
        }
      } else {
        resultDiv = document.getElementById(formAction);
      }
    }
  }

  // Không click Search nếu countdown vẫn đang chạy
  if (form) {
    const activeCountdown = getActiveCountdownInfo(form, resultDiv);
    if (activeCountdown) {
      console.log('[Auto Click] ⏳ Countdown still active - Skip Search click. Text:', activeCountdown.text);
      showStatusOnPage(`⏳ Countdown active (${formatCountdownInfo(activeCountdown)}) - waiting...`);
      isWaitingForVideo = false;
      isClicking = false;
      setTimeout(() => {
        if (isEnabled) {
          startMonitoring();
        }
      }, 1500);
      return;
    }
  }
  
  if (searchButton && !searchButton.disabled) {
    // ✅ Fix: Kiểm tra và fix input field + form validation
    // Sử dụng form đã có hoặc tìm từ searchButton
    if (!form) {
      form = searchButton.closest('form');
    }
    if (form) {
      // Disable HTML5 form validation
      form.noValidate = true;
      
      const input = form.querySelector('input[type="search"], input[type="text"]');
      if (input) {
        if (input.required && !input.value.trim()) {
          console.log('[Auto Click] ⚠️ Input field is required but empty, fixing...');
          try {
            // Remove required attribute
            input.removeAttribute('required');
            // Also set a placeholder value if still empty (some sites need this)
            if (!input.value.trim()) {
              input.value = ' '; // Space character
            }
            console.log('[Auto Click] ✅ Fixed input field (removed required, added space)');
          } catch (e) {
            console.log('[Auto Click] ⚠️ Could not fix input field:', e);
          }
        }
      }
    }
    
    // Use human-like click
    humanClick(searchButton);
    showNotification(`🔄 Retry ${retryCount}: Clicked Search!`);
    
    // ✅ Reset flag sau khi click xong
    setTimeout(() => {
      isClicking = false;
      console.log('[Auto Click] ✅ Retry click completed, reset isClicking flag');
    }, 1000);
    
    // Monitor kết quả với retry count - Đợi để server xử lý và video button xuất hiện
    // Pass form và resultDiv để đảm bảo tìm đúng video button
    setTimeout(() => {
      waitForVideoOrSearchReEnabled(searchButton, retryCount, form, resultDiv);
    }, 1000 + Math.random() * 1000); // Đợi 1-2s để server xử lý và video button xuất hiện (giảm từ 3-5s)
  } else {
    console.log('[Auto Click] ⚠️ Search button not ready for retry');
    // Reset flag và restart monitoring nếu button không sẵn sàng
    isWaitingForVideo = false;
    isClicking = false;
    setTimeout(() => {
      if (isEnabled) {
        startMonitoring();
      }
    }, 2000);
  }
}

function clickSearchButton(searchButton, form, resultDiv) {
  // Nếu không có tham số, tìm lại (backward compatibility)
  if (!searchButton) {
    console.log('[Auto Click] 🔍 Searching for Search button...');
    searchButton = document.querySelector('button.disableButton');
    if (!searchButton) {
      const allButtons = document.querySelectorAll('button[type="submit"]');
      for (let btn of allButtons) {
        const text = btn.textContent || btn.innerText || '';
        const html = btn.innerHTML || '';
        if ((text.includes('Search') || html.includes('fa-search')) && 
            (btn.classList.contains('disableButton') || !btn.disabled)) {
          searchButton = btn;
          break;
        }
      }
    }
  }
  
  if (!form && searchButton) {
    form = searchButton.closest('form');
  }
  
  if (!resultDiv && form) {
    const formAction = form.getAttribute('action');
    if (formAction && !formAction.startsWith('http') && !formAction.startsWith('/')) {
      resultDiv = document.getElementById(formAction);
    }
  }

  // Không click lại nếu countdown vẫn đang chạy
  if (form) {
    const activeCountdown = getActiveCountdownInfo(form, resultDiv);
    if (activeCountdown) {
      console.log('[Auto Click] ⏳ Countdown still active - Skip retry Search. Text:', activeCountdown.text);
      showStatusOnPage(`⏳ Countdown active (${formatCountdownInfo(activeCountdown)}) - waiting...`);
      isWaitingForVideo = false;
      isClicking = false;
      setTimeout(() => {
        if (isEnabled) {
          startMonitoring();
        }
      }, 1500);
      return;
    }
  }
  
  if (searchButton) {
    console.log('[Auto Click] ✅ Search button found! Clicking...');
    if (form && resultDiv) {
      console.log('[Auto Click] 🔍 Form action:', form.getAttribute('action'), '→ Result div id:', resultDiv.id);
    }
    showStatusOnPage('✅ Clicking Search...');
    
    // ✅ Fix: Kiểm tra và fix input field + form validation
    if (form) {
      // Disable HTML5 form validation
      form.noValidate = true;
      
      const input = form.querySelector('input[type="search"], input[type="text"]');
      if (input) {
        if (input.required && !input.value.trim()) {
          console.log('[Auto Click] ⚠️ Input field is required but empty, fixing...');
          try {
            // Remove required attribute
            input.removeAttribute('required');
            // Also set a placeholder value if still empty (some sites need this)
            if (!input.value.trim()) {
              input.value = ' '; // Space character
            }
            console.log('[Auto Click] ✅ Fixed input field (removed required, added space)');
          } catch (e) {
            console.log('[Auto Click] ⚠️ Could not fix input field:', e);
          }
        }
      }
    }
    
    // Use human-like click
    humanClick(searchButton);
    showNotification('✅ Clicked Search button!');
    
    // ✅ Reset flag sau khi click xong
    setTimeout(() => {
      isClicking = false;
      console.log('[Auto Click] ✅ Click completed, reset isClicking flag');
    }, 1000); // Đợi 1s để đảm bảo click đã hoàn thành
    
    // Monitor kết quả - Đợi để server xử lý và video button xuất hiện
    // Pass form và resultDiv để đảm bảo tìm đúng video button
    setTimeout(() => {
      waitForVideoOrSearchReEnabled(searchButton, 0, form, resultDiv);
    }, 1000 + Math.random() * 1000); // Đợi 1-2s để server xử lý và video button xuất hiện (giảm từ 3-5s)
  } else {
    console.log('[Auto Click] ⚠️ Search button NOT found!');
    showStatusOnPage('⚠️ Search button not found...');
  }
}

function waitForVideoOrSearchReEnabled(searchButton, retryCount = 0, form = null, resultDiv = null) {
  const maxRetries = 3; // Giảm max retries để tránh spam click
  const maxAttempts = 20; // Giảm max attempts (10s với interval 500ms) vì button xuất hiện sau 1-2s
  let attempts = 0;
  
  console.log('[Auto Click] 🔍 Waiting for video button or search re-enabled... (retry:', retryCount, '/', maxRetries, ')');
  
  // Nếu không có form/resultDiv, tìm từ searchButton
  if (!form && searchButton) {
    form = searchButton.closest('form');
  }
  
  if (!resultDiv && form) {
    const formAction = form.getAttribute('action');
    if (formAction && !formAction.startsWith('http') && !formAction.startsWith('/')) {
      const formContainer = getFormContainer(form);
      if (formContainer) {
        resultDiv = formContainer.querySelector(`div#${formAction}`);
        if (!resultDiv) {
          resultDiv = document.getElementById(formAction);
          if (resultDiv && !formContainer.contains(resultDiv)) {
            console.log('[Auto Click] ⚠️ Result div', formAction, 'not in form container - may be wrong form');
            resultDiv = null;
          }
        }
      } else {
        resultDiv = document.getElementById(formAction);
      }
    }
  }
  
  // Nếu vẫn không tìm thấy, thử tìm sibling
  if (!resultDiv && form) {
    let sibling = form.nextElementSibling;
    while (sibling && sibling.tagName !== 'DIV') {
      sibling = sibling.nextElementSibling;
    }
    resultDiv = sibling;
  }
  
  if (!form || !resultDiv) {
    console.log('[Auto Click] ⚠️ Form or resultDiv not found');
    isWaitingForVideo = false;
    isClicking = false;
    if (isEnabled) {
      startMonitoring();
    }
    return;
  }
  
  // ✅ ĐẢM BẢO: Form và resultDiv phải khớp nhau
  const formAction = form.getAttribute('action');
  if (formAction && resultDiv.id !== formAction) {
    console.log('[Auto Click] ⚠️ Form action', formAction, 'does not match result div id', resultDiv.id, '- may be wrong form');
  }
  
  // ✅ ĐẢM BẢO: Form phải trong container đã bật
  const formContainer = getFormContainer(form);
  if (formContainer) {
    const containerClass = Array.from(formContainer.classList).find(cls => cls.startsWith('t-') && cls.endsWith('-menu'));
    if (containerClass && !enabledForms.includes(containerClass)) {
      console.log('[Auto Click] ⚠️ Form in container', containerClass, 'is not enabled - stopping');
      isWaitingForVideo = false;
      isClicking = false;
      if (isEnabled) {
        startMonitoring();
      }
      return;
    }
  }
  
  console.log('[Auto Click] 🔍 Using form action:', formAction, '→ result div id:', resultDiv.id);
  
  const checkInterval = setInterval(() => {
    attempts++;
    // Chỉ log mỗi 2 attempts để giảm spam logs
    if (attempts % 2 === 0 || attempts <= 5) {
      console.log(`[Auto Click] 🔍 Attempt ${attempts}/${maxAttempts} - Video: CHECKING..., Search re-enabled: CHECKING...`);
    }
    
    // ✅ ƯU TIÊN 1: TÌM VIDEO BUTTON TRƯỚC
    // Sử dụng resultDiv đã được xác định (id = form.action)
    
    let videoButton = null;
    let isVisible = false;
    let parentVisible = false;
    
    if (resultDiv) {
      console.log('[Auto Click] ✅ Found result div:', resultDiv.id || 'no-id');
      
      // ✅ ƯU TIÊN: Tìm video button trong .w1c hoặc .w1f (nơi button xuất hiện)
      // Case 2: Button heart/video nằm trong <div class="w1c"> hoặc <div class="w1f">
      const w1c = resultDiv.querySelector('.w1c');
      const w1f = resultDiv.querySelector('.w1f');
      
      if (w1c) {
        videoButton = w1c.querySelector('button.wbutton') || w1c.querySelector('button[type="submit"]');
        console.log('[Auto Click] 🔍 Found .w1c container, looking for button inside...');
      } else if (w1f) {
        videoButton = w1f.querySelector('button.wbutton') || w1f.querySelector('button[type="submit"]');
        console.log('[Auto Click] 🔍 Found .w1f container, looking for button inside...');
      }
      
      // Nếu không tìm thấy trong .w1c/.w1f, tìm trong toàn bộ resultDiv
      if (!videoButton) {
        const allButtonsInDiv = resultDiv.querySelectorAll('button[type="submit"], button.wbutton');
        for (let btn of allButtonsInDiv) {
          // ✅ LOẠI TRỪ: Không phải Search button (có class disableButton hoặc text "Search")
          const text = btn.textContent || btn.innerText || '';
          const hasSearchText = text.includes('Search') || text.includes('search');
          const hasSearchIcon = btn.innerHTML.includes('fa-search');
          const isSearchButton = btn.classList.contains('disableButton') || hasSearchText || hasSearchIcon;
          
          if (!isSearchButton) {
            videoButton = btn;
            console.log('[Auto Click] ✅ Found video button in resultDiv (not Search button)');
            break;
          }
        }
      }
      
      // ✅ ĐẢM BẢO: Video button không phải là Search button
      if (videoButton) {
        const text = videoButton.textContent || videoButton.innerText || '';
        const hasSearchText = text.includes('Search') || text.includes('search');
        const hasSearchIcon = videoButton.innerHTML.includes('fa-search');
        const isSearchButton = videoButton.classList.contains('disableButton') || hasSearchText || hasSearchIcon;
        
        if (isSearchButton) {
          console.log('[Auto Click] ⚠️ Found button is Search button, skipping...');
          videoButton = null; // Reset để tìm lại
        }
      }
      
      // Debug: Log HTML và buttons trong resultDiv để debug
      if (!videoButton && attempts <= 5) {
        const allButtons = resultDiv.querySelectorAll('button');
        const htmlLength = resultDiv.innerHTML.trim().length;
        const hasW1c = resultDiv.querySelector('.w1c') !== null;
        const hasW1f = resultDiv.querySelector('.w1f') !== null;
        
        console.log('[Auto Click] 🔍 DEBUG: Result div state:', {
          htmlLength: htmlLength,
          hasW1c: hasW1c,
          hasW1f: hasW1f,
          buttonCount: allButtons.length,
          innerHTML: htmlLength > 0 ? resultDiv.innerHTML.substring(0, 200) + '...' : 'EMPTY'
        });
        
        if (allButtons.length > 0) {
          allButtons.forEach((btn, idx) => {
            const text = btn.textContent || btn.innerText || '';
            const isSearch = btn.classList.contains('disableButton') || text.includes('Search');
            console.log(`[Auto Click]   Button ${idx}:`, {
              text: text.trim(),
              classes: btn.className,
              type: btn.type,
              visible: btn.offsetParent !== null,
              isSearchButton: isSearch
            });
          });
        }
      }
      
      if (videoButton) {
        // ✅ DEBUG CHI TIẾT: Tại sao button bị hidden?
        if (attempts <= 5) {
          const computedStyle = window.getComputedStyle(videoButton);
          const parent = videoButton.closest('.w1c, .w2c, .w1f, .w2f');
          console.log('[Auto Click] 🔍 DEBUG Video Button Visibility (in resultDiv):', {
            offsetParent: videoButton.offsetParent !== null,
            display: videoButton.style.display,
            computedDisplay: computedStyle.display,
            visibility: computedStyle.visibility,
            opacity: computedStyle.opacity,
            hasNonecClass: videoButton.classList.contains('nonec'),
            classes: videoButton.className,
            parent: parent ? {
              tag: parent.tagName,
              classes: parent.className,
              offsetParent: parent.offsetParent !== null,
              display: parent.style.display,
              computedDisplay: window.getComputedStyle(parent).display
            } : 'no parent',
            rect: videoButton.getBoundingClientRect()
          });
        }
        
        // Check visibility - Button phải không có class 'nonec' (error span có class này)
        const computedStyle = window.getComputedStyle(videoButton);
        isVisible = videoButton.offsetParent !== null && 
                    computedStyle.display !== 'none' &&
                    computedStyle.visibility !== 'hidden' &&
                    computedStyle.opacity !== '0' &&
                    !videoButton.classList.contains('nonec');
        
        // Check parent visibility - Ưu tiên check .w1c hoặc .w1f (nơi button thực sự nằm)
        const w1cParent = videoButton.closest('.w1c');
        const w1fParent = videoButton.closest('.w1f');
        const parent = w1cParent || w1fParent || videoButton.closest('.w2c, .w2f');
        
        if (parent) {
          const parentStyle = window.getComputedStyle(parent);
          parentVisible = parent.offsetParent !== null && 
                          parentStyle.display !== 'none' &&
                          parentStyle.visibility !== 'hidden';
          console.log('[Auto Click] 🔍 Parent container:', parent.className, 'visible:', parentVisible);
        } else {
          parentVisible = true; // Không có parent container → visible
        }
        
        console.log('[Auto Click] 🔍 Video button found - visible:', isVisible, 'parent visible:', parentVisible);
      } else {
        console.log('[Auto Click] ⚠️ Video button NOT found in result div');
        
        // ✅ DEBUG: Kiểm tra xem result div có đang được populate không
        if (attempts <= 10) {
          const htmlLength = resultDiv.innerHTML.trim().length;
          const hasContent = htmlLength > 50; // Có nội dung đáng kể
          const hasW1c = resultDiv.querySelector('.w1c') !== null;
          const hasW1f = resultDiv.querySelector('.w1f') !== null;
          
          if (!hasContent && !hasW1c && !hasW1f) {
            console.log('[Auto Click] ⏳ Result div still empty, waiting for server response...');
            // Result div vẫn trống → đợi thêm
          } else if (hasW1c || hasW1f) {
            console.log('[Auto Click] ⚠️ .w1c/.w1f found but no video button inside');
          } else {
            console.log('[Auto Click] ⚠️ Result div has content but no video button structure');
          }
        }
        // ✅ KHÔNG TÌM TRONG CONTAINER RỘNG - Chỉ tìm trong resultDiv để tránh click nhầm form khác
      }
    } else {
      console.log('[Auto Click] ⚠️ Result div NOT found - Cannot find video button without result div');
      // ✅ KHÔNG TÌM TRONG CONTAINER RỘNG - Cần resultDiv để đảm bảo đúng form
    }
    
    // ✅ ƯU TIÊN 2: NẾU VIDEO BUTTON TỒN TẠI VÀ VISIBLE → CLICK NGAY!
    if (videoButton && isVisible && parentVisible) {
      console.log('[Auto Click] ✅ Video button FOUND and VISIBLE → CLICKING!');
      clearInterval(checkInterval);
      showStatusOnPage('✅ Video button found! Clicking...');
      
      // Use human-like click
      humanClick(videoButton);
      showNotification('✅ Clicked Video button!');
      
      // ✅ Reset flag và restart monitoring sau khi click video
      // Đợi lâu hơn để trang load xong countdown và thông báo thành công
      isWaitingForVideo = false;
      isClicking = false;
      showStatusOnPage('✅ Video clicked! Waiting for countdown...');
      
      // ✅ Đợi lâu hơn (5-7s) để đảm bảo countdown đã xuất hiện và ổn định
      setTimeout(() => {
        if (isEnabled) {
          console.log('[Auto Click] 🔄 Restarting monitoring after video click...');
          showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
          // Reset flags để sẵn sàng cho chu trình mới
          isClicking = false;
          isWaitingForVideo = false;
          startMonitoring();
        }
      }, 3000 + Math.random() * 1000); // Đợi 3-4s để trang load xong và countdown xuất hiện (giảm từ 5-7s)
      return;
    }
    
    // ✅ ƯU TIÊN 3: NẾU VIDEO BUTTON TỒN TẠI NHƯNG HIDDEN → THỬ CLICK HOẶC CHỜ
    if (videoButton && (!isVisible || !parentVisible)) {
      // ✅ THỬ CLICK NGAY CẢ KHI HIDDEN (một số site vẫn cho phép click)
      // Chỉ thử nếu button có trong DOM và không có class 'nonec'
      // Case 2: Button có thể nằm trong .w1c/.w1f và vẫn click được
      if (attempts >= 3 && attempts <= 8 && !videoButton.classList.contains('nonec')) {
        const w1cParent = videoButton.closest('.w1c');
        const w1fParent = videoButton.closest('.w1f');
        const hasW1Parent = w1cParent || w1fParent;
        
        console.log('[Auto Click] 🎯 Attempting to click video button (attempts:', attempts, ')');
        console.log('[Auto Click] 🔍 Button in .w1c/.w1f:', hasW1Parent ? 'YES' : 'NO');
        
        try {
          // Thử submit form thay vì click button (nếu button trong form)
          // Case 2: Button nằm trong form với onsubmit="showHideElements('.w1c','.w2c')"
          const videoForm = videoButton.closest('form');
          if (videoForm) {
            console.log('[Auto Click] 🔄 Trying to submit form instead of clicking button...');
            videoForm.submit();
            showNotification('🔄 Submitted video form!');
            clearInterval(checkInterval);
            isWaitingForVideo = false;
            isClicking = false;
            setTimeout(() => {
              if (isEnabled) {
                console.log('[Auto Click] 🔄 Restarting monitoring after form submit...');
                showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
                // Reset flags để sẵn sàng cho chu trình mới
                isClicking = false;
                isWaitingForVideo = false;
                startMonitoring();
              }
            }, 3000 + Math.random() * 1000); // Đợi 3-4s để trang load xong và countdown xuất hiện (giảm từ 5-7s)
            return;
          } else {
            // Nếu không có form, thử click button trực tiếp
            console.log('[Auto Click] 🔄 Trying to click button directly...');
            humanClick(videoButton);
            showNotification('🔄 Clicked video button!');
            clearInterval(checkInterval);
            isWaitingForVideo = false;
            isClicking = false;
            setTimeout(() => {
              if (isEnabled) {
                console.log('[Auto Click] 🔄 Restarting monitoring after button click...');
                showStatusOnPage('✅ Extension ACTIVE - Monitoring countdown...');
                // Reset flags để sẵn sàng cho chu trình mới
                isClicking = false;
                isWaitingForVideo = false;
                startMonitoring();
              }
            }, 3000 + Math.random() * 1000); // Đợi 3-4s để trang load xong và countdown xuất hiện (giảm từ 5-7s)
            return;
          }
        } catch (e) {
          console.log('[Auto Click] ⚠️ Failed to click/submit button:', e);
        }
      }
      
      console.log('[Auto Click] ⏳ Video button exists but HIDDEN - Continue waiting... (attempt:', attempts, ')');
      if (attempts >= maxAttempts) {
        console.log('[Auto Click] ⚠️ Max attempts reached, video button still hidden');
        clearInterval(checkInterval);
        // Retry click search nếu video button không hiện sau nhiều attempts
        if (retryCount < maxRetries) {
          const activeCountdown = getActiveCountdownInfo(form, resultDiv);
          if (activeCountdown) {
            console.log('[Auto Click] ⏳ Countdown still active - stop retry while video hidden. Text:', activeCountdown.text);
            isWaitingForVideo = false;
            isClicking = false;
            showStatusOnPage(`⏳ Countdown active (${formatCountdownInfo(activeCountdown)}) - waiting...`);
            setTimeout(() => {
              if (isEnabled) {
                startMonitoring();
              }
            }, 1500);
            return;
          }
          console.log('[Auto Click] 🔄 Video button hidden too long, retrying search...');
          isClicking = false; // Reset flag trước khi retry
          setTimeout(() => {
            clickSearchButtonWithRetry(retryCount + 1, form, resultDiv);
          }, 2000 + Math.random() * 1000); // Tăng delay để tránh spam
        } else {
          // Reset retry count và tiếp tục
          console.log('[Auto Click] 🔄 Max retries reached, resetting and continuing...');
          isWaitingForVideo = false;
          isClicking = false;
          if (isEnabled) {
            startMonitoring();
          }
        }
      }
      return;
    }
    
    // ✅ ƯU TIÊN 4: NẾU KHÔNG TÌM THẤY VIDEO BUTTON → CHECK ERROR VÀ RETRY
    if (!videoButton) {
      // Check error message - Tìm trong resultDiv hoặc container
      let errorElement = null;
      if (resultDiv) {
        errorElement = resultDiv.querySelector('.error') || 
                       resultDiv.querySelector('span.error') ||
                       resultDiv.querySelector('span.text-danger.error') ||
                       resultDiv.querySelector('span.text-primary.error');
      }
      
      // Nếu không tìm thấy trong resultDiv, tìm trong container
      if (!errorElement && form) {
        const container = form.closest('.card, .container, .col-sm-5, .t-hearts-menu, .t-views-menu');
        if (container) {
          errorElement = container.querySelector('.error') || 
                        container.querySelector('span.error');
        }
      }
      
      const hasError = errorElement && 
                       (errorElement.textContent.includes('error occurred') || 
                        errorElement.textContent.includes('An error occurred') ||
                        errorElement.textContent.includes('Error') ||
                        errorElement.textContent.includes('try again') ||
                        errorElement.textContent.includes('Please try again'));
      
      if (hasError) {
        const errorText = errorElement ? errorElement.textContent.trim() : '';
        console.log('[Auto Click] ⚠️ Error detected:', errorText);
        console.log('[Auto Click] ⚠️ Error detected - Retrying search...');
        clearInterval(checkInterval);
        if (retryCount < maxRetries) {
          // Reset flag trước khi retry
          isClicking = false;
          setTimeout(() => {
            clickSearchButtonWithRetry(retryCount + 1);
          }, 2000 + Math.random() * 1000); // Tăng delay để tránh spam
        } else {
          // Reset retry count và tiếp tục
          console.log('[Auto Click] 🔄 Max retries reached, resetting and continuing...');
          isWaitingForVideo = false;
          isClicking = false;
          if (isEnabled) {
            startMonitoring();
          }
        }
        return;
      }
      
      // Check nếu search button đã re-enabled
      const searchReEnabled = !searchButton.disabled && 
                              (searchButton.classList.contains('disableButton') || 
                               !searchButton.classList.contains('disabled'));
      
      if (searchReEnabled && attempts > 10) { // Đợi ít nhất 5s trước khi retry
        console.log('[Auto Click] 🔄 Search button re-enabled but no video button - Retrying search...');
        clearInterval(checkInterval);
        if (retryCount < maxRetries) {
        const activeCountdown = getActiveCountdownInfo(form, resultDiv);
        if (activeCountdown) {
          console.log('[Auto Click] ⏳ Countdown still active - skip retry when search re-enabled. Text:', activeCountdown.text);
          isWaitingForVideo = false;
          isClicking = false;
          showStatusOnPage(`⏳ Countdown active (${formatCountdownInfo(activeCountdown)}) - waiting...`);
          setTimeout(() => {
            if (isEnabled) {
              startMonitoring();
            }
          }, 1500);
          return;
        }
          // Reset flag trước khi retry
          isClicking = false;
          setTimeout(() => {
            clickSearchButtonWithRetry(retryCount + 1);
          }, 2000 + Math.random() * 1000); // Tăng delay để tránh spam
        } else {
          // Reset retry count và tiếp tục
          console.log('[Auto Click] 🔄 Max retries reached, resetting and continuing...');
          isWaitingForVideo = false;
          isClicking = false;
          if (isEnabled) {
            startMonitoring();
          }
        }
        return;
      }
    }
    
    // Timeout
    if (attempts >= maxAttempts) {
      console.log('[Auto Click] ⚠️ Max attempts reached');
      clearInterval(checkInterval);
      isWaitingForVideo = false;
      isClicking = false;
      if (isEnabled) {
        startMonitoring();
      }
    }
  }, 500); // Check mỗi 500ms
}

function showNotification(message) {
  // Tạo notification đơn giản trên trang
  const notification = document.createElement('div');
  notification.textContent = message;
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: #4CAF50;
    color: white;
    padding: 12px 20px;
    border-radius: 5px;
    z-index: 10000;
    font-size: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    animation: slideIn 0.3s ease;
  `;
  
  document.body.appendChild(notification);
  
  // Tự động xóa sau 3 giây
  setTimeout(() => {
    notification.style.animation = 'slideOut 0.3s ease';
    setTimeout(() => {
      if (notification.parentNode) {
        notification.parentNode.removeChild(notification);
      }
    }, 300);
  }, 3000);
}

// Thêm animation styles nếu chưa có
if (!document.getElementById('auto-click-animations')) {
  const style = document.createElement('style');
  style.id = 'auto-click-animations';
  style.textContent = `
    @keyframes slideIn {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
      from { transform: translateX(0); opacity: 1; }
      to { transform: translateX(100%); opacity: 0; }
    }
  `;
  document.head.appendChild(style);
}
