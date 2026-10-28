# Vehicle Lamp ECU — TASK

> STM32F103C8T6 후방 통합 램프 ECU를 설계·구현하고 SIL(PC)·Custom HIL(STM32 + UNO Q)로 검증한다.
> Automotive SPICE SYS/SWE 흐름을 학습 목적으로 참고한다. 정식 평가·인증이나 ISO 26262/AUTOSAR 준수를 주장하지 않는다.
> **정책 확정, 문서 초안 작성, 구현, 검증 완료는 서로 다르다.**

## 현재 상태

- [x] GitHub 저장소 생성 및 후방 램프 ECU 범위 선정
- [x] **D-01~D-14 사전 설계 정책 결정** — [decision-log.md](docs/decision-log.md)
- [x] **SYS.2 시스템 요구사항 초안 작성** — [system-requirements.md](docs/system-requirements.md)
- [ ] **현재: SYS.2 초안 검토·수정 후 확정**
- [ ] SYS.3 회로·아키텍처, SWE 설계·구현, SIL/HIL 검증

## 작업 순서

### 0. 사전 정책 결정 (SYS.1 개념 참고) — 완료
- [x] D-01~D-14: 기능, 입력, 우선순위, 시동, 점멸, PWM, 고장 처리 정책 확정
- [x] 대안·근거·검증 방향 기록 — `docs/decision-log.md`
- 별도 가상 고객·이해관계자 요구 문서는 작성하지 않는다. 공식 SYS.1 수행 완료를 의미하지 않는다.

### 1. SYS.2 — 시스템 요구사항 분석 ★ 현재
- [x] 기존 결정에서 `SYS-xxx` 시스템 요구사항 초안 도출
- [x] 입출력·동작 진리표·정량 기준·근거 D-ID 정리
- [ ] 요구사항 간 모순, 누락, 모호한 시험 조건 검토
- [ ] 수정 반영 후 SYS.2 요구사항 확정
- **산출물:** `docs/system-requirements.md` 단일 파일 (D-ID 연결 포함)

### 2. SYS.3 — 시스템 아키텍처·하드웨어
- [ ] ECU/스위치/LED/전원/UNO Q 블록도 및 HW/SW 기능 분담
- [ ] GPIO·타이머·UART 핀맵, 회로·배선 및 LED 드라이버/전류 제한 검토
- [ ] 보유/구매 부품 목록과 UNO Q의 PWM·시간 측정 가능성 확인
- **산출물:** `docs/architecture.md`, `hardware/`에 필요 시 BOM·배선 자료

### 3. SWE.1 — SW 요구사항
- [ ] `SYS-xxx`를 `SWR-xxx`로 세분화: 디바운싱, SW 응답, 상태, 진단 및 인터페이스
- [ ] 각 SW 요구사항에 상위 SYS-ID와 검증 조건 연결
- **산출물:** `docs/software-requirements.md`

### 4. SWE.2 — SW 아키텍처
- [ ] 입력 처리·상태머신·타이머/PWM·고장 진단·출력 제어 모듈 분리
- [ ] 동일 핵심 로직을 STM32와 PC SIL에서 실행할 HAL 추상화 설계
- **산출물:** `docs/architecture.md`에 SW 설계 추가

### 5. SWE.3 — 상세설계 및 Embedded C 구현
- [ ] 상태 전이·함수 설계 후 STM32 HAL/GPIO/Timer/PWM/UART 구현
- [ ] 실제 회로 구동 및 빌드·실행 결과 확인
- **산출물:** `firmware/` 및 필요 시 설계 문서 보완

### 6. SWE.4~6 — SIL 검증
- [ ] PC에서 단위·경계값 테스트(디바운싱·점멸·오류 로그)
- [ ] 모듈 통합 및 `SWR-xxx`별 기대값/실제값·PASS/FAIL 기록
- **산출물:** `tests/sil/`, `docs/verification.md`

### 7. SYS.4~5 — Custom HIL 및 시스템 검증
- [ ] UNO Q로 STM32 입력 생성·출력 GPIO 측정, UART 시험용 고장 주입
- [ ] 점멸 400±20ms, 첫 응답 20/30ms, PWM 주파수·듀티 등 실측
- [ ] `SYS-xxx`별 PASS/FAIL, 근거 및 미달 원인·재검증 기록
- **산출물:** `tests/hil/`, `docs/verification.md`

### 8. 포트폴리오 정리
- [ ] README에 회로 사진·아키텍처·시연·테스트 방법 및 실제 결과 연결
- [ ] 완료/미완료와 실제 구현·검증 범위 명확히 표시

## 원칙

- 소수의 설계 문서는 `docs/`에 바로 둔다. 필요할 때만 하위 디렉터리로 분리한다.
- 요구사항 추적성은 `SYS-xxx` 옆의 D-ID, `SWR-xxx` 옆의 SYS-ID, 검증표의 테스트 ID로 연결한다.
- D-07/D-09/D-11/D-13의 시간·PWM 수치는 미검증 초기 목표다. 미달하면 실측값→원인→수정 또는 변경 근거→재검증을 기록한다.
- D-14는 시험용 **가상 고장**이다. 실제 LED 단선·단락 감지나 실차 기능안전을 주장하지 않는다.
- 실질적 작업 단위로 커밋한다. 예: `docs: [SYS.2] 시스템 요구사항 초안 및 문서 구조 정리`.
