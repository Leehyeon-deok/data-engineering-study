📌 SQL IN / NOT IN / EXISTS / NOT EXISTS 정리 (SQLD 핵심)
✅ 1. IN
✔ 개념

값이 목록 안에 있으면 TRUE

👉 값 비교 방식

SELECT *
FROM EMP
WHERE DEPTNO IN (10, 20);

✔ DEPTNO가 10 또는 20이면 조회
✔ 단순 조건 비교
✔ 서브쿼리 결과 전체를 비교

✔ 서브쿼리 사용
SELECT *
FROM EMP
WHERE DEPTNO IN (
    SELECT DEPTNO FROM DEPT
);

👉 서브쿼리 결과 목록과 비교

✔ 특징

비교 연산

결과 전체를 확인

데이터가 적을 때 유리

✅ 2. NOT IN
✔ 개념

목록에 없으면 TRUE

SELECT *
FROM EMP
WHERE DEPTNO NOT IN (10, 20);
🔥 시험 핵심 (NULL 문제)

👉 서브쿼리에 NULL이 있으면 결과가 나오지 않는다.

WHERE ID NOT IN (1, 2, NULL);

👉 모든 결과가 FALSE 또는 UNKNOWN → 조회 결과 없음

✔ 이유

SQL 3값 논리 때문

ID != NULL → UNKNOWN
✔ 특징

NULL 포함 시 위험

시험에서 자주 출제

✅ 3. EXISTS
✔ 개념

서브쿼리 결과가 하나라도 존재하면 TRUE

👉 존재 여부 확인

SELECT *
FROM EMP E
WHERE EXISTS (
    SELECT 1
    FROM DEPT D
    WHERE D.DEPTNO = E.DEPTNO
);
✔ 특징

하나라도 찾으면 종료

성능 우수

상관 서브쿼리에서 사용

NULL 영향 없음

✔ SELECT 1 의미

실제 값이 아니라 존재 여부만 확인
→ 어떤 값이든 상관 없음

✅ 4. NOT EXISTS
✔ 개념

서브쿼리 결과가 없으면 TRUE

SELECT *
FROM EMP E
WHERE NOT EXISTS (
    SELECT 1
    FROM DEPT D
    WHERE D.DEPTNO = E.DEPTNO
);
✔ 특징

NULL 영향 없음

실무에서 많이 사용

가장 안전한 방식

✅ 5. IN vs EXISTS 차이
구분	IN	EXISTS
방식	값 비교	존재 확인
처리	전체 결과 비교	찾으면 종료
성능	데이터 많으면 느림	일반적으로 빠름
NULL	영향 있음	영향 없음
✅ 6. NOT IN vs NOT EXISTS 차이 (🔥 중요)
구분	NOT IN	NOT EXISTS
NULL	문제 발생	문제 없음
안정성	낮음	높음
실무	사용 감소	많이 사용
시험	트릭 문제	정답 자주
✅ 7. 언제 무엇을 사용할까?
✔ IN

작은 데이터

단순 조건

✔ EXISTS

대용량

조인 대체

성능 중요

✔ NOT EXISTS

NULL 포함 가능

안정적인 조건

✅ 8. SQLD 시험 핵심 정리

🔥 가장 중요
👉 NOT IN vs NOT EXISTS
👉 NULL 포함 여부

✔ 시험 공식

IN → 값 비교

EXISTS → 존재 확인

NOT IN → NULL 주의

NOT EXISTS → 가장 안전

✅ 9. 한 줄 요약

👉 NULL이 있을 가능성이 있으면 NOT EXISTS를 사용하라.