# SQL 핵심 정리: ORDER BY, 함수, 인덱스, 집계 및 실행 계획

## 1. ORDER BY 정렬

`ORDER BY`는 조회 결과를 정렬할 때 사용한다.

### 1-1. 컬럼 순번으로 정렬하기

```sql
SELECT 사원번호, 사원명, 급여
FROM 사원
ORDER BY 3;
```

- `ORDER BY 3`은 `SELECT` 목록의 세 번째 표현식인 `급여`를 기준으로 정렬한다.
- 기본 정렬 방식은 `ASC`(오름차순)이다.
- `DESC`를 지정하면 내림차순으로 정렬한다.

```sql
SELECT 사원번호, 사원명, 급여
FROM 사원
ORDER BY 3 DESC;
```

### 1-2. ORDER BY의 실행 순서

일반적인 SQL의 논리적 처리 순서는 다음과 같다.

`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`

따라서 `ORDER BY`에서 `SELECT` 목록의 컬럼 순번을 사용할 수 있다.

**주의할 점**
- `ORDER BY 3`은 숫자 3 자체가 아니라 세 번째 SELECT 항목을 의미한다.
- SELECT 목록이 변경되면 정렬 기준도 달라질 수 있다.
- 세 번째 항목이 없다면 해당 순번을 사용할 수 없다.
- `ORDER BY`는 결과를 정렬할 뿐, SELECT 목록에서 컬럼을 삭제하지 않는다.

## 2. 숫자 함수

| 함수 | 의미 | 예시 | 결과 |
|---|---|---|---|
| `ROUND` | 반올림 | `ROUND(12.56, 1)` | `12.6` |
| `TRUNC` | 지정한 자릿수에서 버림 | `TRUNC(12.56, 1)` | `12.5` |
| `SIGN` | 부호 판별 | `SIGN(-10)` | `-1` |
| `CEIL` | 입력값 이상인 가장 작은 정수 | `CEIL(3.2)` | `4` |
| `FLOOR` | 입력값 이하인 가장 큰 정수 | `FLOOR(3.8)` | `3` |

### SIGN 함수

```sql
SELECT SIGN(10), SIGN(0), SIGN(-10)
FROM DUAL;
```

결과: `1, 0, -1`

- 양수: `1`
- 0: `0`
- 음수: `-1`

### ROUND와 TRUNC 비교

```sql
SELECT ROUND(15.78, 1) FROM DUAL;
-- 15.8

SELECT TRUNC(15.78, 1) FROM DUAL;
-- 15.7
```

`ROUND`는 반올림하고 `TRUNC`는 지정한 자릿수 아래를 버린다.

## 3. DECODE 함수와 CASE문

`DECODE`는 조건에 따라 결과를 반환하는 함수로, 간단한 동등 비교에 사용할 수 있다.

### DECODE 기본 구조

```sql
DECODE(대상값, 비교값1, 결과1, 비교값2, 결과2, 기본값)
```

예제:

```sql
SELECT DECODE(2, 1, 'Y', NULL)
FROM DUAL;
```

- 대상값 `2`와 비교값 `1`이 다르므로 `NULL`을 반환한다.
- 마지막 `NULL`은 일치하는 조건이 없을 때 반환할 기본값이다.

다른 예제:

```sql
SELECT DECODE(2, 1, 'A', 2, 'B', 'C')
FROM DUAL;
-- B
```

### CASE문으로 변환

```sql
SELECT
    CASE
        WHEN 2 = 1 THEN 'A'
        WHEN 2 = 2 THEN 'B'
        ELSE 'C'
    END
FROM DUAL;
-- B
```

`DECODE`는 주로 동등 비교에 사용하고, `CASE`는 범위 조건이나 다양한 논리 조건에도 사용할 수 있다.

## 4. NULL 처리: NVL

`NVL(C1, C2)`는 첫 번째 인수가 `NULL`이면 두 번째 인수를 반환한다.

```sql
SELECT NVL(NULL, 100) FROM DUAL;
-- 100

SELECT NVL(50, 100) FROM DUAL;
-- 50
```

- `C1`이 `NULL`이면 `C2` 반환
- `C1`이 `NULL`이 아니면 `C1` 반환

**주의:** `NULL`은 일반적인 비교 연산자인 `=`, `<>`로 직접 비교하지 않는다. `IS NULL` 또는 `IS NOT NULL`을 사용한다.

```sql
SELECT *
FROM 사원
WHERE 부서번호 IS NULL;
```

## 5. 비교 연산자와 조건식

### 5-1. 주요 연산자

