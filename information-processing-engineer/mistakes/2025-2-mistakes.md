📘 Information Processing Engineer - 핵심 개념 정리
1. Index (인덱스)
데이터베이스에서 검색 속도를 향상시키기 위한 구조
키-값(Key-Value) 쌍으로 구성
테이블 전체를 스캔하지 않고 빠르게 접근 가능
특징
검색 성능 향상 (SELECT 성능 ↑)
추가 저장 공간 필요
INSERT / UPDATE / DELETE 성능은 일부 저하 가능
2. Attribute (속성)
릴레이션(Relation)에서 열(Column)을 의미
데이터 항목의 속성(Attribute) 또는 특성
각 열은 고유한 이름을 가짐
특정 도메인(Domain)에서 정의된 값만 가질 수 있음
예시

학생 릴레이션:

학번
이름
전공

👉 각각이 하나의 Attribute

정리
파일 구조의 Field(필드)에 해당
릴레이션에서 행(Tuple)을 구성하는 요소
3. SSH (Secure Shell)
원격 접속을 위한 보안 통신 프로토콜
Telnet의 보안 취약점을 보완
특징
공개키 기반 인증 방식
데이터 암호화 통신 지원
원격 서버 안전 접속 가능
기본 포트: 22번
주요 용도
서버 원격 관리
안전한 파일 전송 (SCP, SFTP)
4. Java 메서드 바인딩 (Static vs Instance)
구분	결정 기준	특징
일반 메서드 (Instance Method)	실제 객체	오버라이딩(Overriding) 적용 → 런타임 다형성
static 메서드	참조 타입 (클래스 기준)	오버라이딩 X, 숨김(Hiding) 발생
핵심 포인트
new Child()로 생성해도
→ static 메서드는 부모 기준으로 실행됨
Parent p = new Child();
p.staticMethod(); // Parent의 static 실행
instance method는 실제 객체 기준 실행
p.instanceMethod(); // Child가 오버라이딩했으면 Child 실행
5. CPU 스케줄링 - HRN vs RR
🔵 HRN (Highest Response Ratio Next)
비선점 스케줄링
우선순위 계산으로 실행 순서 결정
우선순위 공식
(Response Ratio) = (대기시간 + 서비스 시간) / 서비스 시간
특징
긴 작업 + 오래 기다린 작업 우선 처리
기아 현상 감소
SJF의 단점 보완
🔵 RR (Round Robin)
선점형 스케줄링
각 프로세스에 동일한 시간 할당 (Time Quantum)
특징
공정성 ↑
응답 시간 빠름
Context Switching 발생 많음
동작 방식
준비 큐에서 순서대로 실행
할당 시간 끝나면 다시 큐 뒤로 이동
📌 핵심 비교
항목	HRN	RR
방식	비선점	선점
기준	응답비율	시간 할당
특징	우선순위 계산	시간 분할
목적	효율성	공정성