📌 SQLD 핵심 오답 정리 (JOIN, MERGE, ROLLUP, ROWNUM, COUNT)
✅ 1. INSERT 문 핵심 정리
✔ 기본 원칙

INSERT INTO 테이블 VALUES(...)

VALUES에 넣는 값의 개수는 컬럼 개수와 반드시 동일해야 한다.

전체 컬럼 대상이면 컬럼명 생략 가능

일부 컬럼이면 반드시 컬럼명을 명시해야 한다.

✔ 예시
-- 전체 컬럼 (컬럼 3개라면 값도 3개)
INSERT INTO EMP
VALUES (100, 'KIM', 3000);

-- 일부 컬럼
INSERT INTO EMP (EMPNO, ENAME)
VALUES (101, 'LEE');

📌 시험 포인트
👉 VALUES 개수 ≠ 컬럼 개수 → 오류 발생

✅ 2. IN 절과 NULL
✔ 핵심

IN 리스트 안에 NULL이 있어도 조건에 영향을 주지 않는다.

NULL은 비교 연산이 불가능하기 때문.

✔ 예시
SELECT *
FROM EMP
WHERE DEPTNO IN (10, 20, NULL);

👉 실제 의미

WHERE DEPTNO IN (10, 20)

📌 시험 포인트
👉 NULL은 조건에서 없는 것과 같다

✅ 3. MERGE 문 핵심
✔ 특징

INSERT + UPDATE + DELETE를 동시에 수행

MATCHED는 조건 만족 시 동작

✔ 중요 개념

👉 WHEN MATCHED에서 UPDATE 후 DELETE가 나오면
UPDATE 결과 기준으로 DELETE 실행

✔ 예시
MERGE INTO EMP T
USING TEMP S
ON (T.EMPNO = S.EMPNO)
WHEN MATCHED THEN
  UPDATE SET SAL = S.SAL
  DELETE WHERE SAL < 2000;

👉 UPDATE 후 SAL < 2000인 행만 DELETE

📌 시험 포인트
👉 DELETE는 UPDATE 결과 기준

✅ 4. JOIN 종류 핵심 비교
🔷 CROSS JOIN

모든 경우의 수

M x N 발생

✔ 예시
SELECT *
FROM EMP CROSS JOIN DEPT;

👉 EMP 10건, DEPT 4건 → 40건

🔷 NATURAL JOIN

동일한 컬럼명 자동으로 JOIN

ON절 사용 불가

WHERE절은 가능

✔ 특징

기준 컬럼 자동 결정

TBL.COL 형태 사용 불가

✔ 예시
SELECT *
FROM EMP NATURAL JOIN DEPT;

📌 시험 포인트

ON절 ❌

USING도 없음

자동 JOIN

컬럼 별칭 사용 제한

🔷 INNER JOIN (비교용)
SELECT *
FROM EMP E
JOIN DEPT D
ON E.DEPTNO = D.DEPTNO;
✅ 5. COUNT와 GROUP BY
✔ 중요 개념

👉 SELECT 컬럼 + 집계함수는
GROUP BY 없으면 오류

❌ 잘못된 예시
SELECT DEPTNO, COUNT(*)
FROM EMP;

👉 오류 발생

✔ 올바른 예시
SELECT DEPTNO, COUNT(*)
FROM EMP
GROUP BY DEPTNO;

📌 이유
👉 다대1 관계 발생

✔ COUNT(*) + 다른 집계 함수

👉 집계 함수 결과에 또 집계 함수 사용 불가

❌ 예시
SELECT SUM(COUNT(*))
FROM EMP
GROUP BY DEPTNO;

👉 오류 발생

✔ 해결 방법 → OVER절

👉 분석 함수 사용

SELECT DEPTNO,
       COUNT(*) AS CNT,
       SUM(COUNT(*)) OVER()
FROM EMP
GROUP BY DEPTNO;

📌 OVER 의미
👉 전체 결과 중에서 추가 계산

✅ 6. DELETE CASCADE
✔ 특징

행 단위 삭제

🔷 ON DELETE CASCADE

👉 부모 삭제 → 자식도 삭제

🔷 ON DELETE SET NULL

👉 부모 삭제 → 자식 FK NULL

✔ 예시
ALTER TABLE EMP
ADD CONSTRAINT FK_DEPT
FOREIGN KEY (DEPTNO)
REFERENCES DEPT(DEPTNO)
ON DELETE CASCADE;

📌 시험 포인트
👉 DELETE는 항상 행 단위

✅ 7. ROLLUP
✔ 개념

부분 합 + 전체 합

계층적 그룹

✔ 예시 데이터
COL1
A
B
C
C
✔ SQL
SELECT COL1, COUNT(*)
FROM TBL
GROUP BY ROLLUP(COL1);
✔ 결과
COL1	COUNT
A	1
B	1
C	2
NULL	4

👉 마지막 NULL = 전체

✔ GROUP BY ROLLUP(C1, C2)

👉 순서 중요

GROUP BY ROLLUP(A, B);

👉 결과

A, B

A

전체

📌 개념
👉 GROUP BY A,B + GROUP BY A + 전체
👉 UNION ALL과 유사

✅ 8. ROWNUM
✔ 특징

출력 순서대로 부여

조건 FALSE이면 다음 진행 안함

❌ 잘못된 예시
SELECT *
FROM EMP
WHERE ROWNUM = 10;

👉 결과 없음

📌 이유
ROWNUM은 1부터 부여되는데
첫 행에서 10이 아니므로 FALSE → 종료

✔ 올바른 사용
SELECT *
FROM EMP
WHERE ROWNUM <= 10;
✔ 특정 순위 조회
SELECT *
FROM (
  SELECT *
  FROM EMP
  ORDER BY SAL DESC
)
WHERE ROWNUM = 1;

📌 시험 포인트

ROWNUM = N ❌

ROWNUM <= N ⭕

정렬 후 사용해야 의미 있음

🚀 SQLD 시험 핵심 정리 (초압축)

✔ INSERT → 값 개수 = 컬럼 개수
✔ IN → NULL은 무시
✔ MERGE → UPDATE 후 DELETE
✔ CROSS JOIN → M x N
✔ NATURAL JOIN → ON 없음
✔ COUNT + 컬럼 → GROUP BY 필수
✔ 집계함수 안 집계함수 → OVER 사용
✔ DELETE → 행 단위
✔ ROLLUP → 부분합 + 전체
✔ ROWNUM → <=만 가능