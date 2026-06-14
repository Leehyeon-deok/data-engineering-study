1. 네트워크 공격
공격	핵심
Sniffing	패킷을 엿듣기
Spoofing	신분 위조
Smurfing	Ping(ICMP) 이용 DDoS
암기
Sniffing = 냄새 맡는다 → 몰래 훔쳐본다
Spoofing = 속인다 → 위조
Smurfing = 스머프들이 한꺼번에 공격 → DDoS
시험 포인트

❌ Sniffing = 위조

⭕ Spoofing = 위조

2. Static 변수
지역변수
int f() {
    int x = 1;
}

함수 종료 시 소멸

Static 지역변수
int f() {
    static int x = 1;
    return ++x;
}

실행

f(); // 2
f(); // 3
f(); // 4
이유
일반 변수
생성 → 사용 → 소멸

static 변수
생성 → 계속 유지
암기

Static = 프로그램 종료까지 값 유지

3. Static 멤버 변수
일반 변수
class A{
    int x;
}

객체마다 따로 존재

a.x
b.x
c.x

총 3개

Static 변수
class A{
    static int x;
}

객체가 몇 개여도

a.x ─┐
b.x ─┼─→ x
c.x ─┘

1개만 존재

암기

static = 객체 소속 X → 클래스 소속

4. 데이터 무결성
개체 무결성(Entity Integrity)

PK

조건

NULL 불가
중복 불가
암기

PK = 주민등록번호

참조 무결성(Referential Integrity)

FK

존재하지 않는 부모값 참조 불가

예

학생 테이블

학번 1
학번 2

수강 테이블

학번 3

❌ 불가능

도메인 무결성(Domain Integrity)

컬럼 규칙 준수

예

성별 = 남/여

여기에

ABC

입력

❌

암기
개체 = PK
참조 = FK
도메인 = 형식
5. URL 구조

표준

scheme://authority/path?query#fragment

예

https://www.example.com:8080/product/list?id=100#review

분해

구성요소	값
scheme	https
authority	www.example.com:8080
path	/product/list
query	id=100
fragment	review
암기
S A P Q F

Scheme
Authority
Path
Query
Fragment
의미
요소	설명
Scheme	프로토콜
Authority	호스트, 포트
Path	자원 위치
Query	추가 데이터
Fragment	문서 내부 위치
6. 파이썬 자료형
값	자료형
100	int
100.0	float
'100'	str
[100,200]	list
(100,200)	tuple
{100,200}	set
{'a':100}	dict
암기
[] -> list
() -> tuple
{} -> set
{key:value} -> dict
시험 함정
{}

은 set이 아니다.

{}

= 빈 dict

set()

= 빈 set

7. 오버라이딩 vs 필드 숨김
class Base{
    int x = 100;

    int getX(){
        return x;
    }
}

class Derived extends Base{
    int x = 200;

    int getX(){
        return x;
    }
}
Base a = new Derived();
메서드
a.getX()

결과

200
이유

오버라이딩

실제 객체 기준

Derived

선택

변수
a.x

결과

100
이유

필드 숨김(Field Hiding)

참조변수 기준

Base

선택

암기
메서드 → 객체 기준
변수 → 참조변수 기준

정처기에서 매우 자주 나오는 함정이다.

8. 제네릭 타입 소거(Type Erasure)

컴파일 후

제네릭 정보 제거

기본
class A<T>

↓

class A<Object>
제한
class A<T extends Number>

↓

class A<Number>
class A<T extends Integer>

↓

class A<Integer>
암기
<T>
→ Object

<T extends XXX>
→ XXX
시험 직전 최종 암기
Sniffing = 도청
Spoofing = 위조
Smurfing = ICMP DDoS

static = 값 유지

개체 = PK
참조 = FK
도메인 = 형식

URL
Scheme → Authority → Path → Query → Fragment

[] = list
() = tuple
{} = set
{key:value} = dict

메서드 = 객체 기준
변수 = 참조변수 기준

<T> → Object
<T extends X> → X