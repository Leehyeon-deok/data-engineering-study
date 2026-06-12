📚 정보처리기사 핵심 개념 정리 (관계해석 / 암호화 / 테스트 / 네트워크)
1. 관계해석 (Relational Calculus)
관계 데이터의 연산을 계산 수식으로 표현하는 방법
원하는 결과(WHAT)만 정의하는 비절차적 언어
종류:
튜플 관계해석 (Tuple Relational Calculus, TRC)
도메인 관계해석 (Domain Relational Calculus, DRC)
2. 대칭키 암호화 알고리즘 (Symmetric Key Encryption)
🔹 IDEA
데이터 암호화와 복호화에 동일한 키 사용
Lai & Massey가 개발
PES → IPES → IDEA(1991)로 발전한 블록 암호 알고리즘
🔹 SKIPJACK
미국 NSA에서 개발
Clipper 칩에 내장된 블록 암호 알고리즘
음성 데이터 암호화(전화 통신)에 주로 사용
3. 회귀 테스트 (Regression Test)
오류 수정 후 새로운 오류 발생 여부를 확인하는 반복 테스트
목적:
수정된 시스템이 기존 기능에 문제 없는지 검증
새로운 오류(부작용) 방지
특징:
반복 수행
유지보수 단계에서 중요
4. 라우팅 프로토콜 개념
🔹 자율 시스템 (AS, Autonomous System)
라우터로 연결된 하나의 네트워크 집합 (도메인)
🔹 IGP (Interior Gateway Protocol)
같은 AS 내부에서 라우팅
도메인 내부 경로 설정
🔹 EGP (Exterior Gateway Protocol)
다른 AS 간 라우팅
특징:
관리가 느슨함
신뢰도 낮음
속도보다 보안과 정책 제어 중요
🔹 OSPF (Open Shortest Path First)
대규모 네트워크에서 사용
RIP의 단점 개선
특징:
빠른 수렴 속도
상세한 경로 제어 가능
트래픽 감소
🔹 BGP (Border Gateway Protocol)
AS 간 라우팅을 위한 대표적인 EGP 프로토콜
특징:
목적지까지의 전체 경로 정보(Path) 제공
네트워크 도달 가능성 정보 관리
라우팅 루프 방지
정책 기반 라우팅 지원
✅ 한 줄 핵심 요약
관계해석 → 비절차적(WHAT 중심)
IDEA/SKIPJACK → 대칭키 블록 암호
Regression → 수정 후 부작용 검사
IGP/EGP → 내부 vs 외부 라우팅
OSPF/BGP → 대규모 & 인터넷 핵심 프로토콜