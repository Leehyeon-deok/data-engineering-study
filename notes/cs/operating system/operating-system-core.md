운영체제(OS) 핵심 개념 정리

(CPU · Memory · System Call · Cache · Virtual Memory)

1. 운영체제(OS)란?

운영체제(OS, Operating System)는 하드웨어와 소프트웨어를 관리하는 핵심 시스템 소프트웨어이다.
사용자 프로그램과 하드웨어 사이에서 중재자 역할을 수행하며, 컴퓨터 자원을 효율적이고 안전하게 관리한다.

OS가 관리하는 주요 자원

CPU

Memory

Storage (Disk)

I/O Device

2. 운영체제의 주요 역할 (4가지)

CPU 스케줄링 및 프로세스 관리

프로세스 생성/종료

CPU 할당 및 문맥 교환(Context Switch)

메모리 관리

메모리 할당/회수

가상 메모리 관리

디스크 및 파일 시스템 관리

파일 생성, 삭제, 접근 제어

디스크 공간 관리

I/O 디바이스 관리

키보드, 마우스, 카메라 등 장치 제어

디바이스 드라이버 관리

3. 운영체제 구조
User Program
────────────
GUI
System Call
────────────
Kernel
Device Driver
────────────
Hardware


OS는 유저 프로그램과 하드웨어 사이에 위치

GUI가 없는 CUI 기반 리눅스 서버도 존재

4. 시스템 콜(System Call)
4.1 시스템 콜이란?

유저 프로그램이 커널에 접근하기 위한 인터페이스

유저 프로그램이 OS의 서비스를 요청할 때 사용

4.2 동작 과정

유저 프로그램에서 I/O 요청 발생

Trap(인터럽트) 발생

요청의 유효성 검사

유저 모드 → 커널 모드 전환

커널이 파일/디바이스 접근

처리 후 다시 유저 모드 복귀

👉 이를 통해 하드웨어 직접 접근을 차단하고
👉 프로그램 간 보호(Isolation) 를 보장

4.3 시스템 콜의 특징

프로세스/스레드가 OS에 요청할 때 반드시 거침

추상화 계층

네트워크, DB, 파일 시스템 등 저수준 처리를 신경 쓰지 않아도 됨

5. Mode Bit (유저 모드 / 커널 모드)

Mode Bit: 0 또는 1 값을 가지는 플래그

User Mode

Kernel Mode

왜 필요한가?

유저 모드에서 직접 하드웨어 제어 시 보안 취약

예: 악성 프로그램이 카메라를 무단으로 켜는 문제

👉 OS를 통해서만 접근 가능하도록 제한
👉 보안 및 안정성 확보

6. CPU 구조와 역할
CPU 구성 요소

ALU (산술논리연산장치)

Control Unit (제어장치)

Register (레지스터)

CPU의 역할

메모리에 존재하는 명령어를 해석하고 실행

OS 커널이 프로그램을 메모리에 적재 → 프로세스 생성

CPU는 일꾼처럼 명령어 처리

7. CPU 내부 구성 요소
7.1 제어장치(Control Unit)

명령어 해석

프로세스 동작 지시

입출력 장치 간 통신 제어

7.2 레지스터(Register)

CPU 내부의 초고속 임시 기억장치

CPU는 직접 저장 능력이 없기 때문에 레지스터를 통해 데이터 처리

8. 인터럽트(Interrupt)

외부 또는 내부 이벤트 발생 시 CPU 작업을 잠시 중단

I/O 완료, 타이머, 오류 등

👉 효율적인 CPU 사용을 가능하게 함

9. DMA 컨트롤러

I/O 디바이스가 메모리에 직접 접근하도록 하는 하드웨어

CPU의 보조 일꾼 역할

CPU와 DMA가 동시에 같은 작업을 하지 않도록 조정

👉 CPU 부담 감소 → 성능 향상

10. 메모리 계층 구조와 캐시(Cache)
10.1 캐시란?

자주 사용하는 데이터를 미리 복사해 두는 고속 임시 저장소

CPU와 메모리 간 속도 차이로 인한 병목 해결

메모리 계층
Register
Cache
Main Memory(RAM)
Secondary Storage


👉 이러한 구조를 캐싱 계층(Cache Hierarchy) 이라고 함

10.2 캐시 히트 / 미스

Cache Hit: 캐시에 데이터 존재 → 빠름 (CPU 내부 버스)

Cache Miss: 메모리에서 접근 → 느림 (시스템 버스)

10.3 캐시 매핑 방식

Direct Mapping

Associative Mapping

Set-Associative Mapping

👉 작은 캐시로 큰 메모리를 효율적으로 다루기 위한 방식

11. 가상 메모리(Virtual Memory)

실제 메모리보다 큰 메모리를 사용하는 것처럼 보이게 하는 기법

메모리 자원의 추상화

12. 스와핑(Swapping) & 페이지 폴트

Page Fault: 가상 메모리에는 있지만 RAM에 없는 페이지 접근

사용하지 않는 메모리 영역을 디스크로 이동

디스크 일부를 메모리처럼 사용

👉 사용자에게는 문제 없는 것처럼 보임

13. 스레싱(Thrashing)

페이지 폴트율이 매우 높은 상태

스와핑 과다 → 성능 급격히 저하

발생 원인

메모리에 너무 많은 프로세스 적재

CPU 이용률 감소 → OS가 더 많은 프로세스 적재

악순환 반복

해결 방법

메모리 증설

작업 세트(Working Set)

PFF(Page Fault Frequency)

14. 메모리 할당 기법
14.1 연속 할당

고정 분할 방식

가변 분할 방식

최초 적합

최적 적합

최악 적합

14.2 불연속 할당

페이징(Paging)

15. 페이지 교체 알고리즘

FIFO

LRU

LFU

NUR (Clock Algorithm)

Optimal (Offline Algorithm)