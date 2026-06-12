Data Model, Security & Protocol Concepts

DAC, MAC, RBAC / Data Model Components / CIA Triad / Protocol Elements

1. Data Model Components (데이터 모델 구성요소)

데이터 모델은 데이터베이스에서 데이터의 구조와 관계, 제약 조건을 정의하는 개념이다.
데이터 모델의 구성요소는 다음 3가지이다.

1) Structure (구조)

데이터가 어떤 형태로 구성되는지를 정의한다.

예

테이블

엔터티

속성

관계

즉, 데이터의 구조와 관계를 표현하는 요소이다.

2) Operation (연산)

데이터를 어떻게 처리할 것인지를 정의한다.

예

SELECT

INSERT

UPDATE

DELETE

즉, 데이터 처리 방법을 정의하는 요소이다.

3) Constraint (제약조건)

데이터의 정확성과 일관성을 유지하기 위한 규칙이다.

대표적인 무결성 제약조건

Entity Integrity (개체 무결성)

Primary Key는 NULL이 될 수 없음

Referential Integrity (참조 무결성)

Foreign Key는 참조하는 값이 존재해야 함

예

PRIMARY KEY

FOREIGN KEY

UNIQUE

NOT NULL

CHECK

2. Access Control Models (접근 통제 모델)

접근 통제는 시스템 자원에 대한 접근을 제한하는 보안 기술이다.

대표적인 접근 통제 모델은 다음 3가지이다.

1) DAC (Discretionary Access Control)

임의 접근 통제

특징

객체 소유자가 접근 권한을 결정

권한 위임 가능

비교적 유연하지만 보안이 약함

예

Linux 파일 권한

Windows 파일 권한

사용자 → 자원
(소유자가 권한 설정)
2) MAC (Mandatory Access Control)

강제 접근 통제

특징

시스템이 접근 권한을 강제로 통제

사용자 임의 변경 불가

보안 등급 기반

사용 환경

군사 시스템

정부 기관

대표 규칙

No Read Up

No Write Down

사용자 등급 ↔ 데이터 등급
시스템이 접근 여부 결정
3) RBAC (Role Based Access Control)

역할 기반 접근 통제

특징

사용자에게 직접 권한 부여 X

역할(Role)에 권한 부여

구조
User → Role → Permission → Resource
장점

대규모 조직에서 관리 쉬움

권한 관리 효율적

3. Information Security Triad (정보보안 3요소)

정보보안의 기본 원칙은 다음 3가지이다.

1) Confidentiality (기밀성)

허가된 사용자만 정보에 접근할 수 있도록 보호하는 것

예

암호화

접근통제

인증

2) Integrity (무결성)

데이터가 변조되지 않고 정확하게 유지되는 것

예

해시(Hash)

전자서명

무결성 검사

3) Availability (가용성)

허가된 사용자가 언제든지 시스템과 데이터에 접근 가능해야 함

예

백업

이중화

장애 복구 시스템

4. Protocol Elements (프로토콜 구성 요소)

프로토콜은 네트워크에서 데이터를 주고받기 위한 통신 규칙이다.

프로토콜의 기본 구성 요소는 3가지이다.

1) Syntax (구문)

데이터의 형식과 구조를 정의한다.

예

데이터 형식

패킷 구조

비트 순서

2) Semantics (의미)

각 데이터가 어떤 의미를 가지는지 정의한다.

예

오류 제어

흐름 제어

제어 정보

3) Timing (타이밍)

데이터 전송 속도와 순서를 정의한다.

예

데이터 전송 속도

데이터 전송 순서

동기화

Summary
Data Model Components
구성요소	설명
Structure	데이터 구조
Operation	데이터 처리
Constraint	데이터 제약 조건
Access Control Models
모델	의미	특징
DAC	임의 접근통제	소유자가 권한 결정
MAC	강제 접근통제	시스템이 권한 통제
RBAC	역할 기반 접근통제	역할 중심 권한 관리
Information Security Triad
요소	의미
Confidentiality	기밀성
Integrity	무결성
Availability	가용성
Protocol Elements
요소	의미
Syntax	데이터 형식
Semantics	데이터 의미
Timing	데이터 전송 시간