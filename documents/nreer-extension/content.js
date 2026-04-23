// NREER Auto Click Extension
console.log('[NREER Auto Click] Content script loaded');

let isEnabled = false;
let enabledTypes = [];
let videoUrl = '';
let isClicking = false;
let isWaitingForCountdown = false;
let isWaitingForCard = false;
let checkInterval = null;

// Load settings from storage
chrome.storage.sync.get(['isEnabled', 'enabledTypes', 'videoUrl'], (result) => {
  isEnabled = result.isEnabled || false;
  enabledTypes = result.enabledTypes || [];
  videoUrl = result.videoUrl || '';
  console.log('[NREER Auto Click] Loaded settings:', { isEnabled, enabledTypes, videoUrl });
  
  if (isEnabled) {
    startMonitoring();
  }
});

// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'toggle') {
    isEnabled = request.enabled;
    if (isEnabled) {
      startMonitoring();
    } else {
      stopMonitoring();
    }
    sendResponse({ success: true });
  } else if (request.action === 'updateTypes') {
    enabledTypes = request.enabledTypes || [];
    console.log('[NREER Auto Click] Updated enabled types:', enabledTypes);
    sendResponse({ success: true });
  }
  return true;
});

// Listen for storage changes
chrome.storage.onChanged.addListener((changes, areaName) => {
  if (areaName === 'sync') {
    if (changes.isEnabled) {
      isEnabled = changes.isEnabled.newValue;
      if (isEnabled) {
        startMonitoring();
      } else {
        stopMonitoring();
      }
    }
    if (changes.enabledTypes) {
      enabledTypes = changes.enabledTypes.newValue || [];
      console.log('[NREER Auto Click] Enabled types changed:', enabledTypes);
    }
    if (changes.videoUrl) {
      videoUrl = changes.videoUrl.newValue || '';
      console.log('[NREER Auto Click] Video URL changed:', videoUrl);
    }
  }
});

function startMonitoring() {
  if (checkInterval) {
    return;
  }
  
  console.log('[NREER Auto Click] Starting monitoring...');
  checkInterval = setInterval(() => {
    if (!isEnabled || isClicking) {
      return;
    }
    checkAndClick();
  }, 1000);
  
  // Initial check
  setTimeout(checkAndClick, 500);
}

function stopMonitoring() {
  if (checkInterval) {
    clearInterval(checkInterval);
    checkInterval = null;
    console.log('[NREER Auto Click] Stopped monitoring');
  }
}

