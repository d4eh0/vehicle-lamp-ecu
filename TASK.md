# Vehicle Lamp ECU — TASK

## 개발 단계

- [x] **SYS.1** — 후방 램프 ECU 범위, 기능 요구사항, 운용 조건·제약 정리
- [x] **SYS.2** — 시스템 요구사항·인터페이스·검증 기준 정의
- [ ] **SYS.3** — MCU·CAN·LED 구동회로 및 HIL 아키텍처 설계
- [ ] **SWE.1** — 소프트웨어 요구사항
- [ ] **SWE.2** — 소프트웨어 아키텍처
- [ ] **SWE.3** — 상세설계·펌웨어 구현
- [ ] **SWE.4~6** — PC SIL 단위·통합 검증
- [ ] **SYS.4~5** — CAN 실물 연결·HIL 통합/검증

## SYS.1 산출물

[SYS.1 요구사항](docs/stakeholder-requirements.md)에서 ① 개발 대상 ② 기능 요구사항 ③ 운용·제약 조건을 정의했다.

## SYS.2 산출물

- [x] STK-001~016 요구사항 추적성 확인
- [x] CAN 입력 신호·유효성 검사 및 50ms 전송 주기 정의
- [x] ECU 재부팅 동기화, 200ms 타임아웃 및 오류 출력 정책 정의
- [x] ECU 10ms / 전체 50ms 응답시간 기준 정의
- [x] SYS-001~027 및 검증 기준 정리
- **문서:** [SYS.2 시스템 요구사항](docs/system-requirements.md)

## SYS.1·SYS.2 산출물 보강 — SYS.3 착수 전

- [ ] **SYS.1** — 시스템 컨텍스트 다이어그램 작성: diagrams.net `.drawio` 원본 및 GitHub용 `.svg` 출력. 개발 대상 ECU와 외부 BCM·스위치·후방 램프의 경계 명시
- [ ] **SYS.2** — 방향지시·비상등 우선순위/복귀 상태도 작성: Mermaid `.mmd` 원본 및 `.svg` 출력
- [ ] **SYS.2** — 정상 명령·CAN 타임아웃·재부팅 복구 시퀀스 작성: Mermaid `.mmd` 및 `.svg`
- [ ] **SYS.2** — 동작 흐름도 작성: Mermaid `.mmd` 및 `.svg`, 핵심 제어·오류 판단 단계 표현
- [x] **SYS.2** — 기존 `system-requirements.md`의 STK↔SYS 표를 STK→SYS→TC 계획 매트릭스로 확장
- [ ] 다이어그램 원본과 렌더링 파일을 GitHub에 함께 보관하고, SYS.1·2 문서/README에 필요한 것만 연결
- [ ] 도식·시험 케이스 ID가 SYS.1 STK-001~016 / SYS.2 SYS-001~027과 모순되지 않는지 검토

여기서는 요구사항 자체를 재설계하지 않는다. **SYS.1·SYS.2 정의는 완료 상태로 유지**하고, 시각화와 계획 산출물만 보강한다.

## 부품 관리

- [x] 보유 장비·기존 부품 키트 및 10/27 첫 주문 내역 정리 — [부품 명세](docs/parts.md)
- [ ] 주문 옵션별 실제 수량 및 현재 잔여 재고 확인
- [ ] SYS.2 확정 후 SYS.3에서 회로·핀맵과 필요 부품(BOM) 확정

## 후속 작업 — SYS.3

- [ ] diagrams.net `.drawio` 시스템 상세 블록도 및 인터페이스 구성도 설계
- [ ] CAN DBC(`.dbc`) 메시지 명세 및 cantools 인코딩·디코딩 검증
- [ ] CAN ID, DLC, 신호 비트 배치 및 비트레이트 설계
- [ ] STM32CubeMX `.ioc` 핀맵·클럭·CAN/UART/PWM 구성 검토
- [ ] KiCad `.kicad_sch` 회로도 설계 및 ERC·전원/구동 회로 검토
- [ ] CAN 트랜시버·종단저항·LED 구동회로와 GPIO/PWM 핀맵 설계
- [ ] Wokwi로 지원 가능한 LED/GPIO/PWM 동작만 보조 시뮬레이션 (CAN 실물 검증 대체 금지)
- [ ] ECU/BCM 전원·UART 시험 인터페이스 및 HIL 계측 방법 설계

## 이후 작업

- **SYS.3:** [아키텍처 초안](docs/architecture.md) 검토, STM32·UNO Q 핀맵, LED 드라이버, 트랜시버·120Ω 종단, HIL 계측 방법 확정
- **SWE.1~3:** CAN 메시지 처리, 램프 상태머신, PWM/점멸, 진단 구현
- **SWE.4~6 / SYS.4~5:** SIL·HIL 테스트, 기대·측정 결과와 결함 수정 기록
- **CAN FD:** STM32F103의 하드웨어 제약 해결 방안을 선택하고 별도 확장 단계에서 검증

## 작업 규칙

- 검토·실측하지 않은 작업은 완료 표시하지 않는다.
- STK → SYS → SW → 테스트 ID로 추적한다.
- 작은 파일들은 docs/에 모으고 필요할 때만 하위 폴더를 만든다.
