# MVC Pattern (Model - View - Controller)

애플리케이션을 역할별로 분리하는 대표적인 아키텍처 패턴이다.

## Model
- 데이터 및 상태 관리
- DB, 상수, 비즈니스 로직 포함

## View
- 사용자 인터페이스(UI)
- 데이터를 직접 저장하지 않음

## Controller
- Model과 View 연결
- 이벤트 처리 및 흐름 제어

## 장단점
### 장점
- 재사용성, 확장성 우수

### 단점
- 규모 증가 시 Model-View 관계 복잡

## 사용 예
- Spring Web MVC
