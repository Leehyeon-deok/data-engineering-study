📌 SQL 무결성 & 데이터 변경 명령어 완전 정리 (DELETE, UPDATE, FK 옵션, DROP/TRUNCATE 차이)
1️⃣ UPDATE + DELETE 관련 개념 정리
✅ UPDATE 후 DELETE 수행 기준

DELETE는 UPDATE 절로 갱신된 행 전체를 기준으로 삭제된다.
갱신된 값을 기준으로 조건을 다시 평가하여 삭제한다.

🔎 예제
UPDATE EMP
SET SAL = SAL * 1.1
WHERE DEPTNO = 10;

DELETE FROM EMP
WHERE SAL > 5000;
✔ 해석

먼저 DEPTNO=10 인 행들의 SAL이 변경됨

변경된 SAL 값을 기준으로

SAL > 5000 조건을 만족하는 행을 삭제

👉 DELETE는 기존 값이 아니라 UPDATE 후의 값을 기준으로 동작한다

2️⃣ FK 제약조건 옵션 정리

외래키(FK)는 부모 테이블 변경 시 자식 테이블에 어떤 영향을 줄지 결정한다.

✅ 1. CASCADE

👉 부모 삭제/수정 시 자식도 함께 삭제/수정

FOREIGN KEY (C)
REFERENCES TBL1(C)
ON DELETE CASCADE
예시

TBL1

C
10

TBL2

B	C
1	10
2	10
DELETE FROM TBL1 WHERE C = 10;

👉 TBL2에서 C=10 인 행 전체 삭제

✅ 2. RESTRICT

👉 자식이 존재하면 부모 삭제 금지

ON DELETE RESTRICT

✔ 자식 행이 있으면 에러 발생
✔ 가장 안전한 방식

✅ 3. NO ACTION

👉 RESTRICT와 거의 동일
👉 부모 삭제 시 자식 존재하면 오류 발생

(대부분 DB에서 기본값)

✅ 4. SET NULL

👉 부모 삭제 시 자식 FK 값을 NULL로 변경

ON DELETE SET NULL

단, FK 컬럼이 NULL 허용이어야 함

✅ 5. SET DEFAULT

👉 부모 삭제 시 FK 값을 DEFAULT 값으로 변경

ON DELETE SET DEFAULT

컬럼에 DEFAULT 값이 정의되어 있어야 함

✅ 6. AUTOMATIC

일부 DB에서 내부적으로 자동 처리되는 옵션을 의미
(시험에서는 거의 나오지 않음)

✅ 7. DEPENDENT

부모-자식 의존 관계 표현
일반 SQL 표준 옵션은 아님 (DBMS 종속적 개념)

🎯 FK 옵션 시험 핵심 정리
옵션	부모 삭제 시	자식 처리
CASCADE	허용	함께 삭제
RESTRICT	불가	에러 발생
NO ACTION	불가	에러 발생
SET NULL	허용	NULL 변경
SET DEFAULT	허용	DEFAULT 값 변경
3️⃣ DROP vs TRUNCATE vs DELETE

이건 시험 단골 🔥

✅ 1. DELETE
DELETE FROM EMP WHERE DEPTNO = 10;

✔ 조건 사용 가능
✔ DML
✔ ROLLBACK 가능
✔ 로그 기록 많이 남음
✔ 구조 유지

✅ 2. TRUNCATE
TRUNCATE TABLE EMP;

✔ WHERE 절 불가
✔ 전체 삭제
✔ DDL
✔ ROLLBACK 불가 (대부분 DB)
✔ 로그 거의 안 남음 → 빠름
✔ 구조 유지

✅ 3. DROP
DROP TABLE EMP;

✔ 테이블 자체 삭제
✔ 구조 + 데이터 모두 삭제
✔ DDL
✔ ROLLBACK 불가

🎯 차이 비교표
구분	DELETE	TRUNCATE	DROP
종류	DML	DDL	DDL
WHERE	가능	불가	불가
롤백	가능	불가	불가
속도	느림	빠름	매우 빠름
테이블 구조	유지	유지	삭제
🔥 시험 함정 포인트

TRUNCATE는 DML이 아니다 → DDL이다

CASCADE는 컬럼 삭제가 아니라 행 삭제

SET NULL은 FK 컬럼이 NOT NULL이면 사용 불가

DELETE는 UPDATE 이후 변경된 값 기준으로 수행됨

DROP은 복구 거의 불가