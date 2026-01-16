
---

# 📄 `cs/design-patterns/behavioral/strategy.md`

```md
# Strategy Pattern (전략 패턴)

## 정의
전략 패턴은 행위를 캡슐화하여
런타임에 행위를 교체할 수 있도록 만든 패턴이다.

## 목적
- 조건문(if/switch) 제거
- 행위 변경 시 코드 수정 최소화
- OCP(Open-Closed Principle) 준수

## 구성 요소
- Strategy (전략 인터페이스)
- ConcreteStrategy (구현 전략)
- Context (전략을 사용하는 객체)

## 예시 개념
- 결제 방식 선택 (카드 / 네이버페이 / 카카오페이)
- 정렬 알고리즘 선택
- 압축 방식 선택

## 구조 예시
```java
interface PaymentStrategy {
    void pay();
}

class KakaoPay implements PaymentStrategy {
    public void pay() {}
}

class Context {
    private PaymentStrategy strategy;
    Context(PaymentStrategy strategy) {
        this.strategy = strategy;
    }
}
장점
행위 확장이 쉬움

코드 중복 제거

테스트 용이

단점
클래스 수 증가

전략 선택 로직 필요

DI와의 관계
전략 객체를 외부에서 주입

DI와 함께 사용 시 효과 극대화

사용 사례
결제 시스템

게임 캐릭터 행동

로그 처리 방식