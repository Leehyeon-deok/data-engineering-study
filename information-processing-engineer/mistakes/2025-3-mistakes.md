시험 암기표

용어		특징
Hamming	오류 검출 + 수정
FEC		재전송 없이 수정
BEC		재전송 요구
Parity		1비트 검사
CRC		다항식 이용

① Hamming 코드
오류 검출 + 수정 가능
검사 비트를 여러 개 추가
대표적인 오류 수정 코드

② FEC (Forward Error Correction)
수신 측에서 스스로 수정
재전송이 필요 없음
예: Hamming Code

암기: Hamming → FEC

③ BEC (Backward Error Correction)
오류가 나면 송신 측에 재전송 요구
ARQ 방식이라고도 함

암기: BEC → 재전송

④ Parity 검사
데이터 끝에 1비트(패리티 비트) 추가
홀수/짝수 개수 검사

예) 1011001
패리티 비트 1 추가

⑤ CRC 검사
다항식(Polynomial) 이용
통신에서 가장 많이 사용하는 오류 검출 방식

암기: CRC = 다항식

시험에서는 이렇게 외우면 됩니다.
식	결과
~0	-1
~1	-2
~2	-3
~5	-6
~10	-11

암기 공식 ⭐⭐⭐
~x = -(x+1)

자주 나오는 비트 연산자
연산자	의미		예시
&	AND		둘 다 1이면 1
l	OR		하나라도 1나오면  1
^	XOR		서로 다르면 1
~	NOT		비트 반전
<<	왼쪽 시프트	비트를 왼쪽으로 이동
>>	오른쪽 시프트	비트를 오른쪽으로 이동


extends와 차이
시험에서 가장 많이 물어보는 부분입니다.

키워드		의미
extends		클래스 상속
implements	인터페이스 구현


enumerate(data)는 (인덱스, 값)을 반환합니다.
즉,

(0, [3,5,2,4,1])
(1, [4,5,1])
(2, [4,4,1,5,4])
(3, [4,5])


기호		이름			의미
σ (Sigma)		선택(Selection)		행(Row) 선택 (조건 검색)
π (Pi)		투영(Projection)		열(Column) 선택
∪		합집합(Union)		두 릴레이션 합치기
−		차집합(Difference)		한쪽에만 있는 튜플
∩		교집합(Intersection)	공통 튜플
×		카티션 곱(Cartesian Product)	모든 경우의 수
⋈		조인(Join)			공통 속성으로 연결
÷ (또는 %)	나눗셈(Division)		"모두 만족하는" 값 찾기


÷ (또는 %)
수강(Student, Subject)

학생	과목
김	DB
김	OS
박	DB
이	OS

필수과목(Subject)

과목
DB
OS

수강 ÷ 필수과목 :
결과는 학생 김 뿐입니다.

김 → DB, OS 모두 있음 → ✅
박 → DB만 있음 → ❌
이 → OS만 있음 → ❌

시험에서 자주 나오는 enum 메서드
메서드			설명			예
name()			상수 이름 반환		Tri.A.name() → "A"
ordinal()			순서(0부터) 반환		Tri.B.ordinal() → 1
values()			모든 상수 배열 반환	[A, B, C]
valueOf("B")		이름으로 상수 반환		Tri.valueOf("B") → Tri.B

암기 포인트
name() → 이름(String)
ordinal() → 순번(int)
values() → 배열(enum[])

MAC	
중앙에서 보안 정책을 일괄적으로 설정하며, 주체(사용자)가 임의로 수정하거나 변경할 수 없다. 주로 군사 기밀, 국가 보안과 같은 높은 보안 수준이 요구되는 환경에서 사용된다. 보안 등급(Top Secret / Secret / Confidential 등)에 따라 접근 여부가 결정된다.

RBAC	
조직 내에서 부여된 직무나 역할(Role)에 따라 접근 권한을 부여하는 방식이다. 개별 사용자에게 직접 권한을 설정하지 않고, 역할에 권한을 묶어 부여하기 때문에 관리가 용이하며 직무 변경 시 역할만 변경하면 된다.

DAC	
자원의 소유자(Owner)가 해당 자원에 대한 접근 권한을 자유롭게 부여하거나 회수할 수 있는 방식이다. 파일이나 폴더의 소유자가 읽기/쓰기/실행 권한을 설정하는 것이 대표적인 예로 사용자의 임의 설정이 가능해 보안성이 상대적으로 낮다.