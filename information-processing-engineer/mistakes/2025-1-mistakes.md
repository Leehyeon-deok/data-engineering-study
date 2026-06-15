📘 Information Processing Engineer - Mistakes Note
1. CRC (Cyclic Redundancy Check)
정의
CRC = Cyclic Redundancy Check (순환 중복 검사)
데이터 전송/저장 시 오류를 검출하는 방식
특징
오류 검출용
체크섬 사용
생성 다항식 사용
XOR 기반 나눗셈 수행
나머지를 CRC 값으로 사용
생성 다항식 예
x³ + x + 1
↓
1011
2. Java Exception 정리
예외	의미
ArithmeticException	0으로 나누기
ArrayIndexOutOfBoundsException	배열 범위 초과
NumberFormatException	문자열 → 숫자 변환 실패
NullPointerException	null 객체 사용
ClassCastException	잘못된 형변환
IOException	입출력 오류
FileNotFoundException	파일 없음
3. Java 생성자 실행 순서 (상속)
1. 부모 필드 초기화
2. 부모 생성자
3. 자식 필드 초기화
4. 자식 생성자
핵심
객체 생성 시 부모가 먼저 완성됨
super()가 자동 호출됨
4. Adapter Pattern (어댑터 패턴)
정의
서로 다른 인터페이스를 가진 클래스를 연결하여 함께 사용할 수 있게 하는 구조
특징
기존 클래스(Adaptee)를 수정하지 않음
원하는 인터페이스(Target)에 맞게 변환
Wrapper(감싸는 클래스) 방식
핵심 개념
기존 클래스 → Adapter → 원하는 인터페이스
5. Math 함수
Math.max()
Math.max(a, b)
a와 b 중 더 큰 값 반환
Math.min()
Math.min(a, b)
a와 b 중 더 작은 값 반환