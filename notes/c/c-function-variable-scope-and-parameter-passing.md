
📘 C 언어 핵심 정리 (함수 · 변수 · 전달 방식)
1️⃣ 함수 선언과 정의 순서
🔹 기본 원칙

C 컴파일러는 위 → 아래로 코드를 해석

main()에서 호출하는 함수는
👉 미리 선언되었거나
👉 이미 정의되어 있어야 함

❌ 오류 발생 예시 (선언 없음)
int main() {
    add(3, 4);   // 오류
}

int add(int a, int b) {
    return a + b;
}

✅ 올바른 방법 1: 함수 선언 후 정의
int add(int a, int b);   // 함수 선언

int main() {
    add(3, 4);
}

int add(int a, int b) { // 함수 정의
    return a + b;
}

✅ 올바른 방법 2: 함수 정의를 위에 작성
int add(int a, int b) {
    return a + b;
}

int main() {
    add(3, 4);
}

📌 핵심 정리

함수가 main보다 아래 → 선언 필요

함수가 main보다 위 → 선언 불필요

선언 = 함수 정보만 알려줌

정의 = 실제 코드 구현

2️⃣ 전역 변수 선언 위치와 사용 가능 범위
🔹 핵심 원칙

전역변수도 선언 이전에는 사용할 수 없다

❌ 사용 불가 예시
int main() {
    printf("%d", x);  // 오류
}

int x = 10;

✅ 사용 가능 예시
int x = 10;

int main() {
    printf("%d", x);  // 정상
}

✅ extern 사용
extern int x;

int main() {
    printf("%d", x);
}

int x = 10;

📌 함수 사이에 선언된 전역 변수
void f1() {}

int g = 5;

void f2() {}


f1() → ❌ 사용 불가

f2() → ⭕ 사용 가능

3️⃣ 지역 변수 vs 전역 변수 우선순위
🔹 규칙

같은 이름이면 지역 변수가 항상 우선

예제
int x = 10;

int main() {
    int x = 5;
    printf("%d", x);
}


📌 출력

5

🔹 매개변수도 지역 변수
int x = 100;

void func(int x) {
    printf("%d", x);
}


➡️ 전역 변수는 가려짐 (shadowing)

🔹 블록 스코프
int x = 1;

int main() {
    int x = 2;
    {
        int x = 3;
        printf("%d", x); // 3
    }
    printf("%d", x);     // 2
}

⚠️ 주의

C에서는 전역 변수가 가려지면 접근 방법 없음

:: 연산자 ❌ (C++ 전용)

4️⃣ 함수 호출 방식
1️⃣ 값에 의한 전달 (Call by Value)

값만 복사

원본 변경 ❌

void change(int x) {
    x = 100;
}

int main() {
    int a = 10;
    change(a);
    printf("%d", a);
}


📌 출력: 10

2️⃣ 포인터에 의한 전달 (주소 전달)

주소 전달

원본 변경 ⭕

void change(int *x) {
    *x = 100;
}

int main() {
    int a = 10;
    change(&a);
    printf("%d", a);
}


📌 출력: 100

🔥 핵심 개념

C는 모든 함수 호출이 값 전달
포인터도 주소값을 값으로 전달하는 것

⚠️ 시험 함정
void f(int *p) {
    p = NULL;   // 원본 변경 ❌
}

*p = 0;        // 원본 변경 ⭕