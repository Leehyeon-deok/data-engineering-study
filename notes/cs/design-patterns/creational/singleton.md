# Singleton Pattern

## 정의
- 하나의 클래스에 오직 하나의 인스턴스만 생성

## 사용 예
- DB 커넥션
- Logger
- 설정 객체

## 장점
- 인스턴스 생성 비용 감소
- 자원 공유

## 단점
- 강한 결합
- TDD에 불리
- 테스트 독립성 깨짐

## 3대 원칙
1. 생성자 private
2. static instance 하나
3. getInstance() 제공

## 멀티스레드 문제
- 동시 생성 위험

## 해결 방법
- 정적 내부 클래스 방식
- Lazy Loading
- JVM 클래스 로딩 보장

## 관련 개념
- == vs equals
- DI로 결합도 완화
