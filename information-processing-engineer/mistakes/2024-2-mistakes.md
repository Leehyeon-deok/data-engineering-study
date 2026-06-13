✅ 1. Java 배열 비교 (매우 자주 출제)
구분	설명
a == b	주소(참조) 비교
Arrays.equals(a, b)	1차원 배열 값 비교
Arrays.deepEquals(a, b)	2차원 이상 배열 값 비교
✔ 핵심 암기

배열은 ==로 비교하면 안 되고, 반드시 Arrays.equals() 사용

✅ 2. 대칭키 암호 알고리즘
알고리즘	특징
DES	56비트 키, 64비트 블록
3DES	DES를 3번 반복 적용
AES	128/192/256비트 키, 128비트 블록
SEED	KISA(한국인터넷진흥원) 개발
ARIA	국정원 + 산학연 공동 개발
IDEA	128비트 키
✔ 암기 포인트
DES → 오래된 표준 (짧은 키)
AES → 현재 표준 (가장 중요)
SEED / ARIA → 국내 알고리즘
✅ 3. 패킷 교환 방식
구분	설명
가상회선 방식	연결형 교환 방식 (경로 먼저 설정)
데이터그램 방식	비연결형 교환 방식 (패킷마다 경로 다름)
✔ 핵심
가상회선 = 전화처럼 “경로 고정”
데이터그램 = 택배처럼 “각자 따로 이동”
✅ 4. 라우팅 알고리즘
✔ RIP (Routing Information Protocol)
기준: hop count (라우터 개수)
특징: 단순, 느림

핵심 문장:

“몇 개 라우터 지나가냐”

✔ OSPF (Open Shortest Path First)
기준: 링크 비용 합
특징: 실제 네트워크 환경 반영 (가중치)

핵심 문장:

“비용이 가장 작은 경로”

✅ 5. CPU 스케줄링
✔ SRT (Shortest Remaining Time)
기준: 남은 실행 시간
특징: 선점형

핵심:

남은 시간이 가장 짧은 프로세스 선택

✔ HRN (Highest Response Ratio Next)
공식:
서비스시간
서비스시간+대기시간
	

특징:
오래 기다린 프로세스 우선
SJF 보완형
✔ 핵심 암기

“기다린 시간 + 실행시간 / 실행시간”

IPsec (Internet Protocol Security)
개념
Network Layer(네트워크 계층)에서 동작하는 보안 프로토콜
IP 패킷의 암호화, 인증, 무결성 보장
VPN(Virtual Private Network) 구현에 사용
특징
네트워크 계층(IP 계층)에서 보안 제공
기업의 사설망(VPN) 구축에 활용
IP 패킷 자체를 보호
구성 프로토콜
AH (Authentication Header)
데이터 무결성 제공
송신자 인증 제공
데이터 암호화는 제공하지 않음
ESP (Encapsulating Security Payload)
데이터 암호화 제공
데이터 무결성 제공
송신자 인증 제공
암기
IPsec = VPN + AH + ESP

AH  → 인증(Authentication), 무결성
ESP → 암호화(Encryption), 인증, 무결성
C 언어 - Call by Value (값 전달)
Swap이 실패하는 이유

C는 기본적으로 Call by Value(값 전달) 방식이다.

void swap(int a, int b) {
    int t = a;
    a = b;
    b = t;
}
int a = 10;
int b = 20;

swap(a, b);

함수 호출 시 값이 복사되므로 원본 변수는 변경되지 않는다.

암기
❌ 원본 변경 안 됨
swap(a, b);
✅ 원본 변경 됨
swap(&a, &b);
void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}
핵심
값 전달(Call by Value)
→ 원본 변경 X

주소 전달(Pointer)
→ 원본 변경 O
C 언어 - 구조체 접근 연산자
. (Dot) 연산자

구조체 변수 접근

struct node a;

a.n1;
-> (Arrow) 연산자

구조체 포인터 접근

struct node *p;

p->n1;
의미
p->n1

은

(*p).n1

과 동일하다.

예제
struct node a = {10, NULL};
struct node *p = &a;
a.n1     // 10
p->n1    // 10
(*p).n1  // 10
암기
.   → 구조체 변수 접근
->  → 구조체 포인터 접근

p->n1 = (*p).n1
연결 리스트 예시
head
 ↓
a(10) → b(20) → c(30)
head->n1          // 10
head->n2->n1      // 20
head->n2->n2->n1 // 30