# Demo RAG truyen thong (Quest 5) - chay trong cua so PowerShell HIEN THI de quay video.
# Moi lenh duoc "go" voi hieu ung typewriter roi moi chay. Khong bao gio in API key
# (rag.py tu doc GEMINI_API_KEY tu file .env o thu muc goc repo).
#   powershell -ExecutionPolicy Bypass -File .\run-demo.ps1            # day du
#   powershell -ExecutionPolicy Bypass -File .\run-demo.ps1 -Quick     # chi build + 3 cau hoi

param([switch]$Quick, [int]$Delay = 35)

$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Resolve-Path (Join-Path $Here "..\..\..")
$Py   = Join-Path $Root ".venv\Scripts\python.exe"
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "Traditional RAG baseline - AeroPure AQ-200 (fictional data)"

function Type-Line([string]$Text, [string]$Color = "Yellow") {
    Write-Host -NoNewline "PS> " -ForegroundColor Green
    foreach ($ch in $Text.ToCharArray()) { Write-Host -NoNewline $ch -ForegroundColor $Color; Start-Sleep -Milliseconds $Delay }
    Write-Host ""
    Start-Sleep -Milliseconds 400
}
function Say([string]$Text) { Write-Host ""; Write-Host "# $Text" -ForegroundColor Cyan; Start-Sleep -Milliseconds 900 }
function Run-Rag([string]$ArgsText) {
    Type-Line "python rag.py $ArgsText"
    $argv = @([System.Management.Automation.PSParser]::Tokenize($ArgsText, [ref]$null) | ForEach-Object { $_.Content })
    & $Py (Join-Path $Here "rag\rag.py") @argv
    Start-Sleep -Seconds 2
}

Clear-Host
Say "Quest 5 - Traditional RAG tren cung 4 PDF hu cau (AeroPure AQ-200). API key doc tu .env, khong hien thi."
Set-Location $Here
Type-Line "Get-ChildItem ..\sources\*.pdf | Select-Object Name, Length"
Get-ChildItem ..\sources\*.pdf | Select-Object Name, Length | Format-Table -AutoSize | Out-Host
Start-Sleep -Seconds 2

Say "Buoc 1: extract text -> chunk -> embed (gemini-embedding-2) -> luu index.json"
Set-Location (Join-Path $Here "rag")
Run-Rag "build"

Say "Buoc 2: hoi dap - retrieve top-5 bang cosine, tra loi bang gemini-3.5-flash-lite, co trich nguon [S#]"
Run-Rag "ask `"Which month had the most Wi-Fi/App support tickets, how many, and what was the reason?`""
Run-Rag "ask `"What does error code E03 mean on the AeroPure AQ-200 and how do I fix it?`""
Run-Rag "ask `"What is the price and launch date of the AeroPure AQ-300?`""

if (-not $Quick) {
    Say "Buoc 3: chay toan bo 10 cau hoi danh gia -> eval\rag_answers.json"
    Run-Rag "eval ..\eval\questions.json"
}
Say "Xong. Ket qua: demo-assets\eval\results.md"
