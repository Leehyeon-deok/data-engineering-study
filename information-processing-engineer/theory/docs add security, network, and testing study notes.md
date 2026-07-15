# 📚 정보처리기사 핵심 개념 정리 (Visitor · 오류제어 · HDLC · 암호화 · 접근제어 · ATM · NAT · Python · 테스트)

---

# 1. Visitor Pattern (방문자 패턴)

객체 구조는 변경하지 않고 새로운 기능(연산)을 추가하는 행동(Behavioral) 디자인 패턴이다.

## 특징

- 객체 구조 변경 없이 기능 추가
- 객체와 기능을 분리
- 새로운 기능 추가가 쉬움
- 합성(Composite) 구조에서 자주 사용

## 구성 요소

- Element
- Visitor
- Concrete Visitor
- Object Structure

### 핵심 메서드

```
accept()

visit()
```

### 장점

- 기능 추가가 쉽다.
- 기존 코드 변경이 적다.

### 단점

- 새로운 객체(Element) 추가 시 Visitor 수정 필요

### 시험 암기

> 객체는 그대로, 기능만 Visitor가 방문하여 수행

---

# 2. 오류 제어(Error Control)

데이터 전송 시 발생하는 오류를 검출하거나 정정하는 기술이다.

---

## Hamming Code

1비트 오류를 정정할 수 있는 오류 정정부호이다.

### 특징

- Bell 연구소의 Hamming이 개발
- 선형 블록 부호
- 1비트 오류 정정 가능
- FEC 방식 사용

### 핵심 암기

```
Hamming

↓

1비트 오류 정정
```

---

## FEC (Forward Error Correction)

송신 측에서 오류 정정 정보를 함께 전송하여

수신 측이 스스로 오류를 수정하는 방식이다.

### 특징

- 재전송 불필요
- 위성통신 등에 사용
- Hamming Code 사용

### 핵심

```
송신

↓

오류 정정 정보 포함

↓

수신

↓

스스로 복구
```

---

## BEC (Backward Error Correction)

오류 발생 시 송신 측에 재전송을 요청하는 방식이다.

### 특징

- 재전송 필요
- ARQ 방식

### 오류 검출

- Parity
- CRC
- Checksum

### 핵심

```
오류

↓

재전송 요청
```

---

## Parity Bit

데이터 오류를 검사하기 위한 가장 간단한 방법이다.

### 종류

- Even Parity
- Odd Parity

### 특징

- 1비트 오류 검출
- 오류 정정 불가

---

## CRC (Cyclic Redundancy Check)

체크값을 계산하여 오류를 검출하는 방식이다.

### 특징

- 오류 검출 능력이 우수
- 네트워크에서 가장 많이 사용

---

# ⭐ 오류 제어 비교

| 방식 | 특징 |
|------|------|
| Hamming | 1비트 오류 정정 |
| FEC | 스스로 오류 수정 |
| BEC | 재전송 요청 |
| Parity | 오류 검출 |
| CRC | 체크값 계산 후 오류 검출 |

---

# 3. HDLC (High-level Data Link Control)

비트 중심(Bit-Oriented)의 데이터 링크 제어 프로토콜이다.

---

## I-Frame (Information)

정보(Data)를 전송하는 프레임

### 특징

- Seq 존재
- Next 존재
- P/F 존재

---

## S-Frame (Supervisory)

오류 제어 및 흐름 제어를 수행하는 프레임

### 특징

- Seq 없음
- Next 존재

---

## U-Frame (Unnumbered)

링크 설정 및 연결 제어

### 특징

- 순서번호 없음

---

# HDLC 동작 모드

## NRM (Normal Response Mode)

- 비대칭
- 주국 허가 후 종국 송신

---

## ARM (Asynchronous Response Mode)

- 비대칭
- 종국이 허가 없이 송신 가능

---

## ABM (Asynchronous Balanced Mode)

- 양쪽 모두 혼합국
- 가장 많이 사용

---

# 시험 암기

| 프레임 | 역할 |
|---------|------|
| I | 정보 |
| S | 감독 |
| U | 비번호 |

| 모드 | 특징 |
|------|------|
| NRM | 주국 허가 필요 |
| ARM | 허가 없이 응답 가능 |
| ABM | 양방향 통신 |

---

# 4. 암호화 알고리즘

## 대칭키(Symmetric Key)

암호화와 복호화에 같은 키를 사용한다.