function checkAndClick() {
  if (!isEnabled) {
    return;
  }

  // Step 0: Check if modal is open and close it (always do this first, even if waiting)
  // Find all modals with ID starting with "bootstrap-show-modal-"
  const allModals = document.querySelectorAll('[id^="bootstrap-show-modal-"]');
  for (let modal of allModals) {
    if (isModalVisible(modal)) {
      const modalId = modal.id || 'unknown';
      console.log('[NREER Auto Click] Found modal', modalId, '- closing...');
      const closed = closeModal(modal, '#' + modalId);
      if (closed) {
        return;
      }
    }
  }

  // Step 0.1: Check if Cloudflare challenge is shown
  if (isCloudflareChallenge()) {
    console.log('[NREER Auto Click] Cloudflare challenge detected');
    handleCloudflareChallenge();
    return;
  }

  // Step 0.2: Check if Security Check (CAPTCHA) page is shown
  const securityCheckTitle = document.querySelector('h4 b');
  if (securityCheckTitle && securityCheckTitle.textContent.includes('Security Check')) {
    console.log('[NREER Auto Click] Security Check page detected');
    handleCaptcha();
    return;
  }

  if (isClicking || isWaitingForCard || enabledTypes.length === 0) {
    return;
  }

  // Step 0.5: Check if countdown is active
  if (isCountdownActive()) {
    console.log('[NREER Auto Click] Countdown is active, waiting...');
    isWaitingForCountdown = true;
    updateCountdownStatus();
    return;
  } else {
    isWaitingForCountdown = false;
  }

  // Step 1: Check if we're on home page and need to click "Use" button
  const homeButton = findHomeButton();
  if (homeButton && homeButton.offsetParent !== null) {
    console.log('[NREER Auto Click] Found home button, clicking...');
    isClicking = true;
    setTimeout(() => {
      humanClick(homeButton);
      isClicking = false;
      showNotification('✅ Clicked "Use" button');
    }, 200);
    return;
  }

  // Step 2: Check if we're on input page and need to fill form and click Search
  const inputForm = document.querySelector('form#form1');
  const searchInput = findSearchInput();
  const searchButton = inputForm ? inputForm.querySelector('button[type="submit"]') : null;
  
  if (inputForm && searchInput && searchButton && searchInput.offsetParent !== null) {
    // Check if input is empty or needs URL
    const currentValue = searchInput.value || '';
    if (!currentValue.trim()) {
      // Try to get URL from storage first, then from page
      const urlToUse = videoUrl || getUrlFromPage() || '';
      if (urlToUse) {
        console.log('[NREER Auto Click] Filling input with URL:', urlToUse);
        isClicking = true;
        setTimeout(() => {
          searchInput.value = urlToUse;
          searchInput.dispatchEvent(new Event('input', { bubbles: true }));
          searchInput.dispatchEvent(new Event('change', { bubbles: true }));
          setTimeout(() => {
            if (searchButton && !searchButton.disabled) {
              humanClick(searchButton);
              showNotification('✅ Clicked Search button');
              // After clicking search, wait for card to appear
              isClicking = false;
              waitForCardAndClick();
            } else {
              isClicking = false;
            }
          }, 500);
        }, 200);
        return;
      } else {
        console.log('[NREER Auto Click] No URL available to fill');
      }
    } else if (searchButton.offsetParent !== null && !searchButton.disabled) {
      // Input already has value, just click search
      console.log('[NREER Auto Click] Input has value, clicking Search...');
      isClicking = true;
      setTimeout(() => {
        humanClick(searchButton);
        showNotification('✅ Clicked Search button');
        isClicking = false;
        // After clicking search, wait for card to appear
        waitForCardAndClick();
      }, 200);
      return;
    }
  }

  // Step 3: Check if we're on result page and need to click buttons with data-type
  const cardBody = document.querySelector('.card-body');
  if (cardBody) {
    // Look for buttons with data-type attribute - prioritize hearts first if both are enabled
    // First pass: look for hearts if enabled
    if (enabledTypes.includes('hearts')) {
      const heartsButton = cardBody.querySelector('button[data-type="hearts"]');
      if (heartsButton && 
          heartsButton.offsetParent !== null && 
          !heartsButton.disabled &&
          !heartsButton.classList.contains('d-none')) {
        console.log('[NREER Auto Click] Found Hearts button (data-type), clicking...');
        isClicking = true;
        setTimeout(() => {
          humanClick(heartsButton);
          showNotification('✅ Clicked Hearts button');
          // After clicking, wait for modal to appear
          setTimeout(() => {
            isClicking = false;
            // Check for modal after a delay
            setTimeout(() => {
              checkAndClick();
            }, 1500);
          }, 1000);
        }, 200);
        return;
      }
    }
    
    // Second pass: look for views if enabled
    if (enabledTypes.includes('views')) {
      const viewsButton = cardBody.querySelector('button[data-type="views"]');
      if (viewsButton && 
          viewsButton.offsetParent !== null && 
          !viewsButton.disabled &&
          !viewsButton.classList.contains('d-none')) {
        console.log('[NREER Auto Click] Found Views button (data-type), clicking...');
        isClicking = true;
        setTimeout(() => {
          humanClick(viewsButton);
          showNotification('✅ Clicked Views button');
          // After clicking, wait for modal to appear
          setTimeout(() => {
            isClicking = false;
            // Check for modal after a delay
            setTimeout(() => {
              checkAndClick();
            }, 1500);
          }, 1000);
        }, 200);
        return;
      }
    }
  }
}

