# 📚 정보처리기사 핵심 개념 정리 (RAID · REDO/UNDO · SOLID · 관계대수 등)

---

# 1. RAID (Redundant Array of Independent Disks)

여러 개의 하드디스크를 하나의 논리적 디스크처럼 사용하여 **성능 향상** 또는 **데이터 안정성**을 높이는 기술이다.

## RAID 종류

| RAID | 방식 | 장점 | 단점 |
|------|------|------|------|
| RAID 0 | Striping | 읽기/쓰기 속도 향상 | 장애 시 모든 데이터 손실 |
| RAID 1 | Mirroring | 높은 안정성 | 저장 공간 절반 사용 |
| RAID 5 | Striping + Parity | 성능과 안정성 균형 | 패리티 계산으로 쓰기 성능 감소 |
| RAID 6 | RAID5 + 이중 패리티 | 디스크 2개까지 장애 허용 | RAID5보다 느림 |
| RAID 10 | RAID1 + RAID0 | 최고 수준의 성능과 안정성 | 비용이 높음 |

### 핵심 암기

- RAID 0 → 속도
- RAID 1 → 복제(Mirroring)
- RAID 5 → 패리티 1개
- RAID 6 → 패리티 2개
- RAID 10 → 성능 + 안정성

---

# 2. REDO / UNDO

데이터베이스 장애 발생 시 트랜잭션을 복구하는 방법이다.

## REDO

- Commit 완료된 트랜잭션을 다시 수행
- 데이터 손실 방지

예시

```
Commit 완료
↓
장애 발생
↓
REDO 수행
```

## UNDO

- Commit되지 않은 작업을 취소
- 데이터 일관성 유지

예시

```
작업 중
↓
장애 발생
↓
UNDO 수행
```

### 핵심 암기

- REDO = 다시 실행
- UNDO = 되돌리기

---

# 3. 무결성(Integrity)

데이터가 정확하고 일관성을 유지하도록 하는 제약 조건이다.

## 개체 무결성(Entity Integrity)

- 기본키(Primary Key)는 NULL 불가
- 기본키는 중복 불가

## 참조 무결성(Referential Integrity)

- 외래키(Foreign Key)는 존재하는 기본키만 참조 가능

예시

학생

| 학번 |
|------|
|1001|

수강신청

| 학번 |
|------|
|1001| → 가능

|1002| → 불가능(학생 테이블에 없음)

---

# 4. TKIP (Temporal Key Integrity Protocol)

WEP의 보안 취약점을 개선한 무선 암호화 프로토콜이다.

## 특징

- WPA에서 사용
- 암호키를 계속 변경
- MIC(Message Integrity Check) 제공
- WEP보다 안전

### 핵심 암기

WEP → TKIP → WPA

---

# 5. SOLID

객체지향 설계의 5대 원칙이다.

## S : Single Responsibility Principle

하나의 클래스는 하나의 책임만 가진다.

## O : Open Closed Principle

확장에는 열려 있고 수정에는 닫혀 있다.

## L : Liskov Substitution Principle

자식 클래스는 부모 클래스를 대체할 수 있어야 한다.

## I : Interface Segregation Principle

인터페이스는 필요한 기능만 제공하도록 분리한다.

## D : Dependency Inversion Principle

구체 클래스가 아닌 추상화에 의존한다.

### 핵심 암기

S O L I D

- Single Responsibility
- Open Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

---

# 6. 관계대수(Relational Algebra)

관계형 데이터베이스에서 사용하는 **절차적 질의 언어**이다.

즉, **어떻게(How)** 데이터를 가져올지 기술한다.

## 주요 연산

| 연산 | 의미 |
|------|------|
| σ | Selection(행 선택) |
| π | Projection(열 선택) |
| ∪ | 합집합 |
| - | 차집합 |
| × | Cartesian Product |
| ⋈ | Join |
| ÷ | Division |

---

# 7. 관계해석(Relational Calculus)

관계형 데이터베이스의 **비절차적 질의 언어**이다.

즉, **무엇(What)** 을 원하는지만 기술한다.

## 종류

- Tuple Relational Calculus(TRC)
- Domain Relational Calculus(DRC)

### 관계대수와 비교

| 관계대수 | 관계해석 |
|----------|----------|
| 절차적 | 비절차적 |
| How | What |

---

# 8. Regression(회귀)

연속적인 값을 예측하는 머신러닝 기법이다.

## 예시

- 집값 예측
- 매출 예측
- 온도 예측

## 종류

- 선형 회귀
- 다중 회귀
- 다항 회귀

