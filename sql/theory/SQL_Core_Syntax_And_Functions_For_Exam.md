📘 SQL 핵심 문법 및 명령어 정리 (정처기 실기 / SQLD 대비)
1️⃣ SQL 명령어 분류
✅ DDL (Data Definition Language)

👉 데이터 구조 정의

CREATE

ALTER

RENAME

TRUNCATE

DROP

📌 암기: CARTD

✅ DML (Data Manipulation Language)

👉 데이터 조작

SELECT

INSERT

UPDATE

DELETE

MERGE

📌 ⚠️ 정정 포인트
❌ DCL 아님 → DML이 맞음

📌 암기: SIUDM

✅ DCL (Data Control Language)

👉 권한 제어

GRANT

REVOKE

✅ TCL (Transaction Control Language)

👉 트랜잭션 제어

COMMIT

ROLLBACK

SAVEPOINT

2️⃣ DROP / TRUNCATE / DELETE 차이 (시험 단골)
🔹 DROP
DROP TABLE 테이블명;


테이블 구조 + 데이터 모두 삭제

DDL

ROLLBACK ❌

저장공간 릴리즈 ⭕

로그 거의 안 남김

📌 ⚠️ 주의

DROP은 테이블 삭제
❌ 스키마 전체 삭제는 DROP SCHEMA

🔹 TRUNCATE
TRUNCATE TABLE 테이블명;


데이터만 삭제

테이블 구조 유지

DDL

ROLLBACK ❌

저장공간 릴리즈 ⭕

로그 거의 안 남김 (UNDO 데이터 생성 X)

📌 테이블 초기화 목적

🔹 DELETE
DELETE FROM 테이블명;


데이터 삭제

DML

ROLLBACK ⭕

저장공간 릴리즈 ❌

로그 남김

🔥 성능 비교 (동일 데이터 삭제 시)
구분	DELETE	TRUNCATE
명령어	DML	DDL
로그	남김	거의 안 남김
ROLLBACK	가능	불가
속도	느림	빠름

📌 TRUNCATE가 빠른 이유

UNDO 데이터를 생성하지 않기 때문

3️⃣ 문자열 함수
🔹 || (합성 연산자)
'Hello' || 'World'


문자열 연결

🔹 CHR(arg)

ASCII 코드 → 문자 반환

CHR(65) → 'A'

🔹 TRIM
TRIM([[LEADING | TRAILING | BOTH] 제거문자 FROM] 문자열)


기본: 양쪽 공백 제거

TRIM(' A ')
TRIM(BOTH 'A' FROM 'AAHELLOAA')

🔹 SUBSTR
SUBSTR(arg1, arg2, arg3)


arg1: 문자열

arg2: 시작 위치 (1부터)

arg3: 길이

🔹 REPLACE
REPLACE(arg1, arg2, arg3)


arg3 생략 시 삭제

4️⃣ 숫자 함수
함수	설명
ABS	절댓값
MOD	나머지
ROUND	반올림
TRUNC	버림
SIGN	부호 반환
CEIL	올림
FLOOR	내림
5️⃣ 날짜 함수
🔹 SYSDATE

현재 날짜 반환 (DATE 타입)

🔹 EXTRACT
EXTRACT(YEAR FROM SYSDATE)


년 / 월 / 일 추출

6️⃣ 형 변환 함수

TO_CHAR

TO_NUMBER

TO_DATE

📌 명시적 형 변환 = 시험 단골

7️⃣ NULL 관련 함수
🔹 NVL
NVL(값1, 값2)


값1이 NULL → 값2

🔹 NULLIF
NULLIF(값1, 값2)


같으면 NULL

다르면 값1

🔹 COALESCE
COALESCE(a, b, c)


NULL이 아닌 첫 번째 값 반환

8️⃣ CASE 문
형식 1
CASE
 WHEN 컬럼 = 값 THEN 결과
END

형식 2
CASE 컬럼
 WHEN 값 THEN 결과
END

9️⃣ 조건 연산자
🔹 IN / NOT IN

IN → OR

NOT IN → AND

🔹 LIKE 와일드카드
패턴	의미
%A%	A 포함
_	임의의 문자 1개
LIKE '_A_'  -- 3글자, 가운데 A


📌 % → 0개 이상
📌 _ → 정확히 1개

🔥 시험용 핵심 요약

TRUNCATE는 DDL, DELETE는 DML

TRUNCATE는 로그를 거의 남기지 않아 빠름

DELETE는 ROLLBACK 가능

_는 임의의 문자 1개

%는 0개 이상