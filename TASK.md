# Vehicle Lamp ECU — TASK

## 진행 현황

- [x] SYS.1 — 후방 램프 기능·동작 정책 및 BCM–CAN 구조 선택 (D-01~D-15)
- [ ] **SYS.2 — 시스템 요구사항 분석** (CAN 반영 초안 검토 중)
- [ ] SYS.3 — 시스템 아키텍처·하드웨어 설계
- [ ] SWE.1 — 소프트웨어 요구사항
- [ ] SWE.2 — 소프트웨어 아키텍처
- [ ] SWE.3 — 상세설계·구현
- [ ] SWE.4~6 — SIL 검증
- [ ] SYS.4~5 — HIL 시스템 검증

## 단계별 작업

### SYS.1 — 요구사항 도출
- [x] 전·후방 램프 검토 후 후방 램프 ECU로 범위 확정
- [x] 방향지시·비상등·미등·제동등·후진등·CHMSL 채택
- [x] 스위치 입력·동작 우선순위·점멸·PWM·가상 고장 정책 결정
- [x] BCM 시뮬레이터(UNO Q) → CAN → STM32 후방 램프 ECU 구조 선택
- **산출물:** [`docs/decision-log.md`](docs/decision-log.md)

### SYS.2 — 시스템 요구사항 분석 ★ 현재
- [ ] 입력의 책임 분리: UNO Q의 물리 스위치 처리 / STM32의 CAN 명령 처리 확정
- [ ] `SYS-001~` 기능 요구사항을 CAN 기반 구조에 맞춰 검토
- [ ] 방향지시·비상등·제동등·후진등 진리표 및 수치 기준 확정
- [ ] CAN 명령 형식, 수신 주기, 오류·타임아웃 시 처리 정책 결정
- [ ] 최초 점등 응답 측정 구간 재정의 (스위치→UNO Q→CAN→STM32)
- **산출물:** [`docs/system-requirements.md`](docs/system-requirements.md)

### SYS.3 — 시스템 아키텍처 설계
- [ ] STM32·UNO Q·CAN 트랜시버·LED 블록도 확정
- [ ] CAN 핀·속도·종단저항·전압, PWM 핀 및 LED 구동회로 설계
- [ ] 물리 스위치와 HIL 출력 측정 회로 구분, GPIO 자원 점검
- [ ] [`docs/parts.md`](docs/parts.md) 실제 주문/보유/미구매 상태 갱신
- [ ] CAN FD 확장 방식 선택: SPI 외장 컨트롤러 또는 FDCAN MCU
- **산출물:** [`docs/architecture.md`](docs/architecture.md), `hardware/` (필요 시)

### SWE.1 — SW 요구사항
- [ ] `SYS-xxx`에서 `SWR-xxx` 도출, BCM과 ECU 담당 로직 구분
- [ ] CAN 메시지 송수신, 유효성 검증, 상태머신, 진단·타이밍 요구 명세
- **산출물:** `docs/software-requirements.md`

### SWE.2 — SW 아키텍처
- [ ] CAN 수신·명령 해석·점멸/PWM·진단·GPIO 모듈 설계
- [ ] 핵심 C 제어 로직과 STM32 HAL 분리 및 SIL 빌드 구조 설계
- **산출물:** `docs/architecture.md`에 SW 구성 추가

### SWE.3 — 상세설계·구현
- [ ] UNO Q 스위치 처리·CAN 송신, STM32 CAN 수신·출력 제어 구현
- [ ] STM32 GPIO·타이머/PWM·진단 UART와 LED 회로 연동
- **산출물:** `firmware/`, 필요 시 `tests/`

### SWE.4~6 — SIL 검증
- [ ] 단위·통합 테스트, 램프 기능 및 CAN 명령 파서 경계값 검증
- [ ] `SWR-xxx`별 기대/실제 결과와 회귀 결과 기록
- **산출물:** `tests/sil/`, `docs/verification.md`

### SYS.4~5 — 시스템 통합·HIL 검증
- [ ] UNO Q CAN 송신 ↔ STM32 수신 실물 검증
- [ ] 점멸·PWM·응답시간·통신 오류·가상 고장 시험 및 측정 오차 기록
- [ ] `SYS-xxx`별 PASS/FAIL 및 근거 정리
- **산출물:** `tests/hil/`, `docs/verification.md`

### 최종 정리
- [ ] README 회로 사진·구조도·시연·검증 결과 및 빌드 방법 추가
- [ ] 구현한 Classical CAN과 미구현 CAN FD 기능을 구별하여 명시

## 작업 원칙

- `[x]`는 완료된 결정/작업만 표시한다. 검토 전 문서는 초안으로 둔다.
- 요구사항은 D-ID → SYS-ID → SW/테스트 ID로 연결한다.
- CAN 도입 전 D-09(디바운싱), D-13(응답 20/30ms)은 시스템 배치·측정 시작점을 재검토한다.
- 단일 문서가 충분하면 `docs/`에 바로 둔다.
- 커밋: `docs: [SYS.2] CAN 요구사항 확정` 형식.