※ 로지스틱 회귀는 이름은 회귀지만 **분류(Classification)** 에 사용된다.

---

# 9. SQL의 ALL / ANY

## ALL

모든 값을 만족해야 한다.

```sql
SELECT *
FROM EMP
WHERE SAL > ALL
(SELECT SAL FROM EMP WHERE DEPTNO=30);
```

→ 30번 부서 **모든 직원보다** 급여가 높아야 한다.

---

## ANY

하나 이상의 값만 만족하면 된다.

```sql
SELECT *
FROM EMP
WHERE SAL > ANY
(SELECT SAL FROM EMP WHERE DEPTNO=30);
```

→ 30번 부서 직원 중 **한 명보다만** 급여가 높으면 된다.

### 핵심 암기

- ALL = 모두
- ANY = 하나라도

---

# 10. 함수 종속(Function Dependency)

어떤 속성의 값이 다른 속성의 값을 결정하는 관계이다.

```
A → B
```

A가 결정되면 B도 결정된다.

---

## 완전 함수 종속

복합키 전체가 있어야 다른 속성을 결정할 수 있다.

예)

```
(학번, 과목) → 성적
```

학번만으로는 성적을 알 수 없고

과목만으로도 알 수 없다.

→ 완전 함수 종속

---

## 부분 함수 종속

복합키 일부만으로 결정 가능하다.

예)

```
(학번, 과목) → 학생이름
```

학생이름은 학번만 알면 결정 가능하다.

→ 부분 함수 종속

---

# 11. IGP / EGP

라우팅 프로토콜의 분류이다.

## IGP (Interior Gateway Protocol)

하나의 AS 내부에서 사용하는 라우팅 프로토콜

대표

- RIP
- OSPF

---

## EGP (Exterior Gateway Protocol)

AS와 AS 사이에서 사용하는 라우팅 프로토콜

대표

- BGP

### 핵심 암기

- IGP = 내부
- EGP = 외부

---

# 12. RIP (Routing Information Protocol)

거리 벡터(Distance Vector) 기반 라우팅 프로토콜이다.

## 특징

- Bellman-Ford 알고리즘 사용
- Hop Count 사용
- 최대 15 Hop
- 설정이 간단

단점

- 대규모 네트워크에 부적합

---

# 13. OSPF (Open Shortest Path First)

링크 상태(Link State) 기반 라우팅 프로토콜이다.

## 특징

- Dijkstra 알고리즘 사용
- 빠른 수렴
- 대규모 네트워크 적합

---

# 14. BGP (Border Gateway Protocol)

AS와 AS 사이를 연결하는 라우팅 프로토콜이다.

## 특징

- 인터넷 백본에서 사용
- Path Vector 방식
- TCP 기반

### 핵심 암기

인터넷 = BGP

---

# 15. HTTP (HyperText Transfer Protocol)

웹 브라우저와 서버가 데이터를 주고받는 프로토콜이다.

## 특징

- Stateless
- Request / Response 방식
- 기본 포트 : 80

## HTTPS

- SSL/TLS 적용
- 암호화 통신
- 기본 포트 : 443

---

# 16. HTML (HyperText Markup Language)

웹 페이지의 구조를 만드는 마크업 언어이다.

## 특징

- 태그(Tag) 기반
- 웹 페이지 구조 작성
- CSS와 JavaScript와 함께 사용

예시

```html
<h1>Hello</h1>
<p>안녕하세요.</p>
```

---

# ⭐ 한눈에 암기

| 개념 | 핵심 |
|------|------|
| RAID 0 | 속도 |
| RAID 1 | 복제 |
| RAID 5 | 패리티 |
| RAID 6 | 이중 패리티 |
| RAID 10 | 성능 + 안정성 |
| REDO | 커밋된 내용 재실행 |
| UNDO | 미커밋 작업 취소 |
| TKIP | WEP 보안 강화 |
| SOLID | 객체지향 5원칙 |
| 관계대수 | 절차적(How) |
| 관계해석 | 비절차적(What) |
| Regression | 연속값 예측 |
| ALL | 모두 만족 |
| ANY | 하나 이상 만족 |
| 완전 함수 종속 | 복합키 전체 필요 |
| 부분 함수 종속 | 복합키 일부만 필요 |
| IGP | AS 내부 |
| EGP | AS 외부 |
| RIP | 거리 벡터 |
| OSPF | 링크 상태 |
| BGP | AS 간 라우팅 |
| HTTP | 웹 통신 |
| HTML | 웹 문서 작성 |