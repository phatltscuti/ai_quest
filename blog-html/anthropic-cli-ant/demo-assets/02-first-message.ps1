# First Messages API call via ant (requires ANTHROPIC_API_KEY or ant auth login)
$ErrorActionPreference = "Stop"
$Ant = Join-Path $PSScriptRoot "..\tools\ant.exe"

if (-not (Test-Path $Ant)) {
    Write-Error "ant.exe not found. Run 01-install-windows.ps1 first."
}

if (-not $env:ANTHROPIC_API_KEY) {
    Write-Warning "ANTHROPIC_API_KEY is not set. Run: ant auth login"
}

& $Ant messages create `
  --model claude-sonnet-4-5-20250929 `
  --max-tokens 128 `
  --message "{role: user, content: 'Summarize what the ant CLI does in one sentence.'}" `
  --transform "content.#(type==`"text`").text" `
  --raw-output
