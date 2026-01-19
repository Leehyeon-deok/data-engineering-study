# C Language Core Summary  
## Bit Operators & Type Conversion


---

## 1. C 비트 연산자 (Bitwise Operators)

비트 단위로 연산을 수행하는 연산자이며,  
플래그 처리, 마스킹, 성능 최적화에서 자주 사용된다.

 AND (`&`)
두 비트가 모두 1일 때만 1


5 & 3   // 0101 & 0011 = 0001 (1)
OR (|)
비트 중 하나라도 1이면 1


5 | 3   // 0101 | 0011 = 0111 (7)
XOR (^)
두 비트가 다르면 1, 같으면 0


5 ^ 3   // 0101 ^ 0011 = 0110 (6)
NOT (~)
비트를 반전 (1 → 0, 0 → 1)


~5
비트 이동 연산자
Left Shift (<<)
비트를 왼쪽으로 이동 (× 2 효과)


5 << 1   // 1010 (10)
Right Shift (>>)
비트를 오른쪽으로 이동 (÷ 2 효과)

signed 타입에서는 부호 비트 유지 가능

5 >> 1   // 0010 (2)


2. 조건 연산자 (삼항 연산자)

조건 ? 참일 때 값 : 거짓일 때 값;


int max = (a > b) ? a : b;
if문을 간결하게 표현 가능

가독성 유지가 중요

C 언어 형변환 (Type Conversion) 핵심 정리
3. 형변환 종류
① 암시적 형변환 (Implicit Conversion)
컴파일러가 자동 수행

연산, 대입, 비교 시 발생

② 명시적 형변환 (Casting)


(자료형)값
4. 형변환 핵심 규칙 (⭐⭐⭐⭐⭐)
✅ 1️⃣ 형변환은 연산 전에 발생


(double)a / b   // O
a / b            // X (이미 정수 연산 완료)
✅ 2️⃣ 정수 / 정수 = 정수


5 / 2   // 2
소수점 무조건 버림

✅ 3️⃣ 작은 타입은 자동으로 int 승격
char, short → int



char a = 100, b = 30;
a + b   // int 연산
✅ 4️⃣ unsigned가 하나라도 있으면 전부 unsigned


int a = -1;
unsigned int b = 1;

a < b   // false
-1 → 매우 큰 양수로 변환됨

✅ 5️⃣ 대입 형변환은 정보 손실 가능


double d = 3.9;
int i = d;   // 3
반올림 ❌, 버림

5. Overflow / Underflow (⚠️ 중요)


char c = 130;
printf("%d", c);
char (8bit signed): -128 ~ 127

130 → 2진수 10000010

MSB가 부호 비트 → 음수 해석



-126
값이 잘린 것이 아니라 비트 해석이 달라진 것

6. signed vs unsigned


unsigned int x = -1;
비트는 그대로 저장

unsigned로 해석

✔️ 32bit 기준

4294967295

7. sizeof와 형변환

sizeof(3)        // int → 4
sizeof(3.0)      // double → 8
sizeof((float)3) // float → 4
sizeof는 값이 아닌 타입 기준

컴파일 타임에 결정

8. printf 포맷 주의


printf("%d", 3.14);  // ❌
printf("%f", 3.14);  // O
타입 불일치 → 정의되지 않은 동작(UB)

9. 시험 · 실무 암기 포인트
✔️ 형변환은 연산 전에
✔️ 정수 / 정수 = 정수
✔️ 작은 타입은 int
✔️ unsigned가 우선
✔️ 대입 시 소수점 버림
✔️ overflow는 에러가 아니다

10. 실기 단골 예제


int a = -5;
unsigned int b = 3;
printf("%u", a + b);
✔️ 결과 (32bit 기준)

4294967294
