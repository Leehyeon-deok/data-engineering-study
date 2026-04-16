📘 Information Processing Engineer Practical Cheat Sheet
🔐 1. 접근 통제 (Access Control)
DAC → 사용자 권한
MAC → 시스템 강제
RBAC → 역할 기반
🧪 2. 테스트
✅ 테스트 케이스 구성요소
조건 / 데이터 / 수행 / 예상결과 / 성공기준
✅ 화이트박스 테스트
코드 내부 구조 기반 테스트
📊 커버리지
문장 → 코드 실행
결정 → 결과 T/F
조건 → 조건식 T/F
경로 → 모든 경로
🌐 3. 오류 제어
Hamming → 검출+수정
FEC → 재전송 없이 수정
ARQ → 재전송
Parity → 1비트 검사
CRC → 다항식
🧮 4. 연산자 핵심
✅ C / Java
& → 비트 AND
&& → 논리 AND (단축)
| → 비트 OR
|| → 논리 OR
^ → XOR
⚠️ 핵심
&는 둘 다 실행
&&는 앞 false면 종료
🧾 5. DB 기본
속성 → 열
튜플 → 행
차수 → 열 개수
카디널리티 → 행 개수
스키마 → 구조
인스턴스 → 데이터
📊 6. 관계대수
σ → 행 선택
π → 열 선택
÷ → 모두 만족
🧠 7. 무결성
개체 → PK (NULL X, 중복 X)
참조 → FK 존재
도메인 → 값 범위
🔗 8. 결합도 (Coupling)
내용 > 공통 > 외부 > 제어 > 스탬프 > 자료

👉 낮을수록 좋음

🧩 9. 응집도 (Cohesion)
우연 < 논리 < 시간 < 절차 < 통신 < 순차 < 기능

👉 높을수록 좋음

🎨 10. 디자인 패턴
🟢 생성 패턴
Singleton → 하나
Factory → 생성 위임
Abstract Factory → 묶음
Builder → 단계 생성
Prototype → 복사
🔵 구조 패턴
Adapter → 변환
Decorator → 기능 추가
Facade → 단순화
Composite → 트리
Flyweight → 공유
🟡 행위 패턴
State → 상태 변화
Strategy → 알고리즘 변경
Observer → 알림
Command → 요청 객체화
Mediator → 중재
Memento → 상태 저장
Chain → 책임 전달
🔐 11. 네트워크 공격
Spoofing → 위조
Sniffing → 도청
Smurfing → DDoS
🔢 12. 정렬
삽입 → 끼워넣기
선택 → 최소 선택
버블 → 교환
퀵 → 분할
🐍 13. Python 핵심
enumerate → (인덱스, 값)
💻 14. C / Java 핵심
unsigned → 출력 영향 없음
포인터 +1 → 다음 문자
🚨 15. 시험 핵심 실수
& vs && 혼동
차수 vs 카디널리티
나눗셈 → 모두 만족
출력에 u 붙임
패턴 이름 헷갈림