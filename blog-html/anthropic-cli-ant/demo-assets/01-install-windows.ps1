# Install ant CLI on Windows (amd64) — v1.10.0
$ErrorActionPreference = "Stop"
$Version = "1.10.0"
$InstallDir = Join-Path $PSScriptRoot "..\tools"
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null

$ZipName = "ant_${Version}_windows_amd64.zip"
$ZipPath = Join-Path $InstallDir $ZipName
$Url = "https://github.com/anthropics/anthropic-cli/releases/download/v${Version}/${ZipName}"

Write-Host "Downloading $Url ..."
Invoke-WebRequest -Uri $Url -OutFile $ZipPath
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force

$Ant = Join-Path $InstallDir "ant.exe"
& $Ant --version
Write-Host "Installed: $Ant"
