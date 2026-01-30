🔀 C 언어 qsort()와 비교 함수(compare) 완전 정리
1️⃣ qsort()란?

C 표준 라이브러리 <stdlib.h>에 포함된 범용 정렬 함수

임의의 자료형을 정렬할 수 있도록 비교 함수를 사용

void qsort(
    void* base,       // 배열의 시작 주소
    size_t nmemb,     // 요소 개수
    size_t size,      // 요소 하나의 크기
    int (*compar)(const void*, const void*)
);

2️⃣ compare 함수의 역할

두 요소의 대소 관계만 판단

실제 정렬 알고리즘은 qsort 내부에서 처리

int compare(const void* a, const void* b);

📌 반환값 규칙 (매우 중요)
반환값	의미
음수 (< 0)	a가 b보다 앞에 위치
0	a와 b는 동일
양수 (> 0)	a가 b보다 뒤에 위치

📌 값의 크기 자체가 아니라 부호만 사용

3️⃣ return (*p1 - *p2)가 오름차순인 이유
int compare(const void* a, const void* b) {
    int* p1 = (int*)a;
    int* p2 = (int*)b;
    return (*p1 - *p2);
}

🔍 동작 원리

*p1 < *p2 → 음수 → p1이 앞 → 작은 값이 앞

*p1 == *p2 → 0 → 순서 유지

*p1 > *p2 → 양수 → p1이 뒤 → 큰 값이 뒤

👉 작은 값 → 큰 값 순서 = 오름차순

4️⃣ 내림차순 정렬 방법
return (*p2 - *p1);


비교 순서를 반대로 하여

큰 값이 앞에 오도록 배치

5️⃣ ⚠️ (*p1 - *p2) 사용 시 주의점
📌 문제점

정수 범위가 클 경우 오버플로우 발생 가능

📌 안전한 비교 함수 (권장)
int compare(const void* a, const void* b) {
    int p1 = *(int*)a;
    int p2 = *(int*)b;

    if (p1 < p2) return -1;
    if (p1 > p2) return 1;
    return 0;
}


📌 시험/실무에서 가장 안전한 형태

6️⃣ qsort() 사용 예제 (정수 배열)
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int arr[] = {5, 2, 9, 1, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    qsort(arr, n, sizeof(int), compare);

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

7️⃣ 문자열 정렬 예제
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
    return strcmp(*(char**)a, *(char**)b);
}

int main() {
    char* arr[] = {"banana", "apple", "cherry"};
    int n = 3;

    qsort(arr, n, sizeof(char*), compare);

    for (int i = 0; i < n; i++) {
        printf("%s\n", arr[i]);
    }
}

8️⃣ 구조체 정렬 예제
typedef struct {
    int id;
    int score;
} Student;

int compare(const void* a, const void* b) {
    Student* s1 = (Student*)a;
    Student* s2 = (Student*)b;
    return s1->score - s2->score; // 점수 오름차순
}

9️⃣ 시험에 자주 나오는 핵심 포인트

qsort는 비교 함수의 반환값 부호만 사용

음수 → 앞, 양수 → 뒤

compare 함수는 대소 관계 판단만 담당

내부 정렬 방식은 구현 의존

🔟 한 줄 요약 (암기용)

qsort는 값 비교가 아니라 “누가 앞에 올지”를 return 부호로 결정한다