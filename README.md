# 강남 카지노 VIP LOUNGE 웹 프로젝트

비개발자 사용자를 위한 로컬 테스트, 이미지 관리, 무료 웹 배포 및 도메인 연결 가이드 문서입니다.

---

## 1. 프로젝트 폴더 구조

```
gangnam-casino/
├── index.html        # 메인 웹페이지 코드 (골드 테마, 반응형, CTA 버튼 포함)
├── run_server.bat    # 마우스 더블 클릭 시 로컬 웹 서버 실행 및 브라우저 열기
├── README.md         # 프로젝트 안내 및 배포 설명서
└── [이미지 파일 8장] # 아래 이미지 목록을 이 폴더 안에 넣어주시면 됩니다.
```

---

## 2. 필요한 이미지 파일 목록 (총 8개)

웹페이지 코드 내에 지정되어 있는 이미지 파일명입니다. 아래 이름과 똑같이 파일명을 지정하여 `gangnam-casino` 폴더 안에 넣어주시면 자동으로 적용됩니다:

1. `1. 딜러_정면_토끼홀복.png` (히어로 메인 비주얼 이미지)
2. `2. 실제카지노칩과 트레이.png` (서비스 프로세스 Step 01)
3. `3. 카지노로비 컨시어지 상담.png` (서비스 프로세스 Step 02)
4. `4. 바카라 진행테이블.png` (서비스 프로세스 Step 03)
5. `5. 카지노 VIP 컨시어지 서비스.png` (서비스 프로세스 Step 04)
6. `6. 데일리이벤트.png` (프로모션 & 이벤트 01)
7. `7. 위클리 이벤트.png` (프로모션 & 이벤트 02)
8. `8. 365일_24시간운영.png` (24/7 서비스 비주얼)

---

## 3. 로컬에서 사이트 확인하는 방법

1. `gangnam-casino` 폴더 안에 있는 `run_server.bat` 파일을 **마우스 더블 클릭**합니다.
2. 검은색 창이 뜨면서 기본 인터넷 브라우저에 `http://localhost:3000` 주소로 사이트가 바로 열립니다.
3. 확인이 끝난 후 검은색 창을 닫으시면 로컬 서버가 종료됩니다.

---

## 4. 전 세계 인터넷에 무료 배포하기 (추천: Cloudflare Pages)

서버 비용 없이 평생 무료이며, SSL 보안 인증서(`https://`)와 초고속 속도를 지원합니다.

### Cloudflare Pages 배포 방법 (마우스 드래그 앤 드롭 방식)
1. **Cloudflare 가입**: [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up) 에서 무료 회원가입을 합니다.
2. 좌측 메뉴에서 **Workers & Pages** 클릭 -> **Create application** (애플리케이션 생성) 클릭.
3. 상단 탭에서 **Pages** 선택 -> **Upload assets** (자산 업로드) 클릭.
4. 프로젝트 이름 입력 (예: `gangnam-casino-vip`).
5. 현재 `gangnam-casino` 폴더(안에 `index.html`과 이미지들이 있는 폴더)를 브라우저 화면의 점선 영역으로 **마우스 드래그 앤 드롭**합니다.
6. **Deploy site** (사이트 배포) 버튼을 클릭하면 10초 만에 `https://gangnam-casino-vip.pages.dev` 형태의 실제 작동하는 보안 웹사이트 주소가 생성됩니다!

---

## 5. 나만의 도메인 연결하기 (예: `gangnam-vip.com`)

1. **도메인 구매**:
   - 가비아(Gabia), 호스팅케이알(Hosting.kr), 또는 Cloudflare Registrar 등에서 원하는 도메인을 구매합니다.
2. **Cloudflare Pages에서 커스텀 도메인 등록**:
   - 배포된 프로젝트 대시보드에서 **Custom domains** (사용자 지정 도메인) 탭 클릭.
   - **Set up a custom domain** 클릭 후 구매한 도메인(예: `vip.mycasino.com` 또는 `mycasino.com`) 입력.
3. **DNS 레코드 설정 (도메인 구입처에서 등록)**:
   - 도메인을 구매한 사이트(가비아 등)의 DNS 관리 메뉴로 이동합니다.
   - 타입: `CNAME`
   - 이름/호스트: `@` 또는 `www`
   - 값/목적지: Cloudflare가 안내해 주는 주소 (예: `gangnam-casino-vip.pages.dev`)
   - 저장 후 약 5~30분 뒤 내 도메인으로 접속하면 사이트가 정상 연결됩니다.

---

## 6. GitHub을 통한 코드 관리 및 배포 (비개발자 맞춤)

### 방법 A: 웹 브라우저에서 바로 올리기 (프로그램 설치 없이 2분 완료)
1. **GitHub 로그인**: [github.com](https://github.com) 에 접속하여 로그인합니다. (계정이 없다면 [Sign up](https://github.com/signup)으로 생성)
2. **새 저장소(Repository) 만들기**:
   - 우측 상단 `+` 버튼 -> **New repository** 클릭.
   - **Repository name**에 `gangnam-casino` 입력.
   - 공개 여부를 **Public**(무료 GitHub Pages 배포 시 필수)으로 선택.
   - 맨 아래 초록색 **Create repository** 버튼 클릭.
3. **코드 업로드**:
   - 화면 중간에 보이는 **"uploading an existing file"** 파란색 링크를 클릭합니다.
   - 내 컴퓨터의 `gangnam-casino` 폴더 안에 있는 파일들(`index.html`, `README.md`, 이미지 파일 8장 등)을 드래그하여 화면 점선 상자에 끌어다 놓습니다.
   - 하단의 초록색 **Commit changes** 버튼을 누르면 업로드 완료!
4. **GitHub Pages로 인터넷 무료 배포 켜기**:
   - 저장소 화면 상단의 **Settings** 메뉴 클릭.
   - 왼쪽 사이드바에서 **Pages** 클릭.
   - **Branch** 설정에서 `None`으로 되어 있는 드롭다운을 `main` (또는 `master`)으로 변경하고 **Save** 클릭.
   - 1~2분 후 상단에 `Your site is live at https://<사용자아이디>.github.io/gangnam-casino/` 주소가 나타나며 인터넷에 즉시 배포됩니다!

### 방법 B: GitHub Desktop 앱으로 관리하기 (클릭으로 자동 동기화)
1. [desktop.github.com](https://desktop.github.com) 에서 **GitHub Desktop** 프로그램을 다운로드하여 설치합니다.
2. GitHub 계정으로 로그인합니다.
3. 상단 메뉴의 **File** -> **Add Local Repository** 클릭 후 `C:\Users\LG\.gemini\antigravity\scratch\gangnam-casino` 폴더를 선택합니다.
4. "This directory does not appear to be a Git repository" 경고가 뜨면 **create a repository** 파란 링크를 누르고 확인을 클릭합니다.
5. 상단의 **Publish repository** 파란 버튼을 누르면 내 GitHub 계정에 저장소가 자동으로 생성되고 코드가 업로드됩니다.

