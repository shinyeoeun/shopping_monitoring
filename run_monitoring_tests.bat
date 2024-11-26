@echo off

:loop
cd /d "C:\Users\shiny\IdeaProjects\jp-e2e-monitoring"
start cmd /k "py.test ./jp_e2e_monitoring --reportportal"
cd /d "C:\Users\shiny\IdeaProjects\kr-e2e-monitoring"
start cmd /k "py.test ./kr_e2e_monitoring --reportportal"

timeout /t 1800 /nobreak > nul
goto :loop
