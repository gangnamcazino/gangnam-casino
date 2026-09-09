@echo off
chcp 65001 > nul
set "PATH=C:\Users\LG\AppData\Local\Programs\Git\cmd;C:\Users\LG\AppData\Local\Microsoft\WinGet\Packages\GitHub.cli_Microsoft.Winget.Source_8wekyb3d8bbwe\bin;%PATH%"

echo ========================================================
echo       강남 카지노 VIP LOUNGE - 깃허브 자동 연동 및 배포
echo ========================================================
echo.

echo [1단계] 깃허브 로그인 상태 확인 중...
gh auth status >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 깃허브 로그인이 필요합니다.
    echo 1. 잠시 후 화면에 8자리 영문/숫자 일회용 코드가 표시됩니다.
    echo 2. 엔터를 누르면 브라우저(github.com/login/device)가 열립니다.
    echo 3. 브라우저 창에 해당 코드를 붙여넣고 승인(Authorize) 버튼을 눌러주세요!
    echo.
    gh auth login --web -h github.com -p https
    if %errorlevel% neq 0 (
        echo 로그인에 실패했습니다. 다시 시도해 주세요.
        pause
        exit /b 1
    )
)

echo.
echo [2단계] Git 자격 증명 동기화 설정 중...
gh auth setup-git

echo.
echo [3단계] 깃허브에 원격 저장소(gangnam-casino) 생성 및 업로드 중...
gh repo create gangnam-casino --public --source=. --remote=origin --push
if %errorlevel% neq 0 (
    echo 이미 저장소가 존재하거나 업로드 중입니다. 푸시를 재시도합니다...
    git push -u origin main
)

echo.
echo [4단계] 무료 웹 배포(GitHub Pages) 활성화 중...
powershell -Command "$body = @{ source = @{ branch = 'main'; path = '/' } } | ConvertTo-Json; gh api -X POST repos/:owner/gangnam-casino/pages --input - <<< $body" >nul 2>&1

echo.
echo ========================================================
echo   모든 깃허브 설정 및 배포 준비가 성공적으로 완료되었습니다!
echo   저장소 주소: https://github.com/
echo ========================================================
echo.
pause
