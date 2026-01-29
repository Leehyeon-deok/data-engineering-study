📘 열거체(enum)와 공용체(union) 정리

(C 언어 / 정보처리기사 실기 대비)

1️⃣ 열거체 (Enumeration, enum)
🔹 개념

열거체(enum)는 관련 있는 상수들을 하나의 집합으로 묶어 이름을 붙인 자료형이다.
정수 상수에 의미 있는 이름을 부여하여 코드의 가독성과 유지보수성을 높인다.

🔹 기본 문법
enum 열거형이름 {
    상수1,
    상수2,
    상수3
};

🔹 예제
enum Day {
    MON, TUE, WED, THU, FRI, SAT, SUN
};


기본적으로 첫 값은 0부터 시작

이후 값은 1씩 증가

상수	값
MON	0
TUE	1
WED	2
🔹 값 직접 지정
enum Status {
    READY = 1,
    RUN = 3,
    STOP = 5
};


값 직접 지정 가능

이후 값은 이전 값 + 1

🔹 enum 변수 선언
enum Day today;
today = MON;


또는 한 줄로:

enum Day today = FRI;

🔹 enum의 특징

내부적으로는 int 타입

같은 enum 타입끼리만 의미적으로 사용 권장

코드 가독성 증가

잘못된 값 사용 방지(논리적)

🔹 typedef와 함께 사용 (실무/시험 둘 다 자주 나옴)
typedef enum {
    RED,
    GREEN,
    BLUE
} Color;

Color c = RED;

🔹 enum 정리 요약

✅ 상수 집합 표현

✅ 내부 타입은 int

✅ 가독성 향상

✅ 상태 값, 메뉴, 요일 등에 사용

2️⃣ 공용체 (Union)
🔹 개념

공용체(union)는 여러 멤버가 하나의 메모리 공간을 공유하는 자료형이다.
즉, 한 번에 하나의 멤버만 의미 있는 값을 가진다.

🔹 기본 문법
union 공용체이름 {
    자료형 멤버1;
    자료형 멤버2;
};

🔹 예제
union Data {
    int i;
    float f;
    char c;
};

🔹 메모리 특징 ⭐

모든 멤버가 같은 주소를 공유

크기 = 가장 큰 멤버의 크기

union Data d;

멤버	크기
int	4
float	4
char	1

➡ sizeof(union Data) = 4바이트

🔹 사용 예제
union Data d;

d.i = 10;
printf("%d\n", d.i);

d.f = 3.14;
printf("%f\n", d.f);


⚠ 이전에 저장한 값은 의미 없어짐

🔹 union의 특징

메모리 절약 가능

동시에 여러 값 저장 ❌

마지막에 저장한 멤버만 유효

저수준 시스템 프로그래밍에서 활용

🔹 구조체 vs 공용체 차이 ⭐⭐⭐ (시험 단골)
구분	struct	union
메모리	멤버별로 따로	모든 멤버 공유
크기	멤버 합 + 패딩	가장 큰 멤버 크기
동시 사용	가능	불가능
목적	데이터 묶음	메모리 절약
3️⃣ typedef와 union 함께 사용
typedef union {
    int i;
    float f;
} Value;

Value v;
v.i = 100;

4️⃣ enum vs union 한눈에 비교
구분	enum	union
성격	상수 집합	메모리 공유
내부 구조	정수 값	하나의 메모리
주 용도	상태, 종류 표현	메모리 절약
크기	int 크기	가장 큰 멤버
5️⃣ 시험(정처기 실기) 핵심 포인트 🔥

✅ enum은 int 기반

✅ enum 값은 자동 증가

✅ union 크기는 가장 큰 멤버

✅ union은 마지막에 저장한 값만 유효

✅ struct와 union 차이 문제 자주 출제

6️⃣ 한 줄 요약 (암기용)

enum: 의미 있는 이름을 가진 정수 상수 집합

union: 여러 변수가 하나의 메모리를 공유하는 자료형