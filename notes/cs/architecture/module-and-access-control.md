# Module Pattern & 접근 제어 개념

## Revealing Module Pattern (노출 모듈 패턴)
즉시 실행 함수(IIFE)를 사용하여  
외부에 공개할 대상만 반환함으로써 캡슐화를 구현하는 패턴이다.

### 등장 배경
- JavaScript에는 기본 접근 제어자 없음
- 전역 스코프 오염 문제 발생

### 특징
- public / private 역할 분리
- 내부 구현 은닉

## IIFE (Immediately Invoked Function Expression)
함수를 정의하자마자 즉시 실행하는 표현식

### 사용 목적
- 초기화 코드 실행
- 전역 변수 충돌 방지
- 라이브러리 내부 스코프 보호

## 접근 제어자 정리

### public
- 클래스 내부 / 자식 클래스 / 외부 접근 가능

### protected
- 클래스 내부 / 자식 클래스 접근 가능
- 외부 접근 불가

### private
- 클래스 내부에서만 접근 가능