function findHomeButton() {
  const candidateButtons = document.querySelectorAll('button[onclick*="zxndnnndje"]');
  for (let btn of candidateButtons) {
    const onclickAttr = btn.getAttribute('onclick') || '';
    const hasTokFree = /tok_f(ree|ee)/i.test(onclickAttr);
    if (hasTokFree && btn.offsetParent !== null) {
      return btn;
    }
  }
  return null;
}

function isModalVisible(modal) {
  if (!modal) return false;
  const hasShowClass = modal.classList.contains('show');
  const computedStyle = window.getComputedStyle(modal);
  const isDisplayed = computedStyle.display === 'block' || modal.style.display === 'block';
  const isVisible = modal.offsetParent !== null;
  return hasShowClass && (isDisplayed || isVisible);
}

function closeModal(modal, selector = '') {
  if (!modal) return false;

  isClicking = true;

  const closeButton = modal.querySelector('button.close, button[data-dismiss="modal"]');
  if (closeButton) {
    setTimeout(() => {
      humanClick(closeButton);
      showNotification('✅ Closed modal');
      setTimeout(() => {
        isClicking = false;
        waitForCountdown();
      }, 500);
    }, 300);
    return true;
  }

  let closedWithJquery = false;
  if (window.$ && window.$.fn.modal) {
    try {
      window.$(selector || '#bootstrap-show-modal-0').modal('hide');
      showNotification('✅ Closed modal (jQuery)');
      closedWithJquery = true;
    } catch (e) {
      console.log('[NREER Auto Click] Error closing modal with jQuery:', e);
    }
  }

  modal.classList.remove('show');
  const backdrop = document.querySelector('.modal-backdrop');
  if (backdrop) {
    backdrop.remove();
  }
  document.body.classList.remove('modal-open');

  setTimeout(() => {
    isClicking = false;
    waitForCountdown();
  }, 500);

  return true;
}

function waitForCardAndClick() {
  if (!isEnabled || isWaitingForCard) {
    return;
  }

  console.log('[NREER Auto Click] Waiting for card to appear after search...');
  isWaitingForCard = true;
  let attempts = 0;
  const maxAttempts = 30; // Wait up to 30 seconds

  const checkCard = setInterval(() => {
    attempts++;

    const cardBody = document.querySelector('.card-body');
    if (cardBody && cardBody.offsetParent !== null) {
      console.log('[NREER Auto Click] Card appeared! Looking for buttons...');
      clearInterval(checkCard);
      isWaitingForCard = false;

      // Look for buttons with data-type
      // First pass: look for hearts if enabled
      if (enabledTypes.includes('hearts')) {
        const heartsButton = cardBody.querySelector('button[data-type="hearts"]');
        if (heartsButton && 
            heartsButton.offsetParent !== null && 
            !heartsButton.disabled &&
            !heartsButton.classList.contains('d-none')) {
          console.log('[NREER Auto Click] Found Hearts button, clicking...');
          isClicking = true;
          setTimeout(() => {
            humanClick(heartsButton);
            showNotification('✅ Clicked Hearts button');
            setTimeout(() => {
              isClicking = false;
              setTimeout(() => {
                checkAndClick();
              }, 1500);
            }, 1000);
          }, 200);
          return;
        }
      }

      // Second pass: look for views if enabled
      if (enabledTypes.includes('views')) {
        const viewsButton = cardBody.querySelector('button[data-type="views"]');
        if (viewsButton && 
            viewsButton.offsetParent !== null && 
            !viewsButton.disabled &&
            !viewsButton.classList.contains('d-none')) {
          console.log('[NREER Auto Click] Found Views button, clicking...');
          isClicking = true;
          setTimeout(() => {
            humanClick(viewsButton);
            showNotification('✅ Clicked Views button');
            setTimeout(() => {
              isClicking = false;
              setTimeout(() => {
                checkAndClick();
              }, 1500);
            }, 1000);
          }, 200);
          return;
        }
      }

      console.log('[NREER Auto Click] Card found but no enabled button available');
      // If no button clicked, allow checks to continue
      setTimeout(() => {
        checkAndClick();
      }, 1000);
      return;
    }

    if (attempts >= maxAttempts) {
      console.log('[NREER Auto Click] Timeout waiting for card');
      clearInterval(checkCard);
      isWaitingForCard = false;
    }
  }, 1000);
}

