@echo off
cd C:\Users\shiny\IdeaProjects\jp_api_test
:loop
py.test ./jp_api_test --reportportal
timeout /t 60 /nobreak > nul
goto :loop
