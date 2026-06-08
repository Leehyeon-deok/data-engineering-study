✅ SQLD 핵심 개념 및 오답 정리
1️⃣ 해시 조인 vs Nested Loop 조인
🔹 해시 조인 (Hash Join)

해시 함수를 사용하여 조인 수행.

CPU 사용량이 비교적 많음.

랜덤 액세스가 거의 발생하지 않음.

주로 대용량 테이블 조인에 유리.

인덱스가 없어도 효율적.

👉 특징

Full Scan 기반

메모리 사용

랜덤 I/O 감소

🔹 Nested Loop 조인 (NL Join)

한 테이블을 기준으로 다른 테이블을 반복 탐색.

랜덤 액세스 발생.

인덱스가 존재할 때 매우 빠름.

👉 SQLD 핵심

랜덤 액세스 = Nested Loop 조인

CPU 많이 사용 = Hash Join

2️⃣ 인라인 뷰 (Inline View)

서브쿼리의 한 종류.

FROM 절에서 사용됨.

인라인 뷰의 컬럼은 메인 쿼리에서 사용 가능.

SELECT A.COL1
FROM (SELECT COL1 FROM TAB) A;


👉 SQLD 핵심

FROM절 서브쿼리 = 인라인 뷰

메인 쿼리에서 컬럼 참조 가능.

3️⃣ Sort Merge Join

두 테이블을 각각 정렬한 후 병합.

정렬 후 Merge 수행.

Merge 단계에서는 Full Scan으로 탐색.

👉 특징

대용량 데이터 처리에 유리

인덱스 없어도 사용 가능

정렬 비용 존재

👉 옵티마이저 선택 상황

기본키-외래키 관계에서

외래키 인덱스가 없으면

Sort Merge Join 선택 가능.

4️⃣ 집계 함수 (Aggregate Function)

집합에 대한 정보를 제공.

주로 숫자형에 사용되지만:

✔ MAX, MIN, COUNT는

숫자

문자

날짜
모두 가능.

예:

SELECT MAX(ENAME) FROM EMP;

5️⃣ 인덱스 컬럼 순서와 Random Access

인덱스 컬럼 순서를 변경해도

테이블 Random Access 횟수는 줄지 않음.

하지만 인덱스 탐색 효율에는 영향.

👉 SQLD 핵심

테이블 접근 횟수는 동일

인덱스 스캔 범위는 달라질 수 있음.

6️⃣ 권한 부여 (GRANT)

일반 사용자도:

✔ WITH GRANT OPTION 권한이 있으면
다른 사용자에게 권한 부여 가능.

👉 시험 핵심

DBA만 가능한 것이 아님.

7️⃣ LAG() 윈도우 함수

이전 행의 값을 가져오는 함수.

LAG(컬럼, n)


👉 n번째 이전 행.

예:

SELECT LAG(SALARY, 1) OVER(ORDER BY SALARY)
FROM EMP;

8️⃣ COUNT(*) vs COUNT(1)

✔ 둘은 동일
✔ NULL 여부 상관없이 모든 행 계산.

9️⃣ IN 연산자 특징

NULL은 비교에서 제외.

중복값 있어도 한 번만 비교.

🔟 반정규화 (Denormalization)

성능 향상을 위해 수행.

🔹 단점

데이터 무결성 영향.

🔹 관계 반정규화

중복 관계 추가는

무결성을 크게 해치지 않으면서

성능 향상 가능.

1️⃣1️⃣ 키(Key) 개념

슈퍼키: 유일성만 만족.

후보키: 유일성 + 최소성.

기본키: 후보키 중 선택.

대체키: 나머지 후보키.

1️⃣2️⃣ CASE 문

조건 분기 처리.

CASE
  WHEN 조건 THEN 값
  ELSE 값
END


👉 ELSE 생략 시 NULL 반환.

1️⃣3️⃣ 실행 계획

동일 SQL이라도 실행 계획은 다를 수 있음.

결과는 동일.

성능은 달라질 수 있음.

1️⃣4️⃣ 데이터 모델링 3요소

Things (엔터티)

Attributes (속성)

Relationships (관계)

1️⃣5️⃣ 데이터 모델링 단계
🔹 개념 → 논리 → 물리

개념: 가장 추상적.

논리: 구조 중심.

물리: 실제 DB 구축.

👉 실제 구축 참고
→ 물리 모델.

1️⃣6️⃣ 외래키 구현

논리 모델의 외래키는
물리 모델에서 반드시 구현되는 것은 아님.

🚀 SQLD 시험 핵심 요약

✔ Hash Join → CPU 사용, 랜덤 액세스 적음
✔ NL Join → 랜덤 액세스
✔ Inline View → 메인 쿼리 참조
✔ MAX, MIN → 문자 가능
✔ COUNT(*) = COUNT(1)
✔ IN → NULL 제외
✔ CASE → ELSE 없으면 NULL
✔ 모델링: 개념 → 논리 → 물리