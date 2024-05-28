@echo off
setlocal

rem Prompt the user to enter a line of text
set /p "userInput=Add comments for commit:  "

rem Execute two predefined lines of commands
git add .
git commit -m "%userInput%"
git push -u origin main

endlocal