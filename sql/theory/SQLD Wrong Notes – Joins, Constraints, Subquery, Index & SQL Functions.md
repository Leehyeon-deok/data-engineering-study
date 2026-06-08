📌 SQLD Wrong Notes – Joins, Constraints, Subquery, Index & SQL Functions

SQLD 모의고사에서 틀리기 쉬운 개념들을 예제와 함께 정리하였다.

1️⃣ 비식별자 관계와 조인
✔ 핵심

비식별자 관계라고 해서 조인이 줄어드는 것은 아니다.

비식별자 관계 : 부모 PK가 자식 PK에 포함되지 않음

하지만 데이터 조회 시 여전히 JOIN이 필요하다

예시
CUSTOMER
---------
CUST_ID (PK)
NAME

ORDER
---------
ORDER_ID (PK)
CUST_ID (FK)

조회

SELECT C.NAME, O.ORDER_ID
FROM CUSTOMER C
JOIN ORDER O
ON C.CUST_ID = O.CUST_ID;

👉 비식별자 관계여도 JOIN 발생

2️⃣ BETWEEN 조건 변환
✔ 기본 BETWEEN
COL1 BETWEEN 200 AND 400

동일 표현

COL1 >= 200 AND COL1 <= 400
✔ 값이 가운데 있는 경우
200 BETWEEN COL1 AND COL2

동일 표현

COL1 <= 200 AND COL2 >= 200

👉 값이 범위 안에 있는지 검사

3️⃣ 부분 문자열 함수 (SUBSTR)

문자열의 일부를 추출할 때 사용한다.

문법
SUBSTR(문자열, 시작위치, 길이)
예시
SELECT SUBSTR('DATABASE',1,4) FROM DUAL;

결과

DATA
4️⃣ 다중행 서브쿼리 비교
✔ WHERE 절 비교

다중행 서브쿼리는 단일 비교 연산자 사용 불가

❌ 잘못된 예

SELECT *
FROM EMP
WHERE DEPTNO = (
    SELECT DEPTNO
    FROM DEPT
);
✔ 올바른 방법
IN
SELECT *
FROM EMP
WHERE DEPTNO IN (
    SELECT DEPTNO
    FROM DEPT
);
EXISTS
SELECT *
FROM EMP E
WHERE EXISTS (
    SELECT 1
    FROM DEPT D
    WHERE E.DEPTNO = D.DEPTNO
);
5️⃣ UNIQUE KEY vs PRIMARY KEY
구분	특징
PRIMARY KEY	테이블당 1개만 가능
PRIMARY KEY	NULL 불가
UNIQUE KEY	여러 개 가능
UNIQUE KEY	NULL 허용 가능
예시
CREATE TABLE USER_INFO
(
ID NUMBER PRIMARY KEY,
EMAIL VARCHAR2(100) UNIQUE
);

👉 EMAIL은 NULL 가능

6️⃣ RIGHT OUTER JOIN
✔ 특징

오른쪽 테이블은 모두 출력

왼쪽 테이블은 매칭되는 데이터만 출력

예시
SELECT A.NAME, B.ORDER_ID
FROM CUSTOMER A
RIGHT JOIN ORDERS B
ON A.CUST_ID = B.CUST_ID;

👉 ORDERS 테이블은 전부 출력

7️⃣ HASH JOIN 특징
✔ 특징

동등 조인 (=) 에 적합

작은 테이블 → HASH TABLE 생성

큰 테이블 → Probe

처리 과정

1️⃣ 작은 테이블 읽기
2️⃣ HASH AREA에 해시 테이블 생성
3️⃣ 큰 테이블 읽으며 매칭

주의

큰 테이블로 HASH 생성 시

메모리 부족

과도한 SORT 발생

성능 저하

사용 상황

✔ 대용량 테이블 조인
✔ 수행 빈도 낮고 실행시간 긴 작업

8️⃣ 서브타입 모델 (ONE-TO-ONE TYPE / PLUS TYPE)
ONE TO ONE TYPE

문제점

테이블 수 증가

관리 어려움

PLUS TYPE

특징

항상 사용되는 것은 아님

서브타입별 테이블 분리

단점

👉 조인 발생

9️⃣ 문자열 따옴표 출력

SQL에서 문자열 안에 ' 출력하려면
'' (두개) 사용한다.

예시
SELECT '''A''''' FROM DUAL;

출력

'A''

설명

입력	의미
'	문자열 시작
''	' 문자
''	' 문자
🔟 복합 PK와 인덱스

복합 PK 생성 시 자동으로 복합 인덱스 생성

예시

PRIMARY KEY (COL1, COL2)

생성 인덱스

INDEX (COL1, COL2)
✔ 인덱스 효율 규칙

EQUAL 조건 → RANGE 조건 순서

좋은 예

WHERE COL1 = 10
AND COL2 BETWEEN 100 AND 200

나쁜 예

WHERE COL1 BETWEEN 100 AND 200
AND COL2 = 10

👉 EQUAL 조건이 앞쪽 컬럼이어야 효율적

1️⃣1️⃣ Oracle OUTER JOIN (+)

Oracle 구문

SELECT *
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO(+);

의미

LEFT OUTER JOIN

👉 (+) 가 붙은 테이블이 OUTER JOIN 대상

📌 SQLD 핵심 요약

시험에서 많이 헷갈리는 개념

비식별자 관계 ≠ 조인 감소

BETWEEN ↔ 비교 연산 변환

다중행 서브쿼리 → IN / EXISTS

UNIQUE → NULL 가능

HASH JOIN → 동등 조인

복합 인덱스 → EQUAL → RANGE 순서

Oracle OUTER JOIN → (+)