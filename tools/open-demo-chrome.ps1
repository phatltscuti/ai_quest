# Mo Chrome voi profile demo rieng + cong debug 9222 de Playwright ket noi (connect_over_cdp)
$profile = "D:\code\work\ai_quest\.chrome-demo-profile"
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$profile" --window-size=1920,1080 --start-maximized "https://accounts.google.com" "https://notebook.google.com/" "https://aistudio.google.com/api-keys"
