# C Language – typedef struct Complete Summary

## 1. typedef란?
- 기존 자료형에 새로운 이름(별명)을 부여하는 문법
- 새로운 타입을 생성하는 것이 아님
- 컴파일 타임에 처리됨

```c
typedef int MYINT;
MYINT a = 10;
2. struct 사용 시 불편한 점
struct Student s;
struct Student *p;
struct 키워드를 매번 사용해야 함

코드 길어지고 가독성 저하

3. typedef struct 기본 형태
typedef struct {
    int id;
    char name[20];
} Student;
익명 구조체에 Student라는 자료형 별명 부여

struct 키워드 없이 사용 가능

Student s;
Student *p;
4. struct 태그 + typedef 함께 사용
typedef struct Student {
    int id;
    char name[20];
} Student;
구분	의미
struct Student	구조체 태그
Student	typedef로 만든 자료형
두 이름 모두 사용 가능

5. typedef struct를 사용하는 이유
1) 가독성 향상
Student s;
2) 유지보수 용이
typedef 한 줄 수정으로 전체 반영 가능

3) 포인터 문법 간단
Student *p;
4) 연결 리스트 구현에 필수
typedef struct Node {
    int data;
    struct Node *next;
} Node;
6. 메모리 관점
typedef는 메모리 구조에 영향 없음

typedef 사용 여부와 sizeof 결과는 동일

문법적 편의 기능

7. typedef struct vs #define
구분	typedef	#define
처리 시점	컴파일	전처리
타입 인식	가능	불가능
디버깅	쉬움	어려움
포인터 안정성	높음	낮음
자료형 정의는 typedef 사용 권장

8. 시험 단골 함정
typedef는 새로운 구조체를 만든다 (X)

typedef는 실행 중 적용된다 (X)

typedef를 쓰면 struct 키워드를 못 쓴다 (X)

9. 핵심 암기 문장
typedef struct는 구조체에 별명을 부여하여 struct 키워드를 생략하고 가독성과 유지보수를 향상시키는 문법이다.

10. 핵심 코드 패턴
typedef struct Student {
    int id;
    char name[20];
} Student;