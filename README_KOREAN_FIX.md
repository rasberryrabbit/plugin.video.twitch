# Twitch (Korean Fix) - Kodi Addon

OAuth 로그인 문제를 해결한 Twitch 애드온 수정 버전입니다. 원본 [anxdpanic/plugin.video.twitch](https://github.com/anxdpanic/plugin.video.twitch) v3.0.3을 기반으로 합니다.

## 주요 변경 사항

### 추가된 기능
1. **수동 OAuth 토큰 입력** - Twitch 웹사이트에서 추출한 auth-token을 직접 입력
2. **토큰 추출 도우미** - 단계별 안내와 함께 토큰 입력 대화상자 제공
3. **수동 토큰 적용 버튼** - 입력한 토큰을 즉시 적용하고 검증
4. **Twitch 공식 웹 Client ID 자동 사용** - `kimne78kx3ncx6brgo4mv6wki5h1ko` (기본 ON)
5. **한국어 설정 메뉴** - 모든 새 기능에 한국어 strings 추가

### 해결된 문제
- OAuth URL 만료 문제 ("Gone" 에러)
- 디바이스 로그인 실패 시 대체 인증 방법 부재
- Client ID 입력 필드가 Developer 탭에 숨겨진 문제

## 설치 방법

### 1단계: 사전 준비
- Kodi 19 (Matrix) 이상
- 기존 Twitch 애드온 제거 (선택사항이나 권장)
- `script.module.python.twitch` 모듈 필요 (의존성 자동 설치됨)

### 2단계: ZIP 파일 설치
1. `plugin.video.twitch-3.0.4-korean-fix.1.zip` 파일을 다운로드
2. Kodi → Add-ons → 박스 아이콘 (열린 상자)
3. **Install from zip file**
4. 다운로드한 zip 파일 선택
5. "Twitch add-on installed" 메시지 대기

### 3단계: Twitch auth-token 추출
1. PC 브라우저에서 https://twitch.tv 로그인
2. **F12** 키 눌러 개발자 도구 열기
3. **Console(콘솔)** 탭 클릭
4. 다음 코드 붙여넣고 Enter:
   ```javascript
   document.cookie.split("; ").find(item=>item.startsWith("auth-token="))?.split("=")[1]
   ```
5. 출력된 **30자리 문자열** 복사

### 4단계: 토큰 입력
1. Kodi → Add-ons → Twitch → 설정 (톱니바퀴 아이콘)
2. **수동 로그인 (한국 수정)** 탭 클릭
3. **수동 OAuth Token** 필드에 복사한 토큰 붙여넣기
4. **수동 토큰 적용** 버튼 클릭
5. "토큰이 유효합니다! 사용자: xxx" 메시지 확인

### 5단계: 시청
이제 Add-ons → Twitch에서 스트림 시청 가능

## 문제 해결

### 토큰 추출 도우미 사용
1. Twitch 애드온 설정 → 수동 로그인 탭
2. **토큰 추출 도우미** 버튼 클릭
3. 단계별 안내 확인 후 토큰 입력

### 토큰이 만료된 경우 (60일 후)
Twitch 토큰은 60일마다 만료됩니다. 같은 방법으로 새 토큰을 추출해서 다시 입력하세요.

### "토큰 검증 실패" 메시지가 뜨는 경우
- 토큰이 정확히 30자리인지 확인
- 앞뒤 공백 제거
- Twitch 계정이 정상적으로 로그인되어 있는지 확인
- 브라우저에서 다시 로그인 후 새 토큰 추출

### Client ID를 본인 앱으로 사용하고 싶은 경우
1. https://dev.twitch.tv/console 에서 앱 등록
2. Client ID 발급
3. Twitch 애드온 설정 → 수동 로그인 → OAuth Client ID 필드에 입력
4. "Twitch 공식 웹 Client ID 사용" 옵션 OFF

## 기존 기능 (원본 그대로)
- 디바이스 코드 로그인 (OAuth 2.0 Device Code Grant Flow)
- 자동 백그라운드 토큰 갱신
- 터보/구독자용 두 번째 디바이스 로그인 (광고 제거)
- 웹사이트 (GQL) 검색 백엔드
- HEVC 코덱 지원 (1440p Enhanced Broadcasting)
- InputStream Adaptive 통합

## 호환성
- Kodi 19 (Matrix), 20 (Nexus), 21 (Omega)
- CoreELEC, LibreELEC, Android, Windows, Linux, macOS
- 1GB RAM 환경에서 작동 확인

## 라이선스
GPL-3.0-only (원본과 동일)

## 원본 프로젝트
- 저장소: https://github.com/anxdpanic/plugin.video.twitch
- 원작자: anxdpanic, A Talented Community

## 수정 정보
- 수정 버전: 3.0.4-korean-fix.1
- 수정일: 2026-10-21
- 수정 내용: 수동 토큰 입력 기능, 토큰 도우미, 한국어 strings 추가
