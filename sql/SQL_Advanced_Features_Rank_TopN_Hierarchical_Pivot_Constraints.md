📚 SQL 고급 문법 완전 정리
1️⃣ 순위 함수 (Ranking Functions)

행에 순위를 부여하는 윈도우 함수

✔ 종류
함수	특징
RANK()	공동 순위 허용, 다음 순위 건너뜀
DENSE_RANK()	공동 순위 허용, 건너뛰지 않음
ROW_NUMBER()	무조건 고유 순위
예제 테이블
ENAME	SAL
A	3000
B	4000
C	4000
D	2000
① RANK()
SELECT ENAME, SAL,
       RANK() OVER (ORDER BY SAL DESC) AS RNK
FROM EMP;

ENAME	SAL	RNK
B	4000	1
C	4000	1
A	3000	3
D	2000	4

🔎 2등 없음 (건너뜀)

② DENSE_RANK()
ENAME	SAL	RNK
B	4000	1
C	4000	1
A	3000	2
D	2000	3

🔎 순위 안 건너뜀

③ ROW_NUMBER()
ENAME	SAL	RNK
B	4000	1
C	4000	2
A	3000	3
D	2000	4

🔎 무조건 고유값

📌 시험 포인트

OVER() 반드시 사용

PARTITION BY → 그룹 내 순위

ORDER BY 필수

2️⃣ 비율 관련 함수
① RATIO_TO_REPORT()

전체 합 대비 비율

SELECT ENAME,
       SAL,
       RATIO_TO_REPORT(SAL) OVER() AS RATIO
FROM EMP;


→ SAL / 전체 SAL 합

② PERCENT_RANK()

백분율 순위

공식:

(현재순위 - 1) / (전체행 - 1)

③ CUME_DIST()

누적 분포 비율

📌 시험 포인트

모두 윈도우 함수

OVER() 필수

비율 계산 문제 자주 출제

3️⃣ TOP-N 쿼리

상위 N개 데이터 조회

✔ Oracle (전통 방식)
SELECT *
FROM (
    SELECT *
    FROM EMP
    ORDER BY SAL DESC
)
WHERE ROWNUM <= 3;

✔ ROW_NUMBER() 방식 (권장)
SELECT *
FROM (
    SELECT ENAME, SAL,
           ROW_NUMBER() OVER (ORDER BY SAL DESC) RN
    FROM EMP
)
WHERE RN <= 3;

📌 시험 함정

❌ 잘못된 방식

SELECT *
FROM EMP
WHERE ROWNUM <= 3
ORDER BY SAL DESC;


→ 정렬 전에 ROWNUM 적용됨 ❌

4️⃣ 계층형 질의 (Hierarchical Query)

트리 구조 데이터 조회

예: 조직도

기본 구조
SELECT *
FROM EMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

핵심 키워드
키워드	의미
START WITH	시작 노드
CONNECT BY	부모-자식 관계
PRIOR	부모 참조
LEVEL	계층 깊이
예시
SELECT LEVEL, ENAME
FROM EMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

📌 시험 포인트

PRIOR 위치 바뀌면 방향 바뀜

LEVEL 자주 출제

Oracle 전용

5️⃣ PIVOT

행 → 열 변환

예제 테이블
DEPTNO	JOB	SAL
10	CLERK	1000
10	MANAGER	2000
20	CLERK	1500
PIVOT 문
SELECT *
FROM (
    SELECT DEPTNO, JOB, SAL
    FROM EMP
)
PIVOT (
    SUM(SAL)
    FOR JOB IN ('CLERK', 'MANAGER')
);

결과
DEPTNO	CLERK	MANAGER
10	1000	2000
20	1500	NULL
6️⃣ UNPIVOT

열 → 행 변환

SELECT *
FROM EMP_PIVOT
UNPIVOT (
    SAL FOR JOB IN (CLERK, MANAGER)
);

📌 시험 포인트

PIVOT = 행→열

UNPIVOT = 열→행

집계 함수 반드시 사용

7️⃣ 제약 조건 (Constraint)

데이터 무결성 보장

종류
제약조건	의미
NOT NULL	NULL 불가
UNIQUE	중복 불가
PRIMARY KEY	NOT NULL + UNIQUE
FOREIGN KEY	참조 무결성
CHECK	조건 제한
DEFAULT	기본값
예제
CREATE TABLE EMP (
    EMPNO NUMBER PRIMARY KEY,
    ENAME VARCHAR2(20) NOT NULL,
    SAL NUMBER CHECK (SAL > 0),
    DEPTNO NUMBER,
    CONSTRAINT FK_DEPT
        FOREIGN KEY (DEPTNO)
        REFERENCES DEPT(DEPTNO)
);

📌 시험 포인트

PK = 자동 UNIQUE + NOT NULL

FK는 부모 테이블 먼저 존재해야 함

CHECK는 조건 제한

DEFAULT는 값 자동 입력

🔥 시험 핵심 요약
구분	핵심
순위함수	RANK 차이 구분
비율함수	OVER 필수
TOP-N	정렬 후 제한
계층형	START WITH + CONNECT BY
PIVOT	행→열
UNPIVOT	열→행
제약조건	PK = NOT NULL + UNIQUE
🚀 한 줄 총정리

고급 SQL은 윈도우 함수, 계층형 질의, PIVOT 변환, 제약 조건 이해가 핵심이며 SQLD 및 정처기 실기에서 자주 출제된다.