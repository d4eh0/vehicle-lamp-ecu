# Vehicle Lamp ECU — TASK

> 목표: STM32F103 기반 후방 통합 램프 ECU를 요구사항 → 시스템/소프트웨어 설계 → Embedded C → SIL → Custom HIL → 요구사항 검증 순서로 개발한다.
>
> 기준: Automotive SPICE 4.1의 SYS/SWE 프로세스를 **학습 및 산출물 구성에 참고**한다. 공식 A-SPICE 평가·인증, 정식 AUTOSAR 준수, ISO 26262 준수를 주장하지 않는다.
>
> 규칙: **실제로 수행하고 산출물/검증 근거가 확인된 항목만 `[x]`** 처리한다. 계획·제안·미작성 문서는 `[ ]`로 유지한다. 파일 경로는 예정 경로이며, 단계별 설계 판단에 따라 변경 시 이 파일도 업데이트한다.

## 0. 프로젝트 초기 상태

- [x] GitHub 저장소 `d4eh0/vehicle-lamp-ecu` 생성
- [x] 구현 범위 선정: 후방 통합 램프 ECU (좌/우 방향지시등, 비상등, 미등, 제동등, 후진등)
- [x] 후진 입력 선정: 2단 슬라이드 스위치 (`R / NOT R`)
- [ ] SYS.2 요구사항 분석 완료

## 1. 개발 프로세스 및 정확한 산출물 경로

### SYS.2 — 시스템 요구사항 분석
- [ ] ECU 시스템 경계, 기능 및 입력/출력 정의
- [ ] 정상 동작, 동시 입력, 전원 상태 및 비정상 상황 정의
- [ ] 검증 가능한 요구사항 ID (`SYS-xxx`)와 수용 기준 확정
- [ ] **산출물:** `docs/system/system-requirements.md`
- [ ] **결정 기록:** `docs/decisions/decision-log.md`

### SYS.3 — 시스템 아키텍처 설계
- [ ] ECU·스위치·램프·HIL 장비의 시스템 구성과 인터페이스 정의
- [ ] HW/SW 기능 할당, 3.3V 전기적 조건, GPIO 배선/핀 맵 결정
- [ ] **산출물:** `docs/system/system-architecture.md`
- [ ] **회로/배선:** `hardware/wiring-plan.md`
- [ ] **핀 맵:** `hardware/pin-map.md`

### SWE.1 — 소프트웨어 요구사항 분석
- [ ] `SYS-xxx`에서 `SWR-xxx` 도출 및 정량적인 검증 조건 작성
- [ ] 시스템 ↔ SW 요구사항 양방향 추적성 작성
- [ ] **산출물:** `docs/software/software-requirements.md`
- [ ] **추적성:** `docs/traceability/requirements-traceability.md`

### SWE.2 — 소프트웨어 아키텍처 설계
- [ ] AUTOSAR Classic에서 **계층 분리 개념만 참고**해 ASW/인터페이스/하드웨어 의존성 분리
- [ ] SW 컴포넌트, 데이터 흐름, 인터페이스 및 오류 전파 정의
- [ ] **산출물:** `docs/software/software-architecture.md`
- [ ] **인터페이스 명세:** `docs/software/interface-specification.md`

### SWE.3 — SW 상세설계 및 구현
- [ ] UML 상태머신, 이벤트/전이표, 함수·데이터·타이밍 상세설계
- [ ] Embedded C 구현, STM32 HAL 연동 및 실물 브레드보드 회로 제작
- [ ] **상세설계:** `docs/software/software-detailed-design.md`
- [ ] **구현/빌드 기록:** `docs/software/implementation-notes.md`
- [ ] **펌웨어 진입점(예정):** `firmware/Core/Src/main.c`
- [ ] **펌웨어 헤더(예정):** `firmware/Core/Inc/main.h`
- [ ] SW 모듈별 추가 `.c/.h` 파일명은 SWE.2 아키텍처 확정 후 여기 명시

### SWE.4 — 소프트웨어 단위 검증 (SIL)
- [ ] PC 네이티브 빌드에서 Stub/Mock 기반 단위·경계값·오류 처리 테스트
- [ ] 테스트 결과 및 가능한 범위의 코드 커버리지 기록
- [ ] **테스트 계획:** `docs/verification/swe4-unit-test-plan.md`
- [ ] **테스트 결과:** `docs/verification/swe4-unit-test-report.md`
- [ ] **테스트 코드 위치:** `tests/sil/unit/` (개별 파일명은 단위 설계 후 확정)

### SWE.5 — SW 컴포넌트·통합 검증 (SIL)
- [ ] 컴포넌트 간 인터페이스, 상태 전이, 동시 입력 및 통합 동작 검증
- [ ] **테스트 계획:** `docs/verification/swe5-integration-test-plan.md`
- [ ] **테스트 결과:** `docs/verification/swe5-integration-test-report.md`
- [ ] **테스트 코드 위치:** `tests/sil/integration/`

### SWE.6 — SW 요구사항 검증 (SIL)
- [ ] 각 `SWR-xxx`에 검증 테스트 ID와 결과 연결
- [ ] 요구사항 커버리지 및 회귀 검증
- [ ] **테스트 계획:** `docs/verification/swe6-software-verification-plan.md`
- [ ] **테스트 결과:** `docs/verification/swe6-software-verification-report.md`
- [ ] **테스트 코드 위치:** `tests/sil/requirements/`
- [ ] **추적성 갱신:** `docs/traceability/requirements-traceability.md`

