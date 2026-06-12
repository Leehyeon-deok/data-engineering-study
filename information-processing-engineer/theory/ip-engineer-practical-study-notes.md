📘 정보처리기사 실기 핵심 암기 정리
🧠 1. 테스트 / 품질 / 검증
🔹 동치 분할 테스트 (Equivalence Partitioning)

👉 입력 데이터를 유효/무효 영역으로 나눠 대표값만 테스트

🧠 암기:

“비슷한 값은 묶어서 하나만 테스트”

🔹 Cause-Effect Graph (원인-결과 그래프)

👉 입력 조건 → 출력 결과 관계 분석해서 테스트 케이스 설계

🧠 암기:

“원인 보고 결과 만든다”

🔹 알파 / 베타 테스트
🧪 알파 테스트 → 개발자 내부 테스트
🧪 베타 테스트 → 실제 사용자 테스트

🧠 암기:

“알파 = 안에서 / 베타 = 밖에서”

🔹 회귀 테스트 (Regression Test)

👉 수정 후 기존 기능 정상 여부 확인

🧠 암기:

“고친 다음 옛날 기능 다시 검사”

🧠 2. 결합도 / 설계
🔹 내용 결합도 (Content Coupling)

👉 다른 모듈 내부 변수/기능 직접 사용 (최악)

🧠 암기:

“남의 속까지 건드림 = 최악”

🧠 3. DB / SQL
🔹 ALTER TABLE (구조 변경)
ADD → 추가
MODIFY → 수정
RENAME → 이름 변경
DROP → 삭제
🔹 UPDATE (데이터 변경)
UPDATE 테이블
SET 컬럼 = 값
WHERE 조건;

🧠 암기:

“UPDATE = 값 바꿈”

🔹 JOIN

👉 조건은 ON

🧠 암기:

“JOIN은 ON으로 연결”

🔹 π (파이) 연산 (관계대수)

👉 컬럼 선택 + 중복 제거

🧠 암기:

“SELECT + DISTINCT 느낌”

🧠 4. 암호 / 보안
🔹 AES
128bit 블록
128/192/256 키
👉 대칭키 암호
🔹 DES
64bit 블록
56bit 키 (실질)

👉 현재는 취약

🔹 AAA
Authentication → 인증
Authorization → 인가
Accounting → 과금
🔹 TKIP

👉 WEP 대체 보안 프로토콜 (802.11i)

🔹 TrustZone

👉 ARM 하드웨어 보안 기술

🔹 Typosquatting

👉 오타 도메인 등록 공격

🧠 암기:

“typo = 오타 낚시”

🧠 5. 네트워크 / 라우팅
🔹 RIP / OSPF / BGP
RIP → 거리 벡터 (단순)
OSPF → 링크 상태 (내부)
BGP → AS 간 라우팅 (인터넷)

🧠 암기:

“RIP 단순 / OSPF 내부 / BGP 국가간”

🔹 ATM

👉 53바이트 셀 기반 고속 전송

🔹 계층 역할
데이터링크 → 오류/흐름 제어
네트워크 → 최적 경로
표현계층 → 압축/변환
🧠 6. RAID
RAID 0 → 속도 (복구 X)
RAID 1 → 미러링
RAID 5 → 패리티 분산
RAID 6 → 이중 패리티

🧠 암기:

“0빠름 / 1복사 / 5분산 / 6이중”

🧠 7. AI
AI → 전체
ML → 데이터 학습
DL → 신경망

🧠 암기:

“AI > ML > DL”

🧠 8. ISMS / CMMI
🔹 ISMS

👉 정보보호 관리체계

🔹 CMMI

👉 개발 성숙도 모델
(초 → 관 → 정 → 정 → 최)

🧠 암기:

“ISMS = 보안 / CMMI = 개발 성숙도”

🧠 9. 테스트 개념
🔹 알파 vs 베타
알파 = 내부
베타 = 사용자
🔹 회귀 테스트
수정 후 재검증
🧠 10. 스머핑 / 스푸핑 / 스니핑
🔥 초암기 (이거 하나로 끝)

👉 “머-푸-니”

🧨 스머핑 (Smurfing)
👉 “때린다” → DDoS (ICMP 증폭 공격)
🎭 스푸핑 (Spoofing)
👉 “속인다” → IP/ARP 위장
👀 스니핑 (Sniffing)
👉 “훔쳐본다” → 패킷 감청

🧠 한 줄 스토리:

“머(때림) / 푸(속임) / 니(훔침)”

🧠 11. 핵심 SQL / DB 개념
WHERE → 조건
JOIN → ON
UPDATE → 값 변경
ALTER → 구조 변경
🧠 12. 기타 핵심
🔹 static 메서드

👉 객체 없이 클래스명으로 호출

🔹 REDO / UNDO
REDO → 재실행
UNDO → 되돌리기
🔹 OSI 핵심
링크 → 오류
네트워크 → 경로
표현 → 압축