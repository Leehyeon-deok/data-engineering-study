🌐 HTTP 1.0 ~ HTTP/3 & HTTPS 정리
1️⃣ HTTP/1.0
📌 특징

한 연결당 하나의 요청/응답

요청마다 TCP 3-Way Handshake 필요

연결 종료 후 다시 연결 → RTT 증가

📌 문제점

다수의 리소스(HTML, CSS, 이미지 등) 요청 시
👉 매번 TCP 연결 → 지연시간 증가

📌 보완 기법

이미지 스플리팅

코드 압축 (Minify)

이미지 Base64 인코딩

2️⃣ RTT (Round Trip Time)

패킷이 출발지 → 목적지 → 출발지로 돌아오는 시간

네트워크 지연을 판단하는 핵심 지표

3️⃣ HTTP/1.1
📌 개선점

Persistent Connection (Keep-Alive)

TCP 연결 1회 → 여러 요청/응답 처리

1.0에서도 존재했으나 1.1부터 기본 옵션으로 표준화

📌 문제점

문서 내 리소스 수만큼 요청 필요

요청이 순차 처리됨 → 대기시간 증가

📌 주요 단점

HOL Blocking

같은 큐에서 앞 요청이 지연되면 뒤 요청도 대기

무거운 헤더

쿠키, 메타데이터 많음

압축 미지원 → 오버헤드 큼

4️⃣ HOL Blocking

Head Of Line Blocking

앞선 패킷/요청 지연 → 뒤 요청 전체 지연

HTTP/1.1의 대표적 성능 저하 요인

5️⃣ HTTP/2

Google의 SPDY 프로토콜을 기반으로 발전

📌 핵심 특징

멀티플렉싱

헤더 압축 (HPACK)

서버 푸시

요청 우선순위 처리

🔹 멀티플렉싱 (Multiplexing)

하나의 TCP 연결에서 여러 스트림을 병렬 처리

특정 스트림 패킷 손실 → 해당 스트림만 영향

단일 연결로 동시 요청/응답 가능

👉 HTTP/1.1의 HOL Blocking 해결

🔹 헤더 압축

HPACK 압축 방식

허프만 코딩(Huffman Coding) 사용

빈도 높은 데이터 → 적은 비트

빈도 낮은 데이터 → 많은 비트

헤더 크기 감소 → 전송 효율 증가

🔹 서버 푸시 (Server Push)

HTTP/1.1: 클라이언트 요청 후 리소스 수신

HTTP/2: 요청 없이 서버가 필요한 리소스를 선제 전송

6️⃣ HTTPS

HTTP + SSL/TLS 계층

애플리케이션 계층과 전송 계층 사이에 신뢰 계층 추가

통신 내용 암호화

7️⃣ SSL / TLS
📌 목적

제3자의 도청, 변조 방지

인터셉터(중간자 공격) 차단

📌 사용 기술

인증 메커니즘

키 교환 알고리즘 (Diffie-Hellman)

암호화 알고리즘

해싱 알고리즘

8️⃣ 보안 세션

보안이 유지되는 통신 세션

TLS Handshake로 생성

세션 동안 상태 정보 공유

9️⃣ HTTPS 구축 방법

CA에서 인증서 직접 구매

HTTPS 지원 로드 밸런서 사용

HTTPS 지원 CDN 사용

🔟 HTTP/3
📌 특징

QUIC 프로토콜 기반

TCP ❌ → UDP 기반

WWW 환경에서 HTTP/1,2와 함께 사용

📌 장점

3-Way Handshake 없음

초기 연결 시 1-RTT만 소요

멀티플렉싱 지원

순방향 오류 수정(FEC)

패킷 손실 시 수신 측에서 복구

열악한 네트워크 환경에서도 성능 우수

🎯 핵심 비교 요약
버전	주요 특징
HTTP/1.0	요청마다 TCP 연결
HTTP/1.1	Keep-Alive, HOL Blocking
HTTP/2	멀티플렉싱, 헤더압축, 서버푸시
HTTP/3	QUIC, UDP 기반, 1-RTT
✅ 시험 한 줄 요약

HTTP는 1.0 → 연결 재사용 → 2에서 멀티플렉싱 → 3에서 QUIC으로 지연 최소화