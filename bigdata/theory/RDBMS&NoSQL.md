## 1. 데이터베이스 분류 개요

### ▶ RDBMS (관계형 데이터베이스)

* **특징**

  * 정형 데이터, 테이블 기반 (행/열)
  * 스키마 고정
  * SQL 사용
  * 트랜잭션에서 **ACID** 보장
* **장점**: 데이터 무결성, 일관성, 복잡한 JOIN
* **단점**: 수평 확장(Scale-out) 어려움
* **대표 DB**: Oracle, MySQL, PostgreSQL, MS SQL

### ▶ NoSQL (비관계형 데이터베이스)

* **특징**

  * 비정형/반정형 데이터
  * 스키마 유연
  * 대용량, 분산 환경에 최적화
  * BASE 성향
* **장점**: 수평 확장 용이, 고가용성
* **단점**: 복잡한 트랜잭션, JOIN 어려움
* **대표 DB**: Redis, MongoDB, Cassandra, DynamoDB

---

## 2. RDBMS vs NoSQL 비교

| 구분     | RDBMS    | NoSQL                  |
| ------ | -------- | ---------------------- |
| 데이터 모델 | 테이블      | Key-Value / Document 등 |
| 스키마    | 고정       | 유연                     |
| 확장성    | Scale-up | Scale-out              |
| 트랜잭션   | ACID     | BASE                   |
| 사용 사례  | 금융, ERP  | 로그, 세션, 빅데이터           |

---

## 3. ACID vs BASE

### ▶ ACID (RDBMS)

* **Atomicity**: 원자성
* **Consistency**: 일관성
* **Isolation**: 격리성
* **Durability**: 지속성

### ▶ BASE (NoSQL)

* **Basically Available**: 항상 사용 가능
* **Soft State**: 상태가 변할 수 있음
* **Eventually Consistent**: 최종적 일관성

---

## 4. NoSQL 유형별 분류

### 1️⃣ Key-Value Store

* 구조: Key = Value
* 초고속 읽기/쓰기
* **예**: Redis, DynamoDB

### 2️⃣ Column Family Store

* 열 단위 저장
* 대규모 분산 처리
* **예**: Cassandra, HBase

### 3️⃣ Document Store

* JSON/BSON 문서
* 스키마 유연
* **예**: MongoDB, CouchDB

### 4️⃣ Graph Store

* 노드/엣지 기반
* 관계 탐색 최적화
* **예**: Neo4j, Amazon Neptune

---

## 5. CAP 이론

> 분산 시스템은 **Consistency, Availability, Partition Tolerance** 중
> 동시에 **2가지만 만족 가능**

| 요소                  | 설명           |
| ------------------- | ------------ |
| Consistency         | 모든 노드 데이터 동일 |
| Availability        | 항상 응답 제공     |
| Partition Tolerance | 네트워크 분할 허용   |

### 조합 예시

* **CP**: HBase, MongoDB
* **AP**: Cassandra, DynamoDB
* **CA**: 전통적 RDBMS (단일 시스템)

---

## 6. 언제 어떤 DB를 쓰는가?

* **정합성 중요** → RDBMS
* **대용량 로그/이벤트** → NoSQL (AP)
* **실시간 캐시/세션** → Redis
* **관계 분석** → Graph DB

---


