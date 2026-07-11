# 📚 Information Processing Engineer - Core Concepts (2)

---

# 1. UX & UI

| 구분 | 설명 |
|------|------|
| **UX (User Experience)** | 사람의 감정이나 경험을 나타내는 개념 |
| **UI (User Interface)** | 사용자와 시스템이 상호작용하는 인터페이스 (예: CLI, GUI) |

### 💡 암기법
- **UX = 사용자의 경험**
- **UI = 사용자가 보는 화면**

---

# 2. AES (Advanced Encryption Standard)

### 특징
- 미국 **NIST**가 DES를 대체하여 제정
- **대칭키 암호화 방식**
- 블록 크기 : **128bit**
- 키 길이 : **128 / 192 / 256bit**

### 💡 암기법
> **AES = DES의 업그레이드 버전**

---

# 3. DES (Data Encryption Standard)

### 특징
- 미국 **NBS(현재 NIST)** 국가 표준 암호
- **대칭키 암호화**
- 64bit 평문 → 64bit 암호문
- 키 길이 : **64bit (실제 사용 56bit)**

### AES vs DES

| DES | AES |
|------|------|
| 64bit 블록 | 128bit 블록 |
| 실제 키 56bit | 128/192/256bit |
| 보안 취약 | 현재 가장 많이 사용 |

### 💡 암기법
> **DES → 오래됨 → AES가 대체**

---

# 4. 병행 제어 (Concurrency Control)

### 정의
동시에 수행되는 트랜잭션의 데이터 일관성을 유지하는 기법

### 종류

| 기법 | 설명 |
|------|------|
| **로킹(Locking)** | 연산이 끝날 때까지 다른 트랜잭션 접근 금지 |
| **타임스탬프(Time Stamp)** | 시간 순서대로 수행 |
| **최적 병행 수행(낙관적 기법)** | 충돌이 적다고 가정하고 수행 후 검증 |
| **다중 버전(MVCC)** | 데이터 버전을 여러 개 관리 |

### 💡 암기법
> **로·타·최·다**

---

# 5. 럼바우(Rumbaugh) 객체지향 분석

| 모델링 | 설명 | 예시 |
|---------|------|------|
| **Object Modeling** | 객체와 객체 관계 | ERD |
| **Dynamic Modeling** | 시간에 따른 변화 | 상태도(State Diagram) |
| **Functional Modeling** | 데이터 처리 흐름 | DFD |

### 절차

> **객체 → 동적 → 기능**

### 💡 암기법

- Object → 객체
- Dynamic → 시간 변화
- Functional → 기능(DFD)

---

# 6. AAA (보안)

| 용어 | 설명 |
|------|------|
| **Authentication** | 인증 (신분 확인) |
| **Authorization** | 인가 (권한 확인) |
| **Accounting** | 계정/감사 (사용 기록 관리) |

### 💡 암기법

> **인증 → 인가 → 기록**

---

# 7. OSI 7 Layer

| 계층 | 역할 |
|------|------|
| **7 응용(Application)** | 사용자 서비스 |
| **6 표현(Presentation)** | 인코딩 / 디코딩 |
| **5 세션(Session)** | 연결 관리 |
| **4 전송(Transport)** | TCP, 오류 제어 |
| **3 네트워크(Network)** | IP, 경로 선택 |
| **2 데이터링크(Data Link)** | MAC 주소 |
| **1 물리(Physical)** | 전기 신호 |

### 장비

- Physical → Hub, Repeater, Cable
- Data Link → Switch
- Network → Router

### 💡 암기법

> **응표세전네데물**

---

# 8. static

### static 메서드

객체 생성 없이 호출 가능

```java
Test.check();
```

### 일반 메서드

객체 생성 후 호출

```java
Test t = new Test();
t.check();
```

### 💡 암기법

> **객체 없이 호출 = static**

---

# 9. XOR (^)

### XOR

서로 다르면 true

| A | B | A ^ B |
|---|---|--------|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

### 💡 암기법

> **다르면 True**

---

# 10. 클래스 다이어그램

### 특징

- 클래스
- 속성(Attribute)
- 메서드(Method)

### 용도

- 객체 구조 표현
- 소프트웨어 설계
- 구현 설명

### 💡 암기법

> **클래스 = 속성 + 메서드**

---

# 11. 파일 접근 방식

| 방식 | 설명 |
|------|------|
| **순차 접근(Sequential Access)** | 처음부터 순서대로 접근 |
| **인덱스 접근(Index Access)** | 인덱스를 이용해 빠르게 접근 |
| **해싱 접근(Hash Access)** | 해시 함수를 이용하여 직접 접근 |

### 💡 암기법

> **순 → 인 → 해**

- 순차 = 처음부터
- 인덱스 = 목차 보고 찾기
- 해싱 = 주소 바로 찾기

---

# ⭐ 시험 암기 포인트

- UX = 사용자 경험
- UI = 사용자 인터페이스
- AES = DES 대체, 128bit 블록
- DES = 64bit 블록, 실제 키 56bit
- 병행 제어 = **로·타·최·다**
- 럼바우 = **객체 → 동적 → 기능**
- AAA = **Authentication → Authorization → Accounting**
- OSI = **응표세전네데물**
- static = **객체 없이 호출**
- XOR(^) = **다르면 True**
- 클래스 다이어그램 = **속성 + 메서드**
- 파일 구조 = **순차 → 인덱스 → 해싱**