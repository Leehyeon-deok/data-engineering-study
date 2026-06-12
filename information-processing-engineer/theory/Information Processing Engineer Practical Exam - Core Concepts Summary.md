📚 정보처리기사 실기 핵심 정리 (모의고사 기반)
1️⃣ UWB (Ultra Wide Band, 초광대역)
✔ 개념
중심 주파수의 20% 이상 점유 대역폭
또는 500MHz 이상의 대역폭
GHz 대역을 사용하는 초고속 무선 데이터 전송 기술
✔ 특징
고속 데이터 전송
저전력 소비
위치 추적 정확도 높음
✔ 예시
애플 에어태그, 스마트키 위치 추적
2️⃣ 킬 스위치 (Kill Switch)
✔ 개념
도난/분실 스마트폰을 원격으로 정지시키는 기능
✔ 기능
원격 잠금
데이터 삭제
단말기 무력화
✔ 특징
OS 또는 펌웨어에 내장됨
3️⃣ Verification vs Validation
✔ Verification (검증)
"올바르게 만들고 있는가?"
개발자 관점
명세서 기준 체크
예시
요구사항: 로그인 기능 구현
→ ID/PW 입력 시 로그인 성공 여부 테스트
✔ Validation (확인)
"올바른 것을 만들었는가?"
사용자 관점
실제 요구 충족 여부
예시
사용자: SNS 로그인 원함
→ 기능이 없으면 Validation 실패
4️⃣ C 언어 구조체 & 포인터
✔ 구조체 복사
temp = x[j];          // 구조체 전체 복사
temp = x[j].field;   // 특정 값 복사
x[j] = x[j+1];       // 전체 이동
x[j].field = 10;     // 값만 변경
✔ 포인터 핵심
void func(int *a, int b) {
    *a = 10; // 원본 변경
    b = 20;  // 복사 → 반영 안됨
}
5️⃣ SQL 집계 함수
✔ COUNT
COUNT(*) → NULL 포함
COUNT(컬럼) → NULL 제외
✔ SUM / AVG
NULL 자동 제외
예시
SELECT COUNT(*), COUNT(age), AVG(age)
FROM student;
6️⃣ 문자열 함수
strcat(dest, src);

✔ dest 뒤에 src 붙임 (dest 변경됨)

7️⃣ 추상화 (Abstract)
✔ 개념
구현 없이 구조만 정의
예시
abstract class Animal {
    abstract void sound();
}
8️⃣ 요구사항 수집 기법
기법	설명
델파이	전문가 의견 수렴
롤플레잉	역할극 기반 분석
워크숍	집중 토론
설문조사	간접 수집
9️⃣ GROUP BY
✔ 개념
그룹별 집계
예시
SELECT 부서, 직책, SUM(급여)
FROM 직원
GROUP BY 부서, 직책;
🔟 EAI (Enterprise Application Integration)
✔ 유형
방식	설명
Point-to-Point	1:1 연결
Hub & Spoke	중앙 허브
Message Bus	미들웨어
Hybrid	혼합 방식
1️⃣1️⃣ Scrum
개념	설명
백로그	요구사항 목록
스프린트	2~4주 개발
번다운 차트	작업 진행도
1️⃣2️⃣ 방화벽 (Firewall)
✔ 개념
외부 침입 차단
내부 정보 유출 방지
1️⃣3️⃣ 페이지 교체 알고리즘
알고리즘	설명
LRU	가장 오래 사용 안됨
LFU	사용 횟수 가장 적음
1️⃣4️⃣ 다치 종속 (MVD)
✔ 개념
하나의 속성이 여러 독립 값을 가짐
A →→ B
A →→ C
(B와 C는 독립)
1️⃣5️⃣ 병행 제어
✔ 종류
기법	설명
로킹	동시 접근 제한
낙관적 검증	나중에 검사
타임스탬프	시간 순서
MVCC	다중 버전
2PC	분산 트랜잭션
1️⃣6️⃣ IoT
✔ 핵심 기술
기술	설명
IoT	사물 인터넷
MQTT	경량 메시징
CoAP	REST 기반 통신
1️⃣7️⃣ MAC 방식
방식	설명
CSMA/CD	충돌 감지 (유선)
CSMA/CA	충돌 회피 (무선)
1️⃣8️⃣ 라우팅 알고리즘
✔ 거리 벡터
벨만-포드 사용
이웃에게만 전달
✔ 링크 상태
다익스트라 사용
전체 네트워크 공유
1️⃣9️⃣ 절차형 SQL
종류	설명
프로시저	함수처럼 실행
사용자 정의 함수	값 반환
트리거	자동 실행
2️⃣0️⃣ SOLID
객체지향 설계 원칙
2️⃣1️⃣ 제로데이 공격
✔ 개념
취약점 공개 전 공격
2️⃣2️⃣ 지역성 (Locality)
종류	설명
시간 지역성	최근 데이터 재사용
공간 지역성	근처 데이터 사용
순차 지역성	순서대로 접근
🎯 시험 핵심 요약
Verification = 과정 / Validation = 결과
COUNT(*) vs COUNT(컬럼)
CSMA/CD vs CSMA/CA
LRU vs LFU
거리벡터 vs 링크상태
포인터만 원본 변경 가능
MVD = 독립 다중값