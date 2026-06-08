📚 SQL 집계함수(Aggregate Function) 완전 정리
1️⃣ 집계함수란?

여러 행(Row)을 하나의 결과 값으로 요약하는 함수

즉, 여러 개의 데이터를 계산해서 하나의 값을 반환한다.

대표적인 집계 함수:

함수	의미
COUNT()	행의 개수
SUM()	합계
AVG()	평균
MAX()	최댓값
MIN()	최솟값
2️⃣ 기본 예제 테이블
👇 EMP 테이블
EMPNO	ENAME	SAL	DEPTNO
1001	A	3000	10
1002	B	2500	10
1003	C	4000	20
1004	D	NULL	20
3️⃣ 주요 집계 함수 정리
① COUNT()
✔ 기본 문법
SELECT COUNT(*) FROM EMP;

✔ 의미

전체 행 개수 반환

NULL 포함

✔ 결과
4

✔ COUNT(컬럼명)
SELECT COUNT(SAL) FROM EMP;

✔ 의미

NULL 제외

SAL이 NULL인 행은 제외됨

✔ 결과
3


🔎 D의 SAL이 NULL이므로 제외됨

📌 COUNT 정리
문법	NULL 포함 여부
COUNT(*)	포함
COUNT(컬럼)	제외

⚠ 시험에서 자주 나옴

② SUM()
✔ 문법
SELECT SUM(SAL) FROM EMP;

✔ 의미

NULL 제외 후 합계 계산

✔ 결과
3000 + 2500 + 4000 = 9500

③ AVG()
✔ 문법
SELECT AVG(SAL) FROM EMP;

✔ 의미

NULL 제외 후 평균 계산

✔ 계산
9500 / 3 = 3166.67


⚠ NULL은 계산에서 제외

④ MAX()
SELECT MAX(SAL) FROM EMP;


결과:

4000

⑤ MIN()
SELECT MIN(SAL) FROM EMP;


결과:

2500

4️⃣ GROUP BY와 함께 사용

집계함수는 GROUP BY와 함께 매우 자주 출제됨

✔ 부서별 평균 급여 구하기
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

결과
DEPTNO	AVG(SAL)
10	2750
20	4000

🔎 20번 부서에서 NULL은 제외됨

5️⃣ HAVING 절

그룹에 조건을 줄 때 사용

✔ 평균 급여가 3000 이상인 부서
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING AVG(SAL) >= 3000;

실행 순서
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY


⚠ WHERE에는 집계함수 사용 불가
⚠ HAVING에서 집계조건 사용

6️⃣ DISTINCT와 함께 사용
SELECT COUNT(DISTINCT DEPTNO)
FROM EMP;


→ 서로 다른 부서 개수

7️⃣ 집계함수 특징 정리
✔ 1. NULL은 대부분 제외된다

COUNT(컬럼)

SUM

AVG

MAX

MIN

✔ 2. WHERE에서는 집계함수 사용 불가

❌

SELECT *
FROM EMP
WHERE AVG(SAL) > 3000;


⭕ HAVING 사용해야 함

✔ 3. GROUP BY를 쓰면 SELECT에 일반 컬럼은 반드시 GROUP BY에 포함

❌

SELECT ENAME, AVG(SAL)
FROM EMP;


⭕ 수정

SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

8️⃣ 시험에 잘 나오는 함정
🔥 ① COUNT(*) vs COUNT(컬럼)

NULL 포함 여부 구분 문제 자주 나옴

🔥 ② GROUP BY 없이 일반 컬럼 사용

에러 발생

🔥 ③ WHERE와 HAVING 구분
구분	사용 시점	집계함수 사용
WHERE	그룹 전	불가능
HAVING	그룹 후	가능