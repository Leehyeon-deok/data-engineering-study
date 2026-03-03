📌 SQLD 핵심 개념 총정리 (시험 대비 Complete Note)
1️⃣ ORDER BY 3
✅ 의미

SELECT 절의 세 번째 컬럼 기준으로 정렬

SELECT empno, ename, sal
FROM emp
ORDER BY 3;

👉 sal ASC 와 동일
👉 방향 미지정 시 기본값은 ASC

2️⃣ SQL은 비절차적 언어 (DML 특징)
✅ 의미

DML은

“무엇을 원하는지”만 작성
“어떻게 가져올지”는 DBMS가 결정

SELECT * FROM emp WHERE deptno = 10;

✔ 조회 방법(인덱스/풀스캔 등)은 옵티마이저가 결정
✔ 절차적 언어(예: C, Java)와 차이점

3️⃣ DECODE
✅ 조건 함수 (Oracle 전용)
DECODE(비교값,
       조건1, 결과1,
       조건2, 결과2,
       기본값)
SELECT ename,
       DECODE(deptno, 10, 'A', 20, 'B', 'C')
FROM emp;

✔ NULL 비교 가능 (시험 함정)

4️⃣ 인덱스 스캔 종류
종류	설명
INDEX UNIQUE SCAN	PK, UNIQUE 조건 → 1건
INDEX RANGE SCAN	범위 조건 (>, <, BETWEEN)
INDEX FULL SCAN	인덱스 전체 읽기
5️⃣ 연산자 우선순위 (시험 중요)

우선순위 순서:

산술연산자
→ 비교연산자
→ IS NULL
→ LIKE / IN / BETWEEN
→ NOT
→ AND
→ OR

예:

WHERE A = 10 OR B = 20 AND C = 30

👉 AND가 OR보다 우선

6️⃣ TO_CHAR vs TO_DATE
함수	역할
TO_DATE	문자 → 날짜
TO_CHAR	날짜/숫자 → 문자
WHERE hiredate >= TO_DATE('20250101','YYYYMMDD');
7️⃣ 조인 방식 비교
조인	특징
NESTED LOOP JOIN	작은 테이블 → 큰 테이블 반복 접근
SORT MERGE JOIN	정렬 후 병합
HASH JOIN	해시 생성 후 조인 (대용량 유리)
8️⃣ 서브쿼리 정리
✅ ORDER BY

서브쿼리에서는 ORDER BY 사용 불가
(단, TOP-N 쿼리 예외)

✅ 컬럼 참조 범위
구분	가능 여부
서브쿼리 → 메인쿼리 컬럼 사용	가능 (연관 서브쿼리)
메인쿼리 → 서브쿼리 컬럼 사용	불가
SELECT *
FROM emp e
WHERE EXISTS (
    SELECT 1
    FROM dept d
    WHERE d.deptno = e.deptno
);

👉 연관(CORRELATED) 서브쿼리

9️⃣ 단일행 vs 다중행 비교
구분	반환 건수	연산자
단일행	1건	=, >, <
다중행	2건 이상	IN, ANY, ALL
🔟 뷰(View)
✅ 특징

편리성

보안성

독립성

CREATE VIEW v_emp AS
SELECT empno, ename FROM emp;

✔ 실제 데이터 저장 X
✔ 논리적 테이블

1️⃣1️⃣ ROWNUM
✅ 특징

조회 순서대로 번호 부여

중간 건너뛰기 불가

WHERE ROWNUM <= 5   -- 가능
WHERE ROWNUM = 5    -- 불가

👉 반드시 < 또는 <=

1️⃣2️⃣ 서브쿼리 종류
종류	설명
CORRELATED	메인쿼리 컬럼 참조
INLINE VIEW	FROM절 서브쿼리
SCALAR	단일값 반환
NESTED	일반 서브쿼리
1️⃣3️⃣ IN vs EXISTS
구분	IN	EXISTS
기준	값 중심	존재 중심
NULL 영향	받음	거의 없음
NOT 사용 시	위험	안전
1️⃣4️⃣ DISTINCT
✅ 의미

중복 제거

SELECT DISTINCT deptno
FROM emp;

✔ 최초 1건만 표시
✔ 모든 SELECT 컬럼 기준으로 중복 판단

🎯 시험에서 자주 나오는 핵심 포인트 요약

ORDER BY 숫자 = SELECT 위치 기준

DML은 비절차적 언어

DECODE는 NULL 비교 가능

NOT IN + NULL = 위험

ROWNUM은 = 비교 불가

연산자 우선순위 AND > OR

서브쿼리 ORDER BY 불가

EXISTS는 존재 중심