@echo off
chcp 65001 > nul
set "PATH=C:\Users\LG\AppData\Local\Programs\Git\cmd;C:\Users\LG\AppData\Local\Microsoft\WinGet\Packages\GitHub.cli_Microsoft.Winget.Source_8wekyb3d8bbwe\bin;%PATH%"

echo ========================================================
echo       강남 카지노 VIP LOUNGE - 변경 내용 깃허브 반영
echo ========================================================
echo.
echo 변경된 파일들을 확인하고 깃허브에 업로드합니다...
git add .
git commit -m "Update website content"
git push origin main
echo.
echo ========================================================
echo   깃허브에 최신 내용이 성공적으로 반영되었습니다!
echo ========================================================
echo.
pause
