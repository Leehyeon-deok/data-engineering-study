📌 CS & 보안 핵심 개념 정리 (정보처리기사 실기 대비)
🧩 1. 객체지향 / Java
✔ 클래스 변수 값 대입
매개변수 값을 클래스 변수에 대입할 때
👉 this.변수명 = 변수명 사용
class Test {
    int b;

    Test(int b) {
        this.b = b;  // 매개변수 b → 클래스 변수 b에 대입
    }
}
✔ 인터페이스 구현
implements 키워드 사용
class A implements B {
    // B 인터페이스 구현
}
🌐 2. 네트워크 / 프로토콜
✔ 프로토콜의 기본 요소
구문(Syntax) : 데이터 형식
의미(Semantics) : 데이터 의미
타이밍(Timing) : 전송 시기 및 속도
🔐 3. 보안 공격 기법
✔ 워터링 홀 (Watering Hole)
특정 대상이 자주 방문하는 사이트에 악성코드 삽입
방문 시 자동 감염 유도
✔ 루트킷 (Rootkit)
침입 사실 숨김 + 관리자 권한 획득
백도어, 트로이목마 설치
로그 삭제 등 흔적 은폐
✔ 크라임웨어 (Crimeware)
범죄 목적 악성 프로그램
구성: 키로거, 스파이웨어, 브라우저 하이재킹 등
정보 탈취 및 공격 수행
✔ 스니핑 (Sniffing)
네트워크 패킷 도청
수동적 공격 (직접 공격 X)
✔ 스푸핑 (Spoofing)
신뢰된 사용자로 위장
IP / MAC / 이메일 주소 변조
⚠️ 4. 네트워크 공격 유형
✔ ICMP 공격 (Ping of Death)
비정상적으로 큰 ICMP 패킷 전송
시스템 과부하 유발
✔ SYN 플러딩 (SYN Flooding)
TCP 3-way handshake 악용
SYN만 보내고 ACK 미응답
서버 자원 고갈 → 서비스 불가
✔ 스머프 공격 (Smurf Attack)
출발지 IP를 피해자로 위조
브로드캐스트로 ICMP 요청
응답 트래픽 폭증 → 마비
🌍 5. 웹 기술
✔ HTML
웹 문서의 구조와 의미 정의
✔ CSS
웹 페이지 스타일 (디자인)
✔ XML
HTML의 확장성 한계 보완
사용자 정의 태그 가능
⚙️ 6. CPU 스케줄링
✔ SRT (Shortest Remaining Time)
남은 실행 시간이 가장 짧은 프로세스 우선 실행
선점형 스케줄링 방식
🧠 시험 핵심 포인트 요약
this.변수 = 변수 👉 객체 변수 초기화
스니핑 = 수동 공격
스푸핑 = 위장 공격
SYN Flooding = ACK 안 보내고 자원 고갈
스머프 = IP 위조 + 브로드캐스트
SRT = 남은 시간 기준 최단 작업 우선