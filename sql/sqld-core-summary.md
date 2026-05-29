SQL 핵심 정리 - UNIQUE KEY 참조 & WHERE절 집계함수
1. UNIQUE KEY도 FOREIGN KEY의 참조 대상 가능
핵심

외래키(Foreign Key)는
반드시 PRIMARY KEY만 참조하는 것이 아니다.

PRIMARY KEY 또는 UNIQUE KEY 를 참조 가능

즉:

참조 대상 컬럼이 유일성(UNIQUE)을 보장하면 된다.
가능 조건

참조되는 컬럼이 아래 중 하나여야 함.

가능 여부	제약조건
가능	PRIMARY KEY
가능	UNIQUE KEY
불가능	일반 컬럼
예시 1 - PRIMARY KEY 참조
CREATE TABLE DEPT (
    DEPTNO NUMBER PRIMARY KEY
);

CREATE TABLE EMP (
    EMPNO NUMBER,
    DEPTNO NUMBER,
    FOREIGN KEY (DEPTNO)
        REFERENCES DEPT(DEPTNO)
);
예시 2 - UNIQUE KEY 참조
CREATE TABLE MEMBER (
    EMAIL VARCHAR2(100) UNIQUE
);

CREATE TABLE LOGIN (
    EMAIL VARCHAR2(100),
    FOREIGN KEY (EMAIL)
        REFERENCES MEMBER(EMAIL)
);

가능한 이유:

EMAIL이 UNIQUE라서 중복되지 않음

즉:

외래키는 “하나의 대상”을 정확히 참조할 수 있어야 한다.

암기 포인트
FOREIGN KEY는
PK 또는 UNIQUE를 참조 가능
핵심은 유일성 보장
2. WHERE절에서 집계함수 사용 불가
핵심
WHERE절에서는 집계함수 사용 불가

집계함수:

SUM()
AVG()
COUNT()
MAX()
MIN()
왜 안 되나?

SQL 실행 순서 때문.

SQL은 보통:

FROM
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY

순서로 실행됨.

즉:

WHERE 실행 시점에는
집계가 아직 안 끝남

그래서:

SELECT *
FROM EMP
WHERE AVG(SAL) > 3000;

❌ 오류 발생

집계함수 조건은 HAVING 사용
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING AVG(SAL) > 3000;

✔ 가능

WHERE vs HAVING 차이
구분	WHERE	HAVING
대상	개별 행	그룹 결과
집계함수 사용	불가능	가능
실행 시점	GROUP BY 이전	GROUP BY 이후
암기법
WHERE = 행 필터
HAVING = 그룹 필터
집계함수는 HAVING
시험 핵심 함정
틀린 문장
WHERE COUNT(*) > 1

❌ 불가능

올바른 문장
HAVING COUNT(*) > 1

✔ 가능