function isCountdownActive() {
  const minElement = document.querySelector('#min');
  const secElement = document.querySelector('#sec');
  
  if (minElement && secElement) {
    const minText = minElement.textContent.trim();
    const secText = secElement.textContent.trim();
    const min = parseInt(minText, 10) || 0;
    const sec = parseInt(secText, 10) || 0;
    
    if (min > 0 || sec > 0) {
      return true;
    }
  }
  
  // Also check if countdown container exists
  const countdownContainer = document.querySelector('[data-clock="main_timer"]');
  if (countdownContainer) {
    const timeAttr = countdownContainer.getAttribute('data-time');
    if (timeAttr) {
      const totalSeconds = parseInt(timeAttr, 10) || 0;
      if (totalSeconds > 0) {
        return true;
      }
    }
  }
  
  return false;
}

function waitForCountdown() {
  if (!isEnabled) {
    return;
  }
  
  isWaitingForCountdown = true;
  console.log('[NREER Auto Click] Waiting for countdown to finish...');
  
  const checkCountdown = setInterval(() => {
    if (!isEnabled) {
      clearInterval(checkCountdown);
      isWaitingForCountdown = false;
      return;
    }
    
    if (!isCountdownActive()) {
      console.log('[NREER Auto Click] Countdown finished! Resetting form...');
      clearInterval(checkCountdown);
      isWaitingForCountdown = false;
      
      // Reset form and start again
      setTimeout(() => {
        resetAndRestart();
      }, 1000);
    } else {
      updateCountdownStatus();
    }
  }, 500);
}

function resetAndRestart() {
  console.log('[NREER Auto Click] Resetting and restarting...');
  
  // Clear the input field
  const searchInput = findSearchInput();
  if (searchInput) {
    searchInput.value = '';
    searchInput.dispatchEvent(new Event('input', { bubbles: true }));
    searchInput.dispatchEvent(new Event('change', { bubbles: true }));
  }
  
  // Wait a bit then fill URL and search again
  setTimeout(() => {
    const urlToUse = videoUrl || getUrlFromPage() || '';
    if (urlToUse && searchInput) {
      console.log('[NREER Auto Click] Filling URL again:', urlToUse);
      searchInput.value = urlToUse;
      searchInput.dispatchEvent(new Event('input', { bubbles: true }));
      searchInput.dispatchEvent(new Event('change', { bubbles: true }));
      
      setTimeout(() => {
        const inputForm = document.querySelector('form#form1');
        const searchButton = inputForm ? inputForm.querySelector('button[type="submit"]') : null;
        if (searchButton && !searchButton.disabled) {
          humanClick(searchButton);
          showNotification('🔄 Restarted: Clicked Search again');
        }
      }, 500);
    }
  }, 500);
}

function updateCountdownStatus() {
  const minElement = document.querySelector('#min');
  const secElement = document.querySelector('#sec');
  
  if (minElement && secElement) {
    const min = minElement.textContent.trim();
    const sec = secElement.textContent.trim();
    showStatusOnPage(`⏳ Waiting countdown: ${min}m ${sec}s`);
  } else {
    showStatusOnPage('⏳ Waiting for countdown...');
  }
}

function findSearchInput() {
  const candidates = document.querySelectorAll('input[type="search"], input[enterkeyhint="search"], input.form-control');
  for (let input of candidates) {
    if (input && input.offsetParent !== null) {
      return input;
    }
  }
  return null;
}

