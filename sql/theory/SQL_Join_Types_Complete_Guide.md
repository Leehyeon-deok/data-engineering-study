📚 SQL JOIN 완전 정리
1️⃣ JOIN이란?

두 개 이상의 테이블을 **공통 컬럼(조건)**을 기준으로 연결하여 하나의 결과 집합으로 만드는 것.

SELECT 컬럼
FROM 테이블1
JOIN 테이블2
ON 조인조건;

2️⃣ EQUI JOIN (등가 조인)
✅ 정의

=(같다) 조건을 사용하는 조인

가장 기본적인 조인 방식.

📌 예시 테이블
👨‍🎓 STUDENT
student_id	name	dept_id
1	Kim	10
2	Lee	20
🏫 DEPARTMENT
dept_id	dept_name
10	Computer
20	Math
🔹 SQL
SELECT S.name, D.dept_name
FROM STUDENT S
JOIN DEPARTMENT D
ON S.dept_id = D.dept_id;

🔹 결과
name	dept_name
Kim	Computer
Lee	Math

👉 = 조건이므로 EQUI JOIN

📌 INNER JOIN의 한 종류

3️⃣ NON-EQUI JOIN (비등가 조인)
✅ 정의

= 이 아닌 조건 (>, <, BETWEEN 등)을 사용하는 조인

📌 예시
📊 SCORE_GRADE
min_score	max_score	grade
90	100	A
80	89	B
👨‍🎓 STUDENT_SCORE
name	score
Kim	95
Lee	85
🔹 SQL
SELECT S.name, G.grade
FROM STUDENT_SCORE S
JOIN SCORE_GRADE G
ON S.score BETWEEN G.min_score AND G.max_score;


👉 = 이 아닌 범위 조건
👉 NON-EQUI JOIN

4️⃣ INNER JOIN
✅ 정의

두 테이블에서 조인 조건이 일치하는 행만 반환

가장 많이 쓰는 조인

SELECT *
FROM A
INNER JOIN B
ON A.col = B.col;


✔ INNER는 생략 가능

SELECT *
FROM A
JOIN B
ON A.col = B.col;


📌 EQUI JOIN 대부분이 INNER JOIN이다.

5️⃣ OUTER JOIN
✅ 정의

조건이 일치하지 않는 행도 포함

① LEFT OUTER JOIN

왼쪽 테이블 기준 모두 출력

SELECT *
FROM A
LEFT JOIN B
ON A.col = B.col;


✔ 오른쪽이 없으면 NULL

② RIGHT OUTER JOIN

오른쪽 테이블 기준 모두 출력

SELECT *
FROM A
RIGHT JOIN B
ON A.col = B.col;

③ FULL OUTER JOIN

양쪽 모두 출력

SELECT *
FROM A
FULL JOIN B
ON A.col = B.col;


📌 정처기/SQLD 포인트

구분	매칭 안되면
INNER	제거
LEFT	오른쪽 NULL
RIGHT	왼쪽 NULL
FULL	양쪽 NULL 가능
6️⃣ NATURAL JOIN
✅ 정의

두 테이블에서 같은 이름의 컬럼을 자동으로 조인

ON 절을 쓰지 않음

🔹 SQL
SELECT *
FROM STUDENT
NATURAL JOIN DEPARTMENT;


✔ 같은 이름의 컬럼(dept_id) 자동 연결

⚠ 주의사항

컬럼명이 같으면 자동 조인

의도치 않은 컬럼까지 조인될 위험 있음

실무에서 거의 사용 안함

7️⃣ CROSS JOIN (카테시안 곱)
✅ 정의

조인 조건 없이 모든 경우의 수를 조합

예시

A 테이블 2행
B 테이블 3행

👉 결과 = 2 × 3 = 6행

🔹 SQL
SELECT *
FROM A
CROSS JOIN B;


또는

SELECT *
FROM A, B;


📌 조인 조건이 없으면 카테시안 곱 발생

8️⃣ SELF JOIN
✅ 정의

같은 테이블을 자기 자신과 조인

별칭(alias) 필수

📌 예시
EMPLOYEE
emp_id	name	manager_id
1	Kim	NULL
2	Lee	1
🔹 SQL
SELECT E.name AS employee,
       M.name AS manager
FROM EMPLOYEE E
LEFT JOIN EMPLOYEE M
ON E.manager_id = M.emp_id;


✔ 같은 테이블을 두 번 사용
✔ 별칭 반드시 필요

🔥 JOIN 전체 비교표
종류	조건	특징
EQUI JOIN	=	가장 기본
NON-EQUI JOIN	>, <, BETWEEN	범위 조인
INNER JOIN	일치 행만	기본 조인
LEFT JOIN	왼쪽 기준	NULL 가능
RIGHT JOIN	오른쪽 기준	NULL 가능
FULL JOIN	양쪽 모두	NULL 가능
NATURAL JOIN	같은 컬럼 자동	실무 거의 X
CROSS JOIN	조건 없음	모든 조합
SELF JOIN	자기 자신	별칭 필요
🎯 SQLD 시험 포인트 정리

✔ EQUI JOIN = INNER JOIN의 대표 형태
✔ NON-EQUI JOIN은 범위조건
✔ OUTER JOIN은 NULL 발생
✔ CROSS JOIN은 카테시안 곱
✔ SELF JOIN은 동일 테이블 + 별칭 필수
✔ NATURAL JOIN은 ON 절 없음