📘 데이터 모델링 & SQL 핵심 정리 (정보처리기사 / SQLD)
1. 데이터 모델링의 이해
1-1. 데이터 모델링 정의
복잡한 현실 세계를 추상화 / 단순화하여 표현하는 과정
DB 구축을 위한 분석 + 설계 과정
정보시스템 구축을 위한 데이터 관점 업무 분석 기법
1-2. 모델링 특징
추상성
단순성
명확성
1-3. 모델링 관점
① 데이터 관점 (WHAT)
무엇이 필요한가
데이터와 데이터 간의 관계
② 프로세스 관점 (HOW)
어떻게 처리되는가
업무 절차 중심
③ 상호작용 관점 (INTERACTION)
데이터와 프로세스의 상호 영향
1-4. 모델링 중요성
파급 효과 큼
간결한 표현 가능
데이터 품질 유지
유의점
중복 최소화
비유연성 방지 (프로세스와 분리)
비일관성 제거
1-5. 데이터 모델링 3단계
단계	설명
개념 모델	ERD 도출, 핵심 엔터티 추출
논리 모델	테이블 구조 (PK, FK, 정규화)
물리 모델	DBMS 기준 실제 구현
1-6. 데이터 독립성
응용프로그램과 데이터 구조 분리
종류
논리적 데이터 독립성: 개념 스키마 변경 → 외부 영향 없음
물리적 데이터 독립성: 내부 스키마 변경 → 개념/외부 영향 없음
1-7. DB 스키마
데이터 구조, 타입, 제약조건 정의
1-8. 3단계 스키마 구조
스키마	설명
외부 스키마	사용자 View
개념 스키마	전체 통합 구조
내부 스키마	물리 저장 구조
1-9. 사상(Mapping)
스키마 간 연결 역할
1-10. 구성요소
Entity (개체)
Attribute (속성)
Relationship (관계)
Instance (데이터 값)
1-11. ERD
Entity Relationship Diagram
엔터티 + 관계 시각화
작업 순서
엔터티 도출
배치
관계 설정 (카디널리티/옵션 포함)
2. 엔터티 (Entity)
2-1. 정의
업무상 관리 대상 객체의 집합
2-2. 유형
① 유무형 기준
유형 엔터티
개념 엔터티
사건 엔터티 (주문, 수강신청 등)
② 발생 시점 기준
기본 엔터티 (독립)
중심 엔터티
행위 엔터티 (다른 엔터티로부터 생성)
2-3. 특징
업무 필요성 존재
식별자 존재
인스턴스 집합
관계 최소 1개 이상
속성 보유
3. 속성 (Attribute)
3-1. 정의
더 이상 분리 불가능한 최소 데이터 단위
3-2. 종류
기본 속성
제품명, 제조일
설계 속성
코드 (001, 002)
파생 속성
계산된 값 (총합, 평균)
3-3. 키 속성
PK: 기본키
FK: 외래키
3-4. 속성 유형
값 개수
단일값 속성
다중값 속성 → 1NF 위반 → 분리 필요
구조
단순 속성
복합 속성 (주소 → 시/구/동)
4. 식별자 (Identifier)
특징
유일성
최소성
불변성
존재성 (NULL 불가)
종류
기본키 / 후보키 / 슈퍼키 / 대체키
본질식별자 / 인조식별자
5. 관계 (Relationship)
종류
1. 존재 관계 (UML: 실선)
항상 연결됨
2. 행위 관계 (UML: 점선)
이벤트/행위 기반
6. 정규화
목적
중복 제거
무결성 유지
이상현상 제거
이상 현상
삽입 이상
삭제 이상
갱신 이상
반정규화
JOIN 성능 문제 해결 위해 일부 중복 허용
7. NULL 개념
0, 공백과 다름
미정의 값
연산 시 결과도 NULL
8. SQL 핵심
8-1. DML
SELECT
INSERT
UPDATE
DELETE
MERGE

👉 COMMIT 필요 / ROLLBACK 가능

8-2. DDL
CREATE
ALTER
DROP
TRUNCATE

👉 AUTO COMMIT (ROLLBACK 불가)

8-3. DCL
GRANT
REVOKE
8-4. TCL
COMMIT
ROLLBACK
SAVEPOINT
9. SQL 함수
단일 행 함수
ABS, SIGN
CEIL, FLOOR
ROUND, TRUNC
POWER, SQRT
MOD
10. 서브쿼리
스칼라 서브쿼리: 1값 반환
인라인 뷰: FROM 절 테이블처럼 사용
중첩 서브쿼리: WHERE 필터링
11. GROUP BY / HAVING
GROUP BY: 그룹 생성
HAVING: 그룹 조건

👉 SELECT에 일반 컬럼 쓰려면 집계함수 필요

12. 집합 조건
ANY / ALL
ANY: 하나라도 만족
ALL: 모두 만족
핵심
> ANY → 최소값 기준
< ALL → 최소값보다 작아야 함
13. JOIN 핵심 (보강)
INNER JOIN: 교집합
LEFT JOIN: 왼쪽 기준
RIGHT JOIN: 오른쪽 기준
FULL OUTER JOIN: 전체
USING / ON 차이
USING: 같은 컬럼 자동 매칭
ON: 조건 직접 지정
14. 윈도우 함수 (추가 핵심)
RANK()
DENSE_RANK()
ROW_NUMBER()
LAG()
LEAD()
15. 계층형 쿼리 (추가)
PRIOR 사용
부모 → 자식 구조 표현
16. ROLLUP / CUBE / GROUPING SETS
ROLLUP: 계층 합계
CUBE: 모든 조합
GROUPING SETS: 원하는 조합만