function getUrlFromPage() {
  // Try to find URL in various places
  // Check if there's a URL in the page text or data attributes
  const urlPattern = /(https?:\/\/[^\s<>"{}|\\^`\[\]]+)/i;
  const pageText = document.body.innerText || '';
  const match = pageText.match(urlPattern);
  
  if (match) {
    return match[1];
  }
  
  // Check data attributes
  const elementsWithUrl = document.querySelectorAll('[data-url], [href*="http"]');
  for (let el of elementsWithUrl) {
    const url = el.getAttribute('data-url') || el.getAttribute('href');
    if (url && url.startsWith('http')) {
      return url;
    }
  }
  
  return null;
}

function humanClick(element) {
  if (!element) return;
  
  const events = ['mouseover', 'mousedown', 'mouseup', 'click'];
  events.forEach((eventType, index) => {
    setTimeout(() => {
      const event = new MouseEvent(eventType, {
        view: window,
        bubbles: true,
        cancelable: true,
        buttons: 1
      });
      element.dispatchEvent(event);
    }, index * 50);
  });
  
  // Also try direct click
  setTimeout(() => {
    if (element.onclick) {
      try {
        element.onclick();
      } catch (e) {
        console.log('[NREER Auto Click] Error calling onclick:', e);
      }
    }
  }, 250);
}

function showNotification(message) {
  // Create or update notification element
  let notification = document.getElementById('nreer-auto-click-notification');
  if (!notification) {
    notification = document.createElement('div');
    notification.id = 'nreer-auto-click-notification';
    notification.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: #4CAF50;
      color: white;
      padding: 12px 20px;
      border-radius: 5px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.2);
      z-index: 10000;
      font-family: Arial, sans-serif;
      font-size: 14px;
      max-width: 300px;
    `;
    document.body.appendChild(notification);
  }
  
  notification.textContent = message;
  notification.style.display = 'block';
  
  setTimeout(() => {
    notification.style.display = 'none';
  }, 3000);
}

// Show status bar
function showStatusOnPage(message) {
  let statusBar = document.getElementById('nreer-auto-click-status');
  if (!statusBar) {
    statusBar = document.createElement('div');
    statusBar.id = 'nreer-auto-click-status';
    statusBar.style.cssText = `
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      z-index: 10000;
      font-family: Arial, sans-serif;
      font-size: 12px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    `;
    document.body.appendChild(statusBar);
  }
  
  statusBar.textContent = message;
  statusBar.style.display = 'block';
}

// Handle Cloudflare Challenge
let isProcessingCloudflare = false;

function isCloudflareChallenge() {
  // Check for common Cloudflare challenge indicators
  const bodyText = document.body.textContent || '';
  const hasCloudflareText = /just a moment|checking your browser|ddos protection|cloudflare/i.test(bodyText);
  
  // Check for Cloudflare challenge iframe
  const cloudflareIframe = document.querySelector('iframe[src*="challenges.cloudflare.com"], iframe[src*="cloudflare"]');
  
  // Check for reCAPTCHA checkbox
  const recaptchaCheckbox = document.querySelector('.g-recaptcha, [data-sitekey], iframe[src*="recaptcha"]');
  
  // Check for Turnstile challenge
  const turnstileChallenge = document.querySelector('[data-sitekey][class*="cf-turnstile"], .cf-turnstile');
  
  return hasCloudflareText || cloudflareIframe || recaptchaCheckbox || turnstileChallenge;
}

function handleCloudflareChallenge() {
  if (isProcessingCloudflare) {
    return;
  }

  console.log('[NREER Auto Click] Handling Cloudflare challenge...');
  isProcessingCloudflare = true;
  showStatusOnPage('🛡️ Cloudflare challenge detected...');

  // Try to find and click reCAPTCHA checkbox
  const recaptchaCheckbox = document.querySelector('.g-recaptcha, [data-sitekey]');
  if (recaptchaCheckbox) {
    console.log('[NREER Auto Click] Found reCAPTCHA checkbox');
    showStatusOnPage('🛡️ Clicking reCAPTCHA checkbox...');
    
    // Try to find the actual checkbox element inside iframe or click the container
    setTimeout(() => {
      try {
        // Try clicking the container
        humanClick(recaptchaCheckbox);
        showNotification('✅ Clicked reCAPTCHA checkbox');
        
        // Wait for challenge to complete
        waitForCloudflareComplete();
      } catch (e) {
        console.log('[NREER Auto Click] Error clicking reCAPTCHA:', e);
        showStatusOnPage('⚠️ Please complete Cloudflare challenge manually');
        isProcessingCloudflare = false;
      }
    }, 500);
    return;
  }

  // Try to find Turnstile challenge
  const turnstileChallenge = document.querySelector('[data-sitekey][class*="cf-turnstile"], .cf-turnstile');
  if (turnstileChallenge) {
    console.log('[NREER Auto Click] Found Turnstile challenge');
    showStatusOnPage('🛡️ Turnstile challenge detected...');
    
    // Turnstile usually auto-completes, just wait
    waitForCloudflareComplete();
    return;
  }

  // Check if it's a "Just a moment" page - usually auto-completes
  const justAMoment = /just a moment|checking your browser/i.test(document.body.textContent || '');
  if (justAMoment) {
    console.log('[NREER Auto Click] "Just a moment" page detected, waiting...');
    showStatusOnPage('🛡️ Waiting for Cloudflare check...');
    waitForCloudflareComplete();
    return;
  }

  // If we can't auto-handle, show message
  console.log('[NREER Auto Click] Cloudflare challenge detected but cannot auto-handle');
  showStatusOnPage('⚠️ Please complete Cloudflare challenge manually');
  isProcessingCloudflare = false;
}

function waitForCloudflareComplete() {
  let attempts = 0;
  const maxAttempts = 30; // Wait up to 30 seconds
  
  const checkInterval = setInterval(() => {
    attempts++;
    
    // Check if challenge is still present
    if (!isCloudflareChallenge()) {
      console.log('[NREER Auto Click] Cloudflare challenge completed!');
      clearInterval(checkInterval);
      isProcessingCloudflare = false;
      showStatusOnPage('✅ Cloudflare challenge passed');
      showNotification('✅ Cloudflare challenge completed');
      
      // Continue with normal flow after a short delay
      setTimeout(() => {
        checkAndClick();
      }, 1000);
      return;
    }
    
    if (attempts >= maxAttempts) {
      console.log('[NREER Auto Click] Cloudflare challenge timeout');
      clearInterval(checkInterval);
      isProcessingCloudflare = false;
      showStatusOnPage('⚠️ Cloudflare challenge taking too long, please check manually');
    }
  }, 1000);
}

// Handle CAPTCHA
let isProcessingCaptcha = false;
let tesseractLoaded = false;

function handleCaptcha() {
  if (isProcessingCaptcha) {
    return;
  }

  const captchaForm = document.querySelector('form#cat');
  const captchaInput = captchaForm ? captchaForm.querySelector('input[name="captcha"]') : null;
  const captchaButton = captchaForm ? captchaForm.querySelector('button[type="submit"]') : null;
  const captchaImage = document.querySelector('img[src*="captcha.php"]');

  if (!captchaForm || !captchaInput || !captchaButton || !captchaImage) {
    console.log('[NREER Auto Click] CAPTCHA elements not found');
    return;
  }

  // Check if already filled
  if (captchaInput.value && captchaInput.value.trim().length > 0) {
    console.log('[NREER Auto Click] CAPTCHA already filled, submitting...');
    isProcessingCaptcha = true;
    setTimeout(() => {
      humanClick(captchaButton);
      showNotification('✅ Submitting CAPTCHA...');
      isProcessingCaptcha = false;
    }, 500);
    return;
  }

  console.log('[NREER Auto Click] Processing CAPTCHA...');
  isProcessingCaptcha = true;
  showStatusOnPage('🔍 Processing CAPTCHA...');

  // Load Tesseract.js if not loaded
  if (!tesseractLoaded && !window.Tesseract) {
    loadTesseract().then(() => {
      processCaptchaWithOCR(captchaImage, captchaInput, captchaButton);
    }).catch((error) => {
      console.log('[NREER Auto Click] Failed to load Tesseract:', error);
      showStatusOnPage('⚠️ CAPTCHA: Please enter manually');
      isProcessingCaptcha = false;
    });
  } else if (window.Tesseract) {
    processCaptchaWithOCR(captchaImage, captchaInput, captchaButton);
  } else {
    console.log('[NREER Auto Click] Tesseract not available');
    showStatusOnPage('⚠️ CAPTCHA: Please enter manually');
    isProcessingCaptcha = false;
  }
}

function loadTesseract() {
  return new Promise((resolve, reject) => {
    if (window.Tesseract) {
      tesseractLoaded = true;
      resolve();
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@4/dist/tesseract.min.js';
    script.onload = () => {
      tesseractLoaded = true;
      console.log('[NREER Auto Click] Tesseract.js loaded');
      resolve();
    };
    script.onerror = () => {
      reject(new Error('Failed to load Tesseract.js'));
    };
    document.head.appendChild(script);
  });
}

function processCaptchaWithOCR(captchaImage, captchaInput, captchaButton) {
  console.log('[NREER Auto Click] Starting OCR...');
  showStatusOnPage('🔍 Reading CAPTCHA...');

  // Get image source
  const imageSrc = captchaImage.src;
  
  // Use Tesseract to recognize text
  window.Tesseract.recognize(
    imageSrc,
    'eng',
    {
      logger: (m) => {
        if (m.status === 'recognizing text') {
          showStatusOnPage(`🔍 Reading CAPTCHA... ${Math.round(m.progress * 100)}%`);
        }
      }
    }
  ).then(({ data: { text } }) => {
    // Clean the recognized text
    const cleanedText = text.trim().toLowerCase().replace(/[^a-z]/g, '');
    console.log('[NREER Auto Click] OCR result:', cleanedText);

    if (cleanedText && cleanedText.length > 0) {
      // Fill the input
      captchaInput.value = cleanedText;
      captchaInput.dispatchEvent(new Event('input', { bubbles: true }));
      captchaInput.dispatchEvent(new Event('change', { bubbles: true }));

      showStatusOnPage(`✅ CAPTCHA: ${cleanedText}`);
      showNotification(`✅ CAPTCHA recognized: ${cleanedText}`);

      // Submit after a short delay
      setTimeout(() => {
        humanClick(captchaButton);
        showNotification('✅ Submitting CAPTCHA...');
        isProcessingCaptcha = false;
      }, 1000);
    } else {
      console.log('[NREER Auto Click] OCR failed to recognize text');
      showStatusOnPage('⚠️ CAPTCHA: Recognition failed, please enter manually');
      isProcessingCaptcha = false;
    }
  }).catch((error) => {
    console.log('[NREER Auto Click] OCR error:', error);
    showStatusOnPage('⚠️ CAPTCHA: Error, please enter manually');
    isProcessingCaptcha = false;
  });
}

// Update status periodically
setInterval(() => {
  if (!isEnabled) {
    showStatusOnPage('❌ NREER Auto Click: OFF');
    return;
  }
  
  if (enabledTypes.length === 0) {
    showStatusOnPage('⚠️ NREER Auto Click: No types selected');
    return;
  }
  
  if (isProcessingCloudflare) {
    return; // Status is updated in handleCloudflareChallenge
  }
  
  if (isProcessingCaptcha) {
    return; // Status is updated in handleCaptcha
  }
  
  if (isWaitingForCountdown) {
    updateCountdownStatus();
    return;
  }
  
  if (isClicking) {
    showStatusOnPage('🔄 NREER Auto Click: Processing...');
    return;
  }
  
  showStatusOnPage(`✅ NREER Auto Click: ${enabledTypes.join(', ')}`);
}, 1000);