### 종류

- DES
- AES
- ARIA
- SEED

### 특징

- 속도 빠름
- 키 관리 어려움

---

## 비대칭키(Asymmetric Key)

공개키와 개인키를 사용한다.

### 종류

- RSA
- ECC

### 특징

- 속도 느림
- 보안성 우수

---

# ⭐ 시험 암기

## 대칭키

```
DES

AES

ARIA

SEED
```

## 비대칭키

```
RSA

ECC
```

---

# 5. 접근 제어(Access Control)

---

## MAC (Mandatory Access Control)

강제 접근 제어

### 특징

- 규칙 기반
- 보안 등급 기준
- 관리자만 권한 변경

---

## DAC (Discretionary Access Control)

임의 접근 제어

### 특징

- 사용자 신분 기반
- 소유자가 권한 부여

---

## RBAC (Role Based Access Control)

역할 기반 접근 제어

### 특징

- 역할(Role) 기반
- 기업에서 가장 많이 사용

---

# 시험 암기

| 방식 | 기준 |
|------|------|
| MAC | 등급 |
| DAC | 사용자 |
| RBAC | 역할 |

---

# 6. ATM (Asynchronous Transfer Mode)

고정 길이 셀(Cell)을 사용하는 고속 패킷 교환 방식이다.

## 특징

- 셀 길이 53Byte
- 연결 지향
- 가상 채널 기반
- 통계적 다중화

### 핵심 암기

```
ATM

↓

53Byte

↓

Cell
```

---

# 7. NAT (Network Address Translation)

사설 IP를 공인 IP로 변환하는 기술이다.

## 특징

- IP 부족 해결
- 보안성 향상
- 공유기에서 사용

### 시험 암기

```
Private IP

↓

NAT

↓

Public IP
```

---

# 8. Python split()

문자열을 구분자로 나누는 함수이다.

예)

```python
num1, num2 = input().split()
```

입력

```
2 3
```

결과

```
num1 = "2"

num2 = "3"
```

---

# 9. Equivalence Partitioning (동등 분할 기법)

입력값을 동일하게 처리되는 그룹(동등 클래스)으로 나누어 대표값만 테스트하는 기법이다.

화이트박스가 아닌 **블랙박스 테스트 기법**이다.

## 특징

- 대표값만 테스트
- 테스트 케이스 감소
- 효율적인 테스트 가능
- 경계값 분석(BVA)과 함께 사용

---

## 예시

입력 범위

```
1~100
```

동등 클래스

```
0 이하

1~100

101 이상
```

대표값

```
-1

50

101
```

세 개만 테스트하면 된다.

---

# 경계값 분석(BVA)

경계에서 오류가 많이 발생하므로

경계값을 집중적으로 테스트하는 기법이다.

예)

```
1~100
```

테스트

```
0

1

2

99

100

101
```

---

# 동등 분할 vs 경계값 분석

| 구분 | 동등 분할 | 경계값 분석 |
|------|-----------|-------------|
| 기준 | 대표값 | 경계값 |
| 목적 | 테스트 수 감소 | 경계 오류 발견 |
| 분류 | 블랙박스 테스트 | 블랙박스 테스트 |

---

# ⭐ 시험 암기 포인트

| 용어 | 핵심 |
|------|------|
| Visitor | 객체 구조 변경 없이 기능 추가 |
| Hamming | 1비트 오류 정정 |
| FEC | 오류 정정 정보 포함 |
| BEC | 재전송 요청 |
| Parity | 오류 검출 |
| CRC | 체크값 기반 오류 검출 |
| I-Frame | 정보 프레임 |
| S-Frame | 감독 프레임 |
| U-Frame | 비번호 프레임 |
| ABM | 양방향 통신 |
| ARM | 허가 없이 응답 가능 |
| NRM | 주국 허가 필요 |
| DES | 대칭키 |
| AES | 대칭키 |
| ARIA | 대칭키 |
| SEED | 대칭키 |
| RSA | 비대칭키 |
| ECC | 비대칭키 |
| MAC | 등급 기반 접근 제어 |
| DAC | 사용자 기반 접근 제어 |
| RBAC | 역할 기반 접근 제어 |
| ATM | 53Byte Cell |
| NAT | 사설 IP → 공인 IP |
| split() | 문자열 분리 |
| Equivalence Partitioning | 대표값 테스트 |
| Boundary Value Analysis | 경계값 테스트 |