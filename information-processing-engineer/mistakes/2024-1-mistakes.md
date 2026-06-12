# Information Processing Engineer - Mistakes Note

## Java Singleton Pattern

### 핵심

* `new`가 있으면 새로운 객체 생성
* Singleton 패턴에서는 `new`를 사용하지 않고 `getInstance()`를 통해 기존 객체 반환
* 객체를 1개만 생성하여 공유

```java
Singleton a = Singleton.getInstance();
Singleton b = Singleton.getInstance();

System.out.println(a == b); // true
```

---

## 조건식 판별

### C 언어

* 0 → False
* 0이 아닌 값 → True

```c
if(-1) // 참
```

### Java

* 조건식에는 반드시 boolean 값만 사용 가능

```java
if(-1) // 컴파일 오류
```

### Python

* 0만 False
* 나머지 숫자는 True

```python
if -1:
    print("True")
```

---

## OSPF (Open Shortest Path First)

### 정의

* 대표적인 링크 상태(Link State) 라우팅 프로토콜
* 내부 게이트웨이 프로토콜(IGP)

### 특징

* 링크 상태 정보를 기반으로 경로 계산
* 다익스트라(Dijkstra) 알고리즘 사용
* 최단 경로 계산
* 빠른 수렴
* 대규모 네트워크에 적합

### 동작 과정

1. 주변 링크 상태 수집
2. LSA(Link State Advertisement) 전송
3. LSDB(Link State Database) 생성
4. SPF(Shortest Path First, 다익스트라) 수행
5. 최적 경로 계산

### LSDB

* 모든 라우터가 동일한 네트워크 지도를 보유

### OSPF vs RIP

| 구분    | OSPF  | RIP   |
| ----- | ----- | ----- |
| 방식    | 링크 상태 | 거리 벡터 |
| 알고리즘  | 다익스트라 | 벨만-포드 |
| 규모    | 대규모   | 소규모   |
| 수렴 속도 | 빠름    | 느림    |
| 홉 제한  | 없음    | 15 홉  |
| 업데이트  | 변경 시  | 주기적   |

### 암기

* OSPF = 링크 상태 + 다익스트라
* RIP = 거리 벡터 + 벨만포드 + 15홉 제한

---

## JOIN 정리

### 동등 조인 (Equi Join)

* '=' 조건 사용

```sql
A.ID = B.ID
```

### 세타 조인 (Theta Join)

* 비교 연산자 사용

```sql
=, >, <, >=, <=, <>
```

### 비등가 조인 (Non-Equi Join)

* 범위 조건 사용

```sql
A.SALARY BETWEEN B.MIN AND B.MAX
```

### INNER JOIN

* 양쪽 테이블에 모두 존재하는 데이터만 조회

### OUTER JOIN

* 매칭되지 않는 데이터도 포함
* NULL 발생 가능

### NATURAL JOIN

* 동일한 이름의 컬럼 자동 연결

### CROSS JOIN

* 카티션 곱
* 모든 경우의 수 생성

### SELF JOIN

* 자기 자신과 조인

### 암기

* 동등 조인 = '='
* 세타 조인 = 비교 연산자
* 비등가 조인 = 범위 조건

---

## 페이지 교체 알고리즘

### LRU (Least Recently Used)

* 가장 오랫동안 사용되지 않은 페이지 제거

예시

최근 사용 순서

D → C → B → A

교체 대상 = A

### LFU (Least Frequently Used)

* 사용 빈도가 가장 적은 페이지 제거

예시

A : 10회
B : 3회
C : 1회

교체 대상 = C

### FIFO (First In First Out)

* 가장 먼저 들어온 페이지 제거


### 암기

* LRU = 오래 안 쓴 것 제거
* LFU = 적게 사용한 것 제거
* FIFO = 먼저 들어온 것 제거
* OPT = 미래를 알고 최적 선택
## 페이지 교체 알고리즘

### FIFO (First In First Out)

- 가장 먼저 들어온 페이지 제거

예시

A → B → C → D

교체 대상 = A

### LRU (Least Recently Used)

- 가장 오랫동안 사용되지 않은 페이지 제거

예시

최근 사용 순서

D → C → B → A

교체 대상 = A

### LFU (Least Frequently Used)

- 사용 빈도가 가장 적은 페이지 제거

예시

A : 10회
B : 3회
C : 1회

교체 대상 = C

### 암기

- FIFO = 먼저 들어온 것 제거
- LRU = 오래 안 쓴 것 제거
- LFU = 적게 사용한 것 제거
---

## 시험에서 자주 헷갈리는 내용

### Singleton

* new 사용 → 새 객체 생성
* getInstance() → 기존 객체 반환

### 조건식

* C : 0만 거짓
* Java : boolean만 가능
* Python : 0만 거짓

### OSPF

* 링크 상태
* 다익스트라
* LSDB 사용

### RIP

* 거리 벡터
* 벨만포드
* 15홉 제한

### LRU vs LFU

* LRU = 최근 사용 여부
* LFU = 사용 빈도

### JOIN

* 동등 조인 = '='
* 세타 조인 = 비교 연산자
* 비등가 조인 = 범위 조건
