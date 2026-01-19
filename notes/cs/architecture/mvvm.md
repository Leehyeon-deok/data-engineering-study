# MVVM Pattern (Model - View - ViewModel)

MVC에서 Controller 대신 ViewModel을 사용하는 아키텍처 패턴이다.

## ViewModel
- View를 추상화한 계층
- UI 로직과 상태 관리 담당

## 핵심 개념
- Data Binding: View ↔ ViewModel 자동 동기화
- Command: 여러 동작을 하나의 액션으로 처리

## 장점
- 양방향 데이터 바인딩
- UI 재사용성
- 단위 테스트 용이

## 대표 프레임워크
- Vue.js
  - 컴포넌트 기반 UI
  - 값 변경 시 화면 자동 갱신
