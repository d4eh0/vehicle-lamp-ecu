# Vehicle Lamp ECU

**STM32F103C8T6 기반 후방 램프 ECU 개발 프로젝트.**

운전자 조작은 Arduino UNO Q의 BCM 시뮬레이터에서 처리하고, **Classical CAN**으로 STM32 후방 램프 ECU에 전달한다. ECU는 명령을 해석해 후방 방향지시등·비상등·미등·제동등·후진등·CHMSL을 제어한다.

    Switches → Arduino UNO Q (BCM simulator)
                              │ Classical CAN
                              ▼
                       STM32F103 (Rear Lamp ECU)
                              │ GPIO / PWM
                              ▼
                     LED drivers → Rear lamps

## 기술 및 검증 계획

- **MCU:** STM32F103C8T6 · Embedded C · STM32CubeIDE
- **BCM 시뮬레이터:** Arduino UNO Q
- **통신:** Classical CAN 1차 목표, CAN FD는 외장 컨트롤러/MCU 변경을 포함해 확장 검토
- **검증:** PC SIL, UNO Q 기반 Custom HIL
- **기능:** 6개 논리 출력 채널, 램프 우선순위, 점멸·PWM, 오류 주입·기록

## 진행 상태

- [x] SYS.1 — 개발 범위·기능·운용 조건 정의
- [x] SYS.2 — 시스템 요구사항 및 검증 기준 명세
- [ ] SYS.3 — 상세 시스템 아키텍처·회로
- [ ] SWE.1~3 — SW 요구사항·설계·구현
- [ ] SWE.4~6 / SYS.4~5 — SIL·HIL 검증

## 문서

- [개발 계획](TASK.md)
- [SYS.1 — 요구사항](docs/stakeholder-requirements.md)
- [SYS.2 — 시스템 요구사항](docs/system-requirements.md)
- [아키텍처 구성안](docs/architecture.md)
- [보유 부품 명세](docs/parts.md)
