📌 Information Processing Engineer (Practical) – Frequently Confused Concepts Review
1️⃣ SQL SELECT, DISTINCT, COUNT 개념 정리
✔ 문제 상황

학생 테이블에

전기과 50명

전산과 100명

전자과 50명

총 학생 수 = 200명

🔹 (1) SELECT 학과 FROM 학생;

👉 DISTINCT가 없으면 중복 포함

즉, 각 학생의 학과가 그대로 출력된다.

학과
전기과
전기과
...
전산과
...

따라서 결과 튜플 수는
👉 전체 학생 수 = 200개

✔ 핵심

SELECT는 중복 제거를 하지 않는다.

🔹 (2) SELECT DISTINCT 학과 FROM 학생;

👉 DISTINCT = 중복 제거

학과 종류만 출력된다.

학과 종류:

전기과

전산과

전자과

따라서 결과 튜플 수
👉 3개

✔ 핵심

DISTINCT는 중복을 제거한다.

GROUP BY와 유사한 역할.

🔹 (3) SELECT COUNT(DISTINCT 학과) FROM 학생 WHERE 학과='전산과';

먼저 WHERE 조건 적용
👉 전산과 학생만 남음 → 100명

이 상태에서 DISTINCT 적용
👉 전산과만 존재 → 1개

COUNT
👉 결과 = 1

✔ 핵심

WHERE → DISTINCT → COUNT 순서로 처리됨.

⭐ 정리
SQL	결과
SELECT 학과	200
SELECT DISTINCT 학과	3
COUNT(DISTINCT 학과) WHERE 전산과	1
2️⃣ C언어 switch문과 break 없는 경우 (Fall Through)
✔ 코드
int c = 1;
switch (3) {
   case 1: c += 3;
   case 2: c++;
   case 3: c = 0;
   case 4: c += 3;
   case 5: c -= 10;
   default: c--;
}

🔹 핵심 개념

👉 switch문에서 break가 없으면 아래 case가 계속 실행됨 (Fall Through)

🔹 실행 과정

초기값
👉 c = 1

switch(3) → case 3부터 실행

case 3
c = 0

case 4
c = 0 + 3 = 3

case 5
c = 3 - 10 = -7

default
c = -7 - 1 = -8

👉 최종 결과
-8

✔ 핵심 정리

break 없으면 다음 case 계속 실행

시험에서 매우 자주 출제됨.

3️⃣ MD5 암호화 해시 알고리즘
✔ 특징

128비트 해시 값 생성

단방향 해시 함수

파일 무결성 검사에 사용

RFC 1321 표준

1991년 개발

개발자
👉 Ronald Rivest

목적
👉 기존 MD4의 보안 문제 개선

✔ 활용

파일 변조 여부 확인

비밀번호 해싱 (현재는 보안 취약)

데이터 무결성 검사

✔ 주의

현재는 충돌 공격 가능
👉 보안 시스템에서는 SHA-256 등 사용.

4️⃣ 릴리즈 노트 (Release Note) 구성 요소
✔ 문제 설명

다음 정보 포함:

릴리즈 노트 이름

소프트웨어 이름

릴리즈 버전

릴리즈 날짜

릴리즈 노트 날짜

릴리즈 노트 버전

👉 정답
헤더(Header, 머릿말)

🔹 릴리즈 노트 주요 구성
✔ 1. Header (머릿말)

기본 정보

버전

날짜

소프트웨어 이름

✔ 2. 개요

변경 목적

주요 기능

✔ 3. 변경 사항

추가 기능

수정 사항

개선 내용

✔ 4. 영향도

사용자 영향

시스템 영향

✔ 5. 참고 사항

설치 방법

주의 사항

⭐ 시험 핵심 포인트 정리
✔ SQL

DISTINCT는 중복 제거

COUNT(DISTINCT)는 유니크 개수

✔ C언어

switch에서 break 없으면 연속 실행

✔ 보안

MD5 = 128비트 해시

현재 보안 취약

✔ 소프트웨어 공학

릴리즈 노트 기본 정보 = Header