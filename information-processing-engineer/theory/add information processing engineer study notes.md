# 📚 정보처리기사 실기 핵심 암기 노트

---

# 1. AJAX (Asynchronous JavaScript and XML)

## 정의
- **XMLHttpRequest 객체**를 이용한 **비동기 통신 기술**
- **전체 페이지를 새로고침하지 않고** 필요한 부분만 데이터를 갱신
- 웹 페이지와 사용자가 **동적으로 상호작용** 가능

### 핵심 키워드
- 비동기 통신
- XMLHttpRequest
- 부분 갱신
- JavaScript

---

# 2. 정적 분석 도구 (Static Analysis Tool)

## 정의
프로그램을 **실행하지 않고** 소스 코드를 분석하여 다음을 검사하는 도구

- 코딩 표준
- 코딩 스타일
- 코드 복잡도
- 잠재적 결함(Bug)

### 암기
> **실행 안 함 = 정적 분석**

---

# 3. Android

## 정의
- Linux 기반 모바일 운영체제
- Google에서 개발
- Java / Kotlin 지원
- 모바일 앱 개발 플랫폼

### 핵심 키워드
- Linux
- Java
- Kotlin
- 모바일 운영체제

---

# 4. INDEX 생성

```sql
CREATE INDEX IDX_NAME
ON 학생(NAME);
```

### 문법

```sql
CREATE INDEX 인덱스명
ON 테이블명(컬럼명);
```

---

# 5. 형상관리(Configuration Management)

## 정의

소프트웨어 개발 과정에서 **변경 사항을 체계적으로 관리하는 기법**

### 대표 도구

- Git
- SVN
- CVS

### 암기

> Git = 형상관리

---

# 6. 오버로딩(Overloading) vs 오버라이딩(Overriding)

## 오버로딩

- 같은 이름
- **매개변수 다름**
- **컴파일 시 결정**

### 암기

> 오버로딩 = 컴파일 + 매개변수

---

## 오버라이딩

- 부모 메서드 재정의
- **실제 객체 기준 실행**
- **런타임 시 결정**

### 암기

> 오버라이딩 = 런타임 + 객체

---

## 가장 중요한 한 줄

### 오버로딩

> **어떤 메서드를 호출할지 결정**

### 오버라이딩

> **결정된 메서드를 어느 클래스의 구현으로 실행할지 결정**

---

# 7. HDLC (High-Level Data Link Control)

## 한 줄 정의

> **비트 중심(Bit-Oriented) 데이터 링크 제어 프로토콜**

프레임 단위로 데이터를 전송하며

- 오류 제어
- 흐름 제어

를 제공한다.

### 암기

```
HDLC = 비트 + 프레임 + 오류 + 흐름
```

---

# 8. HDLC 프레임

## I Frame (Information)

- 실제 데이터 전송
- 순서 번호 포함

### 암기

```
I = Information = 데이터
```

---

## S Frame (Supervisory)

- 오류 제어
- 흐름 제어

대표 명령

- RR : Receive Ready (계속 보내)
- RNR : Receive Not Ready (잠깐 멈춰)
- REJ : Reject (다시 보내)
- SREJ : Selective Reject (해당 프레임만 다시)

### 암기

```
S = Supervisory = 감독
→ 오류 제어 + 흐름 제어
```

---

## U Frame (Unnumbered)

- 링크 설정
- 링크 해제
- 모드 설정

### 암기

```
U = Unnumbered = 번호 없는 제어
```

---

# 프레임 한 줄 암기

```
I = 데이터

S = 감독(오류·흐름)

U = 제어
```

---

# 9. HDLC 동작 모드

## NRM (Normal Response Mode)

주국의 허가를 받아야 종국이 송신

```
주국
 ↓ 허가
종국 송신
```

### 암기

```
N = Need Permission
(허가 필요)
```

---

## ARM (Asynchronous Response Mode)

종국이 허가 없이 응답 가능

```
주국

종국 → 바로 송신
```

### 암기

```
A = Allow
(허가 없이 가능)
```

---

## ABM (Asynchronous Balanced Mode)

양쪽이 동등한 위치

```
A ↔ B
```

### 암기

```
B = Balanced
(균형)
```

---

# 모드 한 줄 암기

```
NRM = 허가받고

ARM = 허가 없이

ABM = 서로 동등
```

---

# 10. Flag

항상

```
01111110
```

### 암기

```
HDLC Flag = 01111110
```

---

# 11. Bit Stuffing

데이터 안에

```
11111
```

이 나오면

```
0
```

을 하나 삽입한다.

### 이유

Flag

```
01111110
```

와 구분하기 위해

### 암기

```
11111 → 0 삽입
```

---

# 시험 직전 30초 암기

## 오버로딩 / 오버라이딩

```
오버로딩 = 컴파일 + 매개변수

오버라이딩 = 런타임 + 객체
```

---

## HDLC

```
HDLC = 비트 + 프레임 + 오류 + 흐름

I = 데이터

S = 감독(오류·흐름)

U = 제어

NRM = 허가받고

ARM = 허가 없이

ABM = 서로 동등

Flag = 01111110

11111 → 0 삽입(Bit Stuffing)
```

---

## 자주 출제되는 한 줄 암기

- AJAX → **XMLHttpRequest 기반 비동기 통신**
- 정적 분석 → **실행하지 않고 코드 분석**
- Android → **Linux 기반 모바일 운영체제**
- 형상관리 → **Git, SVN, CVS**
- 오버로딩 → **컴파일 + 매개변수**
- 오버라이딩 → **런타임 + 객체**
- HDLC → **비트 중심 데이터 링크 프로토콜**