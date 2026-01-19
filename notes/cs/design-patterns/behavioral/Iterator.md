# Iterator Pattern (이터레이터 패턴)

Iterator를 사용하여 컬렉션의 내부 구조를 노출하지 않고  
요소들에 순차적으로 접근할 수 있도록 하는 **행위(Behavioral) 디자인 패턴**이다.

## 핵심 개념
- 컬렉션 내부 구현과 순회 로직을 분리
- 자료구조 종류와 무관하게 동일한 방식으로 순회 가능
- 결합도 감소, 확장성 증가

## Iterator Protocol
- **Iterable**: 반복 가능한 객체
- 배열, 리스트, 트리 등 다양한 자료구조를 일반화한 개념

## 장점
- 컬렉션 구현 변경에 영향 없음
- 단일 책임 원칙(SRP) 만족

## 사용 예
- Java: `Iterator`, `Iterable`
- Python: `__iter__`, `__next__`
