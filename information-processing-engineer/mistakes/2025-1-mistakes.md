📘 Information Processing Engineer - Mistakes Note
1. CRC (Cyclic Redundancy Check)
정의
CRC = Cyclic Redundancy Check (순환 중복 검사)
데이터 전송/저장 시 오류를 검출하는 방식
특징
오류 검출용
체크섬 사용
생성 다항식 사용
XOR 기반 나눗셈 수행
나머지를 CRC 값으로 사용
생성 다항식 예
x³ + x + 1
↓
1011
2. Java Exception 정리
예외	의미
ArithmeticException	0으로 나누기
ArrayIndexOutOfBoundsException	배열 범위 초과
NumberFormatException	문자열 → 숫자 변환 실패
NullPointerException	null 객체 사용
ClassCastException	잘못된 형변환
IOException	입출력 오류
FileNotFoundException	파일 없음
3. Java 생성자 실행 순서 (상속)
1. 부모 필드 초기화
2. 부모 생성자
3. 자식 필드 초기화
4. 자식 생성자
핵심
객체 생성 시 부모가 먼저 완성됨
super()가 자동 호출됨
4. Adapter Pattern (어댑터 패턴)
정의
서로 다른 인터페이스를 가진 클래스를 연결하여 함께 사용할 수 있게 하는 구조
특징
기존 클래스(Adaptee)를 수정하지 않음
원하는 인터페이스(Target)에 맞게 변환
Wrapper(감싸는 클래스) 방식
핵심 개념
기존 클래스 → Adapter → 원하는 인터페이스
5. Math 함수
Math.max()
Math.max(a, b)
a와 b 중 더 큰 값 반환
Math.min()
Math.min(a, b)
a와 b 중 더 작은 값 반환

시험 단골
1.
int *p = (int*) malloc(sizeof(int) * 5);

의미

정수 5개 저장 가능한 공간 생성
2.
char *str = (char*) malloc(sizeof(char) * 10);

의미

문자 10개 저장 공간 생성
3.
free(p);

의미

동적 할당 메모리 해제
정처기 실기 암기
malloc()
→ 메모리 할당

free()
→ 메모리 해제

sizeof(자료형)
→ 자료형 크기

int *p
→ 정수형 포인터

int **p
→ 이중 포인터 (2차원 배열 구현에 자주 사용)

키워드	의미
static	클래스 변수, 공유 변수
final	변경 불가
static final	공유 + 변경 불가 (상수)

1. 삼항 연산자 (조건 표현식)
A if 조건 else B
의미
조건이 참이면 A
거짓이면 B
이 문제에서
node.value if level % 2 == 1 else 0
해석
level이 홀수 → node.value
level이 짝수 → 0
일반 if로 풀면
if level % 2 == 1:
    node.value
else:
    0
시험 포인트
한 줄 if = 삼항 연산자
2. sum(generator) 패턴
sum(calc(n, level + 1) for n in node.children)
의미
자식 노드 전부 재귀 호출해서 합
풀어서 쓰면
total = 0
for n in node.children:
    total += calc(n, level + 1)
return total
구조 분석
sum(  [반복식]  )

= 리스트 없이 바로 반복 결과 합산

시험 포인트
for문 + sum 압축 표현
3. for + generator 표현식
(calc(n, level + 1) for n in node.children)
의미
리스트 만들지 않고 하나씩 값 생성
차이
방식	특징
[ ... ]	리스트 생성
( ... )	generator (즉시 계산 안 함)
시험에서는?
거의 항상 sum() 안에 등장
4. 재귀 호출 패턴
calc(n, level + 1)
의미
자식 노드로 내려가면서 level 증가
핵심
트리 문제 = 거의 무조건 DFS 재귀
5. Node 구조 (클래스 핵심)
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
의미
value = 값
children = 자식 리스트
시험 포인트
이 구조 = 트리 기본 템플릿
6. list comprehension (노드 생성)
nodes = [Node(i) for i in li]
의미
li의 값을 Node 객체로 변환
일반 코드
nodes = []
for i in li:
    nodes.append(Node(i))
시험 포인트
for문 압축 버전
7. 핵심 부모 인덱스 공식
(i - 1) // 2
의미
완전 이진트리에서 부모 찾기
구조
parent = (i-1)//2
시험 필수
왼쪽/오른쪽 자동 배치됨 (배열 순서 기반)
8. append 구조
nodes[parent].children.append(nodes[i])
의미
부모 노드의 자식 리스트에 현재 노드 추가
쉽게 말하면
부모 → 자식 연결
9. return 구조 (재귀 핵심)
return A + B

이 문제에서는:

현재 값 + 자식 결과 합
구조
DFS = 현재 + 왼쪽 + 오른쪽