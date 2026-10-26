# DDL, DML 트랜잭션 및 DROP · TRUNCATE · DELETE 정리

## 1. DDL과 DML의 차이

### DDL (Data Definition Language)
데이터베이스의 구조를 정의하거나 변경하는 언어

- `CREATE` : 객체 생성
- `ALTER` : 객체 구조 변경
- `DROP` : 객체 삭제
- `TRUNCATE` : 테이블의 전체 데이터 삭제

**특징**
- 일반적으로 DDL은 실행 시 암묵적 커밋이 발생한다.
- 따라서 일반적인 DML처럼 `ROLLBACK`으로 실행 전 상태를 되돌릴 수 없다.
- 단, 정확한 동작은 DBMS에 따라 다를 수 있다.

### DML (Data Manipulation Language)
테이블의 데이터를 조회하거나 조작하는 언어

- `SELECT` : 데이터 조회
- `INSERT` : 데이터 삽입
- `UPDATE` : 데이터 수정
- `DELETE` : 데이터 삭제

**특징**
- 일반적으로 DML은 명시적으로 `COMMIT`하기 전까지 트랜잭션을 확정하지 않는다.
- `ROLLBACK`을 실행하면 커밋하지 않은 변경 사항을 취소할 수 있다.
- 다른 사용자는 일반적으로 커밋되지 않은 변경 사항을 볼 수 없다. 단, 격리 수준과 DBMS 설정에 따라 달라질 수 있다.

```sql
DELETE FROM EMPLOYEE
WHERE EMP_ID = 100;

-- 변경 사항 확정
COMMIT;

-- 또는 커밋 전 변경 사항 취소
ROLLBACK;
```

> 주의: `COMMIT`한 뒤에는 일반적인 `ROLLBACK`으로 해당 변경 사항을 되돌릴 수 없다.

---

## 2. DROP · TRUNCATE · DELETE 차이

| 구분 | DROP | TRUNCATE | DELETE |
|---|---|---|---|
| 분류 | DDL | DDL | DML |
| 삭제 대상 | 테이블 객체 자체 | 테이블의 전체 데이터 | 조건에 맞는 행 |
| 테이블 구조 | 삭제됨 | 유지됨 | 유지됨 |
| `WHERE` 사용 | 불가능 | 불가능 | 가능 |
| 삭제 범위 | 테이블 전체 | 테이블 전체 데이터 | 전체 또는 일부 행 |
| 일반적인 ROLLBACK | 불가능 | 불가능 | 가능 |
| 일반적인 자동 커밋 | 발생 | 발생 | 발생하지 않음 |
| 삭제 후 테이블 사용 | 테이블 자체가 없어짐 | 계속 사용 가능 | 계속 사용 가능 |

※ 자동 커밋 및 롤백 가능 여부는 DBMS에 따라 차이가 있다. 특히 Oracle과 PostgreSQL 등은 `TRUNCATE`의 트랜잭션 처리 방식이 다르다.

### 2-1. DROP

테이블 객체 자체를 삭제한다.

```sql
DROP TABLE EMPLOYEE;
```

- 테이블 구조와 데이터가 모두 사라진다.
- 테이블을 조회하거나 데이터를 추가할 수 없다.
- 테이블을 다시 사용하려면 새로 생성해야 한다.
- 일반적으로 `ROLLBACK`으로 복구할 수 없다.

**암기:** DROP = 테이블 자체를 제거

### 2-2. TRUNCATE

테이블 구조는 유지하고 내부 데이터를 전체 삭제한다.

```sql
TRUNCATE TABLE EMPLOYEE;
```

- 모든 행을 삭제한다.
- `WHERE` 조건을 사용할 수 없다.
- 테이블 구조는 유지된다.
- 일반적으로 DDL로 분류되며 암묵적 커밋이 발생할 수 있다.
- 일부 DBMS에서는 트랜잭션 내 롤백이 가능하므로 DBMS별 특성을 확인해야 한다.

**암기:** TRUNCATE = 테이블은 남기고 데이터만 비움

### 2-3. DELETE

조건에 맞는 데이터를 삭제한다.

```sql
-- 특정 사원 삭제
DELETE FROM EMPLOYEE
WHERE EMP_ID = 100;

-- 전체 데이터 삭제
DELETE FROM EMPLOYEE;
```

- `WHERE`를 사용하여 특정 행만 삭제할 수 있다.
- `WHERE`를 생략하면 모든 행이 삭제된다.
- 테이블 구조는 유지된다.
- 커밋하기 전이라면 일반적으로 `ROLLBACK`으로 복구할 수 있다.
- 일반적으로 삭제된 각 행에 대한 작업이 수행된다.

**암기:** DELETE = 조건에 따라 행을 삭제

---

## 3. 실행 예제로 비교하기

다음과 같은 테이블이 있다고 가정한다.

| EMP_ID | NAME |
|---:|---|
| 1 | 김철수 |
| 2 | 이영희 |
| 3 | 박민수 |

### DELETE 실행

```sql
DELETE FROM EMPLOYEE
WHERE EMP_ID = 1;
```

결과: 김철수 행만 삭제되고 나머지 데이터는 유지된다.

### TRUNCATE 실행

```sql
TRUNCATE TABLE EMPLOYEE;
```

결과: 모든 데이터가 삭제되지만 EMPLOYEE 테이블 구조는 유지된다.

### DROP 실행

```sql
DROP TABLE EMPLOYEE;
```

결과: EMPLOYEE 테이블 객체 자체가 삭제된다.

---

## 4. 시험 대비 핵심 암기

- **DDL**: 데이터베이스 객체의 구조를 정의하거나 변경한다.
- **DML**: 테이블의 데이터를 조회하거나 조작한다.
- **COMMIT**: 트랜잭션의 변경 사항을 확정한다.
- **ROLLBACK**: 커밋하지 않은 변경 사항을 취소한다.
- **DROP**: 테이블 자체를 삭제한다.
- **TRUNCATE**: 테이블의 전체 데이터를 삭제한다.
- **DELETE**: 조건에 따라 행을 삭제한다.
- **WHERE 사용 가능**: DELETE만 가능하다.
- **테이블 구조 유지**: TRUNCATE와 DELETE.
- **일반적인 롤백 가능 대상**: 커밋 전 DELETE 등의 DML 변경 사항.

### 한 줄 암기법

> DROP은 집을 없애고, TRUNCATE는 집 안을 비우고, DELETE는 원하는 물건만 골라 버린다.

### 주의할 함정

`DELETE FROM EMPLOYEE;`는 테이블 자체를 삭제하는 것이 아니라 모든 행을 삭제한다.

`DROP TABLE EMPLOYEE;`는 데이터뿐 아니라 테이블 객체 자체를 삭제한다.

`TRUNCATE TABLE EMPLOYEE;`는 전체 데이터를 삭제하며 `WHERE` 조건을 지정할 수 없다.

5. SQLD 시험에서 특히 기억할 것

1. 삭제 범위: DROP은 객체, TRUNCATE는 전체 데이터, DELETE는 행을 삭제한다.
2. 조건 지정: WHERE는 DELETE에서만 사용할 수 있다.
3. 트랜잭션: 일반적으로 DELETE는 커밋 전 롤백이 가능하지만, DROP과 TRUNCATE는 DBMS별 차이를 확인해야 한다.