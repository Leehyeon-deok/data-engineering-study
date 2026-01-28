# C Language – Structure (struct) Complete Summary

## 1. 구조체(struct)란?
- 서로 다른 자료형의 변수들을 하나로 묶는 사용자 정의 자료형
- 관련 있는 데이터를 하나의 논리적 단위로 관리하기 위해 사용

> 배열: 같은 자료형만 저장 가능  
> 구조체: 서로 다른 자료형 저장 가능

---

## 2. 구조체 기본 선언
```c
struct Student {
    int id;
    char name[20];
    float score;
};
사용 시:

struct Student s;
3. 구조체 선언과 동시에 변수 생성
struct Student {
    int id;
    char name[20];
} s1, s2;
4. typedef를 이용한 구조체 (권장 방식)
typedef struct {
    int id;
    char name[20];
    float score;
} Student;
사용:

Student s;
5. 구조체 멤버 접근
(1) 일반 구조체 변수
s.id = 1;
(2) 구조체 포인터
Student *p = &s;
p->id = 2;
. : 구조체 변수

-> : 구조체 포인터

6. 구조체 초기화
(1) 선언과 동시에 초기화
Student s = {1, "Kim", 95.5};
(2) 일부 초기화
Student s = {1, "Lee"};
7. 구조체 배열
Student arr[2] = {
    {1, "Kim", 90.0},
    {2, "Lee", 85.5}
};
접근:

arr[0].score = 100.0;
8. 구조체와 함수
(1) 값에 의한 전달
void print(Student s);
구조체 전체 복사

메모리 비효율

(2) 포인터 전달 (권장)
void print(Student *s);
메모리 효율적

실무 및 시험에서 많이 사용

9. 중첩 구조체
typedef struct {
    int year;
    int month;
    int day;
} Date;

typedef struct {
    char name[20];
    Date birth;
} Person;
접근:

p.birth.year = 2000;
10. 구조체와 포인터
(1) 구조체 포인터 선언
Student *p;
(2) 동적 메모리 할당
Student *s = (Student *)malloc(sizeof(Student));
11. 구조체 크기와 패딩(Padding)
struct Test {
    char a;
    int b;
};
sizeof 결과는 8바이트가 될 수 있음

CPU 접근 속도를 위한 메모리 정렬 때문

자료형 크기 기준으로 패딩 발생

12. 구조체와 공용체(union) 비교
구분	struct	union
메모리	멤버 전체 합	멤버 중 최대
동시 저장	가능	불가능
용도	데이터 묶기	메모리 절약
13. 구조체 사용 시 주의사항
❌ 문자열 직접 대입 불가
s.name = "Kim"; // 오류
⭕

strcpy(s.name, "Kim");
❌ 구조체 전체 비교 불가
if (s1 == s2) // 오류
멤버별 비교 필요

14. 정보처리기사 실기 핵심 포인트
struct와 typedef struct 차이

. 과 -> 연산자

구조체 포인터 전달

구조체 배열 접근

sizeof 구조체 (패딩)

구조체 vs union

15. 핵심 암기 문장
구조체는 서로 다른 자료형의 데이터를 하나의 논리적 단위로 묶어 관리하기 위한 사용자 정의 자료형이다.

16. 핵심 코드 패턴
typedef struct Student {
    int id;
    char name[20];
    float score;
} Student;