| 연산자 | 의미 | 예시 |
|---|---|---|
| `=` | 같다 | `급여 = 3000` |
| `<>` | 같지 않다 | `급여 <> 3000` |
| `>` | 초과 | `급여 > 3000` |
| `<` | 미만 | `급여 < 3000` |
| `>=` | 이상 | `급여 >= 3000` |
| `<=` | 이하 | `급여 <= 3000` |
| `IS NULL` | NULL인지 확인 | `부서번호 IS NULL` |
| `LIKE` | 패턴 검색 | `이름 LIKE '김%'` |
| `IN` | 목록에 포함되는지 확인 | `부서번호 IN (10, 20)` |
| `BETWEEN A AND B` | A 이상 B 이하 | `급여 BETWEEN 2000 AND 3000` |

### 5-2. AND, OR, NOT

- `AND`: 모든 조건이 참이어야 참
- `OR`: 조건 중 하나 이상이 참이면 참
- `NOT`: 조건의 논리적 부정

```sql
SELECT *
FROM 사원
WHERE 급여 >= 3000
  AND 부서번호 = 10;
```

### 5-3. IN, ANY, ALL, EXISTS

#### IN

목록에 일치하는 값이 있으면 조건을 만족한다.

```sql
SELECT *
FROM 사원
WHERE 부서번호 IN (10, 20, 30);
```

#### ANY

비교 대상 중 하나 이상과 비교 조건이 참이면 참이다.

```sql
SELECT *
FROM 사원
WHERE 급여 > ANY (
    SELECT 급여
    FROM 사원
    WHERE 부서번호 = 10
);
```

`>`와 함께 사용하면 서브쿼리 결과 중 **하나라도 작은 값이 있으면** 조건을 만족한다.

#### ALL

모든 비교 대상에 대해 비교 조건이 참이어야 한다.

```sql
SELECT *
FROM 사원
WHERE 급여 > ALL (
    SELECT 급여
    FROM 사원
    WHERE 부서번호 = 10
);
```

`>`와 함께 사용하면 서브쿼리 결과의 모든 값보다 급여가 커야 한다.

#### EXISTS

서브쿼리 결과가 한 행 이상 존재하면 참이다.

```sql
SELECT *
FROM 부서 d
WHERE EXISTS (
    SELECT 1
    FROM 사원 s
    WHERE s.부서번호 = d.부서번호
);
```

해당 부서에 소속된 사원이 한 명 이상 존재하는 부서를 조회한다.

**핵심 비교**

| 구문 | 기억할 내용 |
|---|---|
| `IN` | 목록의 값과 일치하는지 |
| `ANY` | 비교 조건이 하나 이상 참인지 |
| `ALL` | 비교 조건이 모두 참인지 |
| `EXISTS` | 서브쿼리 결과 행이 존재하는지 |

주의: `IN`은 목록에 `NULL`이 포함되는 경우 결과가 예상과 다를 수 있다. `NOT IN`은 특히 서브쿼리 결과에 `NULL`이 있으면 조건이 참이 되지 않을 수 있다.

## 6. 인덱스 스캔 종류

인덱스는 데이터를 빠르게 찾기 위한 자료구조다. 인덱스 스캔 방식은 조건과 인덱스 구조에 따라 달라진다.

| 스캔 방식 | 의미 | 핵심 특징 |
|---|---|---|
| `INDEX FULL SCAN` | 인덱스 전체 범위를 스캔 | 인덱스의 전체 범위를 탐색 |
| `INDEX RANGE SCAN` | 인덱스의 특정 범위를 스캔 | 범위 조건이나 일부 값 검색에 사용 |
| `INDEX RANGE SCAN DESCENDING` | 인덱스 범위를 역방향으로 스캔 | 내림차순 탐색 등에 사용 가능 |
| `INDEX UNIQUE SCAN` | 고유한 인덱스 키로 검색 | 일반적으로 하나의 키를 찾을 때 사용 |

### INDEX FULL SCAN

인덱스 전체 범위를 읽는 방식이다.

```sql
SELECT 사원번호
FROM 사원
ORDER BY 사원번호;
```

인덱스가 적절하고 옵티마이저가 유리하다고 판단하면 전체 인덱스 스캔이 사용될 수 있다.

### INDEX RANGE SCAN

```sql
SELECT *
FROM 사원
WHERE 사원번호 BETWEEN 100 AND 200;
```

인덱스에서 조건에 해당하는 범위를 탐색한다.

### INDEX RANGE SCAN DESCENDING

인덱스를 역방향으로 탐색하는 방식이다.

```sql
SELECT 사원번호
FROM 사원
ORDER BY 사원번호 DESC;
```

인덱스를 이용하면 정렬을 줄이거나 생략할 수 있지만, 실제 실행 계획은 인덱스 구성과 옵티마이저 판단에 따라 달라진다.

### INDEX UNIQUE SCAN

```sql
SELECT *
FROM 사원
WHERE 사원번호 = 100;
```

`사원번호`가 고유 인덱스의 키라면 하나의 키를 찾는 데 사용할 수 있다.

**시험 주의:** 인덱스 스캔 방식은 SQL 문장만으로 무조건 결정되지 않는다. 인덱스의 종류, 조건식, 통계정보와 옵티마이저 판단이 영향을 준다.

