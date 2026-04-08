📚 핵심 IT 개념 정리 (시험 대비)
1️⃣ RAID & ITIL
💾 RAID (Redundant Array of Independent Disks)
여러 개의 디스크에 데이터를 분산 저장하는 기술
일부 중복 저장으로 성능 + 안정성 향상
디스크 어레이(Disk Array)라고도 함
📘 ITIL (Information Technology Infrastructure Library)
IT 서비스 운영 및 관리를 위한 베스트 프랙티스 집합
IT 서비스 관리(ITSM)의 표준 참고 문서
2️⃣ 보안 공격 기법
🎯 스피어 피싱 (Spear Phishing)
특정 대상(Target)을 노린 공격
정상적인 이메일로 위장
지속적으로 접근하여 개인정보 탈취
🎯 APT 공격 (Advanced Persistent Threat)
특정 목표 대상에 대해 장기간 지속 공격
다양한 방법으로 침투
정보 수집 → 취약점 분석 → 공격 수행
3️⃣ 트랜잭션 복구 기법
🔄 REDO
완료된 트랜잭션 재실행
로그에 시작 + 완료 기록 존재
↩️ UNDO
미완료 트랜잭션 취소
시작 기록만 존재 (완료 기록 없음)
4️⃣ 테스트 커버리지
유형	설명
문장	모든 코드 1회 실행
분기	True / False 모두 수행
조건	각 조건 True/False
조건/결정	조건 + 분기
다중조건	모든 조건 조합
경로	모든 실행 경로

👉 강도 순서
문장 < 분기 < 조건 < 조건/결정 < 다중조건 < 경로

5️⃣ C 반복문 핵심
for ( ; x[i]; )

👉 의미

x[i] != '\0' 동안 반복
문자열 끝까지 반복

👉 동일 표현

while (x[i] != '\0')
6️⃣ 해시 함수
임의 길이 입력 → 고정 길이 출력
빠른 검색 가능 (Key → 주소 매핑)
데이터 무결성 검증에 사용
7️⃣ SQL LIKE 와일드카드
🔍 기본
기호	의미
%	0개 이상의 문자
_	정확히 1개의 문자
🔐 ESCAPE
특수문자를 일반 문자로 처리
표현	의미
_	"_" 문자
%	"%" 문자
8️⃣ 네트워크 보안 프로토콜
🔒 IPSec
IP 계층 보안
AH → 인증 / 무결성
ESP → 암호화 / 기밀성
터널링 방식 지원
🔒 SSL / TLS
전송계층과 응용계층 사이
데이터 암호화 + 인증 + 무결성
🔒 S-HTTP
HTTP 기반 보안
메시지 단위 암호화
💳 SET (Secure Electronic Transaction)
Visa, MasterCard 개발
전자결제 보안 프로토콜
특징:
메시지 암호화
이중 전자서명
기밀성 + 무결성 보장
9️⃣ 디자인 패턴 정리 (핵심🔥)
🏗️ 생성 패턴 (Creational)

👉 객체 생성

패턴	핵심
Singleton	하나만 생성
Factory Method	생성 책임 분리
Abstract Factory	관련 객체 묶음
Builder	단계적 생성
Prototype	복제

👉 암기
싱팩앱빌프

🧱 구조 패턴 (Structural)

👉 객체 구조

패턴	핵심
Adapter	인터페이스 변환
Bridge	추상/구현 분리
Composite	트리 구조
Decorator	기능 추가
Facade	단순화
Flyweight	메모리 공유
Proxy	대리 처리

👉 암기
어브컴데퍼플프

🤝 행위 패턴 (Behavioral)

👉 객체 협력

패턴	핵심
Observer	상태 전파
Strategy	알고리즘 교체
Command	요청 캡슐화
Mediator	중재
State	상태 변화
Memento	상태 저장
Iterator	순회
Chain of Responsibility	책임 전달
Template Method	알고리즘 틀
Visitor	기능 확장

👉 핵심 암기
옵스커미 (중요 4개)