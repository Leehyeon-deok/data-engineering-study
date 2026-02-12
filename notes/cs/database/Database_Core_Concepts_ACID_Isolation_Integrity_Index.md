📌 Database 핵심 개념 정리 (트랜잭션, 무결성, 격리수준, 인덱스, NoSQL)
1️⃣ 트랜잭션(Transaction)과 ACID
✅ 트랜잭션이란?

하나의 논리적인 작업 단위
ALL OR NOTHING (전부 수행되거나 전부 취소)

예:

BEGIN;
UPDATE account SET balance = balance - 10000 WHERE id = 1;
UPDATE account SET balance = balance + 10000 WHERE id = 2;
COMMIT;


둘 중 하나라도 실패하면 → ROLLBACK

✅ ACID 원칙
속성	의미	설명
Atomicity	원자성	전부 성공 or 전부 실패
Consistency	일관성	무결성 규칙을 항상 만족
Isolation	고립성	동시에 실행되어도 서로 영향 X
Durability	지속성	COMMIT 후 영구 저장
2️⃣ 트랜잭션 격리 수준 (Isolation Level)
📌 격리수준 단계
격리수준	더티리드	반복불가조회	팬텀리드
READ_UNCOMMITTED	O	O	O
READ_COMMITTED	X	O	O
REPEATABLE_READ	X	X	O
SERIALIZABLE	X	X	X
📌 발생 현상 정리
1️⃣ Dirty Read (더티 리드)

커밋되지 않은 데이터를 읽음

T1이 UPDATE → 아직 COMMIT 안함
T2가 읽음 → 이후 T1이 ROLLBACK
→ 존재하지 않는 데이터를 읽은 것

2️⃣ Non-Repeatable Read (반복 불가능 조회)

같은 쿼리를 두 번 실행했는데 결과가 달라짐

T1: SELECT balance
T2: UPDATE balance → COMMIT
T1: 다시 SELECT → 값 달라짐

3️⃣ Phantom Read (팬텀 리드)

조건 검색 결과 행 개수가 달라짐

T1:

SELECT * FROM orders WHERE price > 1000;


T2:

INSERT INTO orders VALUES (....);
COMMIT;


T1이 다시 조회 → 새로운 행이 나타남

📌 격리수준 설명
🔹 READ_UNCOMMITTED

가장 낮음

성능 빠름

정합성 매우 낮음

🔹 READ_COMMITTED

커밋된 데이터만 읽음

Oracle 기본

🔹 REPEATABLE_READ

읽은 행은 트랜잭션 끝까지 유지

MySQL 기본

🔹 SERIALIZABLE

완전한 직렬 실행

성능 가장 느림

가장 안전

3️⃣ 데이터 무결성 (Integrity)
1️⃣ 개체 무결성 (Entity Integrity)

기본키는 NULL 불가

PRIMARY KEY (id)

2️⃣ 참조 무결성 (Referential Integrity)

외래키는 참조 테이블에 존재해야 함

FOREIGN KEY (user_id) REFERENCES users(id)


삭제 시:

CASCADE

SET NULL

RESTRICT

3️⃣ 고유 무결성 (Unique Integrity)
UNIQUE (email)


중복 불가

4️⃣ NULL 무결성
name VARCHAR(50) NOT NULL


NULL 불가 제약조건

4️⃣ RDBMS vs NoSQL
📌 PostgreSQL

오픈소스 RDBMS

MVCC 기반

ACID 완전 지원

JSON 지원 가능

📌 MongoDB

Document 기반 NoSQL

JSON 형태 (BSON)

스키마 유연

수평 확장 용이

예:

{
  "name": "Kim",
  "age": 30
}

📌 Redis

Key-Value 저장소

인메모리 DB

캐시, 세션 관리에 사용

매우 빠름

5️⃣ 인덱스(Index)
📌 B-Tree 인덱스란?

균형 트리 구조

왜 빠른가?

전체 탐색: O(N)
B-Tree 탐색: O(log N)

→ 대수적 확장성(Logarithmic Scalability)

데이터가 100 → 1억개로 증가해도
탐색 깊이는 거의 증가하지 않음

📌 MySQL 인덱스 생성
CREATE INDEX idx_name ON users(name);


복합 인덱스:

CREATE INDEX idx_user ON users(name, age);

📌 MongoDB 인덱스 생성
db.users.createIndex({ name: 1 });


복합:

db.users.createIndex({ name: 1, age: -1 });


1 → 오름차순
-1 → 내림차순

6️⃣ 인덱스 최적화 전략
⚠ 인덱스는 비용이다

저장공간 증가

INSERT / UPDATE / DELETE 느려짐

유지비용 발생

📌 복합 인덱스 설계 순서

👉 같음 → 정렬 → 범위 → 카디널리티

예:

WHERE user_id = 10
AND status = 'Y'
AND created_at > '2024-01-01'
ORDER BY created_at


인덱스 설계:

(user_id, status, created_at)

📌 카디널리티

중복도

높은 카디널리티 (거의 중복 없음) → 인덱스 효율 좋음
낮은 카디리널리티 → 비효율적

예:

성별 → 낮음

주민번호 → 높음

📌 항상 EXPLAIN으로 확인
EXPLAIN SELECT * FROM users WHERE name = 'Kim';


Full Scan인지
Index Scan인지 반드시 확인

7️⃣ 프로브 단계 (Hash Join)

해시 조인 시

1️⃣ Build 단계
→ 작은 테이블 해시 생성

2️⃣ Probe 단계
→ 큰 테이블을 읽으며 해시 테이블 탐색

→ 매칭 데이터 찾음

🔥 면접/시험 핵심 정리

✔ ACID 4가지
✔ 격리수준 4단계와 발생현상
✔ 무결성 4가지
✔ B-Tree는 O(logN)
✔ 인덱스는 비용이다
✔ 복합인덱스 순서 중요
✔ 카디널리티 이해
✔ 해시조인 = Build + Probe