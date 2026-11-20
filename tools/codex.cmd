@echo off
rem Codex CLI wrapper: dùng CODEX_HOME riêng (model provider = Gemini qua bridge local 127.0.0.1:4141)
set "CODEX_HOME=%~dp0codex-home"
set "PATH=C:\Program Files\nodejs;%APPDATA%\npm;%PATH%"
call "%APPDATA%\npm\codex.cmd" %*
