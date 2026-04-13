📘 정보처리기사 실기 핵심 정리 (인프라 / 테스트 / 보안 / 자료구조 등)

☁️ 클라우드 서비스 모델

## ☁️ 클라우드 서비스 모델

- IaaS (Infrastructure as a Service)
  👉 서버, 네트워크, 스토리지 같은 인프라 제공

- PaaS (Platform as a Service)
  👉 개발 환경(플랫폼) 제공

- SaaS (Software as a Service)
  👉 소프트웨어를 서비스 형태로 제공

✅ 한줄 정리
👉 IaaS(인프라) / PaaS(개발환경) / SaaS(소프트웨어)

🗄️ SQL 기본

## 🗄️ SQL 기본

INSERT INTO 급여 (부서명, 직책, 급여)
VALUES ('마케팅부', '부장', '100');

## 📊 그래프 이론

- 정점이 n개인 방향 그래프의 최대 간선 수
👉 n(n-1)

(자기 자신 제외하고 모든 방향 연결 가능)

## 📦 자료구조

- Set → ❌ 중복 불가
- List → ⭕ 중복 가능

### pop / remove

- Python List → pop(인덱스) / 마지막 요소 제거
- Python Set → pop() → 랜덤 제거
- Java Stack → pop() → 마지막 제거
- Java List
  - remove(인덱스)
  - remove(값)

✅ 한줄 정리
👉 Set은 중복 불가, List는 중복 가능  
👉 Python set pop은 랜덤  
👉 Java remove는 인덱스/값 구분

## 🧪 테스트 기법

### 블랙박스 테스트 (Black Box Test)
👉 내부 코드 보지 않음
👉 입력/출력만으로 테스트

### 화이트박스 테스트 (White Box Test)
👉 내부 코드 구조 확인하면서 테스트

## 📏 커버리지

### 1. 문장 커버리지 (Statement Coverage)
👉 모든 코드(문장) 최소 1번 실행

### 2. 분기 커버리지 (Branch Coverage)
👉 if / else 모든 경우 실행
👉 true / false 둘 다 확인

### 3. 조건 커버리지 (Condition Coverage)
👉 각 조건의 참/거짓 모두 실행

## 💣 네트워크 공격

- Ping of Death
👉 ICMP 패킷을 비정상적으로 크게 전송
👉 과부하 발생

- Tear Drop
👉 잘못된 Fragment Offset으로 재조합 오류 발생
👉 시스템 다운 유도

## 💾 페이징 기법

### 스레싱 (Thrashing)
👉 페이지 부재가 너무 많이 발생
👉 실제 작업보다 교체 시간이 더 많아짐

### 해결 방법

- 워킹 세트 (Working Set)
  👉 자주 사용하는 페이지를 메모리에 유지

- 페이지 부재 빈도 (PFF)
  👉 페이지 부재율 상/하한 설정해서 조절

## 🔒 const 포인터

- const 자료형 *변수명
- 자료형 const *변수명
👉 값 변경 ❌

- 자료형* const 변수명
👉 주소 변경 ❌

✅ 한줄 정리
👉 앞 const = 값 보호  
👉 뒤 const = 주소 보호

## 🦠 보안

- 랜섬웨어
👉 시스템 접근 제한 후 금전 요구하는 악성코드

## 🔍 정적 테스트

- 인스펙션 (Inspection)
  👉 전문가가 공식적으로 검사

- 워크스루 (Walkthrough)
  👉 사전 검토 후 회의 진행

- 동료 검토 (Peer Review)
  👉 2~3명이 간단히 검토

## 🧪 알파 / 베타 테스트

- 알파 테스트
  👉 개발사 내부 테스트
  👉 출시 전 마지막 점검

- 베타 테스트
  👉 실제 사용자(외부) 테스트
  👉 출시 직전 사용자 검증

✅ 한줄 정리
👉 알파 = 내부 / 베타 = 외부 사용자

- 클라우드: IaaS / PaaS / SaaS
- 그래프: n(n-1)
- 자료구조: Set(중복X), List(중복O)
- 테스트: 블랙(외부), 화이트(내부)
- 커버리지: 문장 / 분기 / 조건
- 공격: Ping of Death / Tear Drop
- 메모리: 스레싱 → 워킹세트, PFF
- const: 값 vs 주소 보호
- 테스트 종류: 정적 / 알파 / 베타