## 7. 조인 수행 방식

조인은 여러 테이블의 데이터를 연결하는 작업이다. 실행 계획에서는 다음과 같은 방식이 사용될 수 있다.

| 방식 | 동작 원리 | 일반적인 특징 |
|---|---|---|
| `NESTED LOOPS` | 외부 테이블의 각 행에 대해 내부 테이블을 탐색 | 외부 결과가 적고 내부 인덱스가 유용할 때 유리 |
| `HASH JOIN` | 한쪽 데이터를 해시 테이블로 만들고 다른 쪽과 비교 | 대량 데이터의 동등 조인에 유리한 경우가 많음 |
| `SORT MERGE JOIN` | 조인 키 기준으로 정렬한 후 순차적으로 비교 | 정렬된 데이터를 비교하거나 대량 데이터를 처리할 때 유리할 수 있음 |

### NESTED LOOPS

```sql
SELECT *
FROM 부서 d
JOIN 사원 s
  ON d.부서번호 = s.부서번호;
```

외부 테이블에서 행을 가져온 후 내부 테이블에서 대응하는 행을 찾는 방식이다.

### HASH JOIN

한쪽 테이블을 이용해 해시 테이블을 구성하고 다른 쪽 테이블의 행을 대응시킨다. 동등 조건의 대량 조인에서 효율적인 경우가 많다.

### SORT MERGE JOIN

조인 키를 기준으로 데이터를 정렬하고 두 데이터 집합을 순차적으로 비교한다.

**주의:** 소량 데이터에는 항상 `NESTED LOOPS`, 대량 데이터에는 항상 `HASH JOIN`이 정답인 것은 아니다. 실제 비용과 데이터 분포에 따라 달라진다.

## 8. GROUP BY와 집계 함수

`GROUP BY`는 지정한 컬럼을 기준으로 행을 그룹화한다.

### 8-1. GROUP BY + COUNT(*)

```sql
SELECT 부서번호, COUNT(*) AS 사원수
FROM 사원
GROUP BY 부서번호;
```

부서별 사원 수를 계산한다.

### 8-2. GROUP BY + SUM(금액)

```sql
SELECT 부서번호, SUM(금액) AS 총금액
FROM 매출
GROUP BY 부서번호;
```

부서별 금액 합계를 계산한다.

`COUNT(*)`, `SUM(금액)`, `AVG(금액)`, `MAX(금액)`, `MIN(금액)` 등은 그룹별 집계에 사용할 수 있다.

### 8-3. SUM(COUNT(*))는 왜 주의해야 할까?

다음과 같이 같은 쿼리 블록에서 집계 함수를 중첩하는 것은 일반적으로 허용되지 않는다.

```sql
SELECT 부서번호, SUM(COUNT(*))
FROM 사원
GROUP BY 부서번호;
```

집계 함수의 결과를 다시 집계하려면 **서브쿼리로 집계 단계를 분리**한다.

```sql
SELECT SUM(부서별_사원수) AS 전체_사원수
FROM (
    SELECT 부서번호, COUNT(*) AS 부서별_사원수
    FROM 사원
    GROUP BY 부서번호
);
```

안쪽 쿼리에서 부서별 사원 수를 구하고, 바깥쪽 쿼리에서 그 결과를 합산한다.

참고로 전체 사원 수만 구하려는 목적이라면 다음처럼 간단하게 작성하면 된다.

```sql
SELECT COUNT(*) AS 전체_사원수
FROM 사원;
```

## 9. 시험 직전 핵심 암기

- `ORDER BY 3`: SELECT 목록의 세 번째 항목 기준으로 정렬
- 정렬 기본값: `ASC`
- `ROUND`: 반올림
- `TRUNC`: 버림
- `SIGN`: 양수 `1`, 0 `0`, 음수 `-1`
- `CEIL`: 입력값 이상인 가장 작은 정수
- `FLOOR`: 입력값 이하인 가장 큰 정수
- `DECODE`: 동등 비교를 통한 조건별 값 반환
- `NVL(C1, C2)`: C1이 NULL이면 C2 반환
- `<>`: 같지 않음
- `ANY`: 하나 이상
- `ALL`: 모두
- `EXISTS`: 결과 행의 존재 여부
- `IN`: 목록에 포함되는지 확인
- `INDEX UNIQUE SCAN`: 고유 키 검색
- `INDEX RANGE SCAN`: 인덱스 범위 검색
- `NESTED LOOPS`: 외부 행마다 내부 탐색
- `HASH JOIN`: 해시 테이블을 활용한 조인
- `SORT MERGE JOIN`: 정렬 후 순차 비교
- `GROUP BY + COUNT(*)`: 가능
- `GROUP BY + SUM(금액)`: 가능
- 같은 쿼리 블록의 집계 함수 중첩: 일반적으로 불가
- 집계 결과를 다시 집계하려면 서브쿼리로 분리