### SYS.4 — 시스템 통합 및 통합 검증 (Custom HIL)
- [ ] Arduino UNO Q가 STM32 ECU의 입력을 생성하고 실제 출력을 측정하는 HIL 구성
- [ ] GPIO 인터페이스, 출력 타이밍, HW/SW 통합 및 비정상 입력 테스트
- [ ] **테스트 계획:** `docs/verification/sys4-system-integration-plan.md`
- [ ] **테스트 결과:** `docs/verification/sys4-system-integration-report.md`
- [ ] **HIL 테스트 코드 위치:** `tests/hil/`

### SYS.5 — 시스템 요구사항 검증 (Custom HIL / 실물)
- [ ] `SYS-xxx`별 End-to-End 시험 및 PASS/FAIL 검증
- [ ] 요구사항·실제 결과·증거 링크 정리
- [ ] **테스트 계획:** `docs/verification/sys5-system-verification-plan.md`
- [ ] **테스트 결과:** `docs/verification/sys5-system-verification-report.md`
- [ ] **추적성 최종화:** `docs/traceability/requirements-traceability.md`

### 최종 결과 정리
- [ ] **검증 요약:** `docs/verification/verification-summary.md`
- [ ] **프로젝트 소개, 아키텍처, 시연, 검증 근거:** `README.md` 갱신
- [ ] 모든 SYS/SWE 단계의 증거 및 체크리스트 대조

## 2. SYS.2 사전 의사결정 목록 (총 8건)

> **방법:** D-01~D-08을 정해진 순서로 결정한다. 진행 중 발견되는 추가 쟁점은 즉시 선택하지 않고 아래 '추가 결정 대기열'에 적어 **D-08 이후 일괄 결정**한다. 사용자 판단 → 검토/근거 기록 → 요구사항 반영 순서다.

- [x] **D-01 기능 범위:** 후방 통합 ECU (좌·우 방향지시등, 비상등, 미등, 제동등, 후진등)
- [x] **D-02 후진 입력:** 2단 슬라이드 스위치 (`R / NOT R`)
- [x] **D-03 시동과 미등:** 별도 미등 스위치로 시동과 독립 제어 (AUTO 제외, 시동 OFF 정책은 D-06에서 결정)
- [x] **D-04 조작 입력 방식:** 레버 위=우회전/중앙=OFF/아래=좌회전, 브레이크=누르는 동안 ON, 비상등=누를 때마다 ON/OFF 토글
- [x] **D-05 동시 작동 정책:** 비상등 우선(좌·우 동기 점멸), 미등·제동등 공용 LED/PWM 밝기 전환(제동 우선), 후진등 독립 동시 작동
- [x] **D-06 시동 OFF 정책:** 비상등·미등·제동등 입력 동작 허용, 방향지시등·후진등 출력 차단 (ON=입력 조건 충족 시 허용, 상시 점등 아님)
- [x] **D-07 점멸 정책:** 방향지시등·비상등 ON 400ms/OFF 400ms (75회/분), 각 구간 허용 오차 ±20ms, 점멸 기능 전환 시 새 기능 ON부터 시작하며 타이머 리셋
- [x] **D-08 초기화·비정상 상황:** MCU 재부팅 시 출력 OFF 안전 초기화 후 물리 입력 재평가·비상등 토글 OFF, 좌우 레버 동시 활성 시 방향지시 무효/오류 기록(정상 기능 유지), 입력 오류 및 테스트용 가상 출력 고장 주입 검증

### 추가 결정 대기열

- [ ] **D-09 스위치 디바운싱 정책:** 입력별 적용 범위, 디바운싱 방식/시간, 토글의 1회 입력 판정 (D-08 완료 후 결정)
- [ ] **D-10 보조제동등(CHMSL) 추가:** 후면 중앙 LED 3개 추가 여부 및 브레이크 연동 정책 (D-08 완료 후 결정)
- [ ] **D-11 공용 LED PWM 세부값:** 미등/제동등 목표 밝기, PWM 주파수·듀티 및 검증 기준 (D-08 완료 후 결정)
- [ ] **D-12 시동 전환·전원 동작:** IGN OFF/ON 전환 시 유지 중인 레버·후진 입력의 재평가, 비상등 토글 상태 유지/초기화, 시동 OFF에서도 ECU 동작 가능한 전원 공급 조건 (D-08 이후 결정, 전원 구조는 SYS.3 반영)
- [ ] **D-13 첫 점등 응답 및 측정 기준:** 점멸 요청 인식부터 최초 ON까지 허용 지연과 SIL/HIL 측정 시점 정의 (D-08 완료 후 결정; D-07의 400±20ms ON/OFF 구간과 구별)
- [ ] **D-14 오류 기록·가상 출력 고장 처리:** 테스트용 출력 오류 주입 인터페이스, 출력별 안전 대응 및 고장 해제, 오류 로그 내용·유지 정책 (D-08 완료 후 결정; 실제 전류/단선 검출 아님)

## 3. 단계별 완료 기준

- 각 단계는 문서 파일 존재만으로 완료 처리하지 않는다.
- 요구사항은 모호하지 않고 테스트로 검증할 수 있어야 한다.
- 설계 선택은 근거/대안/트레이드오프가 `docs/decisions/decision-log.md`에 남아야 한다.
- 검증은 테스트 ID, 기대 결과, 실제 결과와 증거를 연결해야 한다.
- 진행할 때마다 이 `TASK.md`의 체크 상태를 실제 완료 범위에 맞게 갱신한다.
