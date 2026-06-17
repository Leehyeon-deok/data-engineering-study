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

-> 연산자
ptr->p

는

(*ptr).p

와 같습니다.

시험 포인트 ⭐
dict는 생성 후 리스트가 바뀌어도 자동으로 갱신되지 않는다.
set()은 중복을 제거한다.
& 연산자는 집합의 교집합이다.
변화 요약
단계	dst	s
생성	{1:2, 2:4, 3:6}	{2,4,6}
lst[0]=99	변화 없음	변화 없음
dst[2]=7	{1:2,2:7,3:6}	변화 없음
s.add(99)	변화 없음	{2,4,6,99}
교집합	{2,7,6} ∩ {2,4,6,99}	{2,6} → 길이 = 2

연산자	의미	예시	결과
&	비트 AND / 집합 교집합	5 & 3	1
|	비트 OR / 집합 합집합	5 | 3	7
^	비트 XOR / 집합 대칭차집합	5 ^ 3	6
~	비트 NOT	~5	-6
<<	왼쪽 시프트	5 << 1	10
>>	오른쪽 시프트	5 >> 1	2
and	논리 AND	True and False	False
or	논리 OR	True or False	True
not	논리 NOT	not True	False
1. 집합(Set)에서
a = {1,2,3}
b = {2,3,4}
& : 교집합
a & b
{2, 3}
| : 합집합
a | b
{1,2,3,4}
- : 차집합
a - b
{1}
^ : 대칭차집합

둘 중 한쪽에만 있는 원소

a ^ b
{1,4}
2. 정수(int)에서는 비트 연산

예를 들어

5 = 101
3 = 011
&
5 & 3
101
011
---
001

결과

1
|
101
011
---
111

결과

7
^
101
011
---
110

결과

6
3. 논리 연산자는 and, or

파이썬은 C, Java처럼

a && b
a || b

를 사용하지 않습니다.

파이썬에서는

a and b
a or b
not a

를 사용합니다.

예)

True and False
# False

True or False
# True

not True
# False
4. C / Java와 비교
의미	C / Java	Python
논리 AND	&&	and
논리 OR	`	
논리 NOT	!	not
비트 AND	&	&
비트 OR	|	|
비트 XOR	^	^
비트 NOT	~	~
정처기·코딩테스트 암기 포인트 ⭐
and, or, not → 논리 연산
&, |, ^, ~ → 비트 연산
집합(Set)에서는
& → 교집합
| → 합집합
- → 차집합
^ → 대칭차집합

TCP는 연결을 수립하기 위해 클라이언트가 서버에 SYN 패킷을 보내고 서버는 SYN-ACK 패킷으로 응답한 후 클라이언트가 다시 ACK 패킷을 보내는 3-way-handshake 과정을 거친다.

 

이때 공격자는 클라이언트 역할로 수많은 SYN 패킷을 서버에 전송한 뒤 마지막 ACK를 고의로 보내지 않아 서버가 연결 대기 상태를 계속 유지하게 만든다.

 

이로 인해 서버의 연결 대기 큐가 가득 차면서 정상적인 접속 요청을 처리하지 못하게 되어 서비스 거부 상태가 발생한다.

--SYN Flooding