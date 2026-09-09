@echo off
chcp 65001 > nul
echo ========================================================
echo   강남 카지노 VIP LOUNGE 로컬 웹 서버 실행
echo ========================================================
echo.
echo 브라우저에서 사이트(http://localhost:3000)를 자동으로 엽니다.
echo 서버를 종료하려면 이 창에서 Ctrl + C 를 누르거나 창을 닫으세요.
echo.
start http://localhost:3000
python -m http.server 3000
