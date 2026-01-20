# C Control Flow Statements Summary


---

## 1. switch 문

### 기본 동작
- `switch` 문에서 **특정 case에 break가 없으면**
  → break를 만날 때까지 **아래 case 문들이 모두 실행됨**
  (fall-through 현상)

### default 문
- `default`는 **생략 가능**
- 어떤 case에도 해당하지 않을 때 실행됨

### switch 조건식 제한
- `switch()` 괄호 안에는 **정수식만 사용 가능**
- 사용 가능: `int`, `char`, 정수 상수
- 사용 불가: `float`, `double`, 문자열

---

## 2. 무한 루프 (Infinite Loop)

### 대표적인 형태
```c
for (;;)
while (1)
조건식이 항상 참이므로 break를 통해서만 탈출 가능

서버 대기 루프, 이벤트 처리 등에 사용

3. do-while 문
구조

do {
    // 실행할 문장
} while (조건식);
특징
조건 검사 전에 문장을 먼저 실행

조건이 거짓이더라도 최소 1회는 반드시 실행됨

4. for / while / do-while 차이점
실행 순서 비교
for / while

조건식 → 참일 때만 실행

do-while

문장 실행 → 조건식 검사

5. continue 문
기본 개념
반복문 안에서 continue를 만나면
→ 현재 반복을 중단하고 다음 반복으로 이동

반복문별 동작 차이
for 문

증감식 실행 → 조건식 검사

while 문

조건식 검사 → 반복

do-while 문

do-while 끝의 조건식 검사 → 반복

6. goto 문
개념
프로그램 실행 중 제어 흐름을 특정 위치로 이동

사용 조건
이동 대상은 반드시 레이블(label) 이어야 함

레이블은 미리 정의되어 있어야 함

레이블 뒤에는 콜론(:) 사용

예시
c
코드 복사
goto LABEL;

LABEL:
    printf("이동 완료");
⚠️ 가독성과 유지보수 문제로 사용은 최소화 권장

7. return 문
기능
함수 실행을 즉시 종료

호출한 위치로 제어 반환

main 함수에서 return
main() 함수에서 return을 만나면
→ 프로그램 전체가 종료됨

return 0;   // 정상 종료


for,while과 do while 차이 --- for while은 조건식을 먼저 검사해서 조건식이 참인 경우에만 문장 수행 그러나 do while은 일단 먼저 문장을 수행후 조건식을 검사한다.

continue -- 반복문 안에서 continue를 만나면 루프의 시작 부분으로 이동해서 조건문 검사부터 다시 계속한다
	for은 증감식 수행후 다시 조건식부터 검사 
	while은 조건식을 검사하고 루프 반복 
	do while은 do while의 끝 부분에 있는 조건식을 검사하고 루프 반복 

goto -  프로그램 수행중제어의 흐름을 프로그램의 특정 위치로 이동하려면 goto문을 사용한다 사용시 먼저 이동할 문장을 가리키는 레이블이 필요하다 레이블이 먼저 준비된 경우에만 goto 문을 이용해서 이동할수있다. 레이블을 구별하기 위해 콜론(:)이 필요하다 

return - 프로그램 수행 중에 return문을 만나면 함수를 호출한 곳으로 되돌아간다. 만일 main함수 안에서 return문을 만나면 main함수를 리턴하므로 프로그램이 종료된다.
