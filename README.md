# Vehicle Lamp ECU

STM32F103C8T6 기반 후방 램프 제어 ECU.

Arduino UNO Q가 **BCM 시뮬레이터**로서 조작 입력을 처리하고, Classical CAN으로 후방 램프 ECU에 명령을 보낸다. STM32는 수신한 명령에 따라 방향지시등·비상등·미등·제동등·후진등·중앙 보조제동등(CHMSL)을 제어한다.

```text
스위치 → Arduino UNO Q (BCM 시뮬레이터)
                         │ Classical CAN
                         ▼
                 STM32F103 (Rear Lamp ECU)
                         │ GPIO / PWM · LED 구동회로
                         ▼
                       후방 LED
```

## 주요 기능

- 좌·우 방향지시등 및 비상등, 기능 우선순위
- 공용 미등·제동등 PWM 및 후진등·CHMSL 제어
- CAN 수신·명령 처리, 통신 오류 및 가상 고장 처리
- PC SIL 및 UNO Q 기반 Custom HIL 검증
- CAN FD 확장 검토: STM32F103 내장 CAN은 Classical CAN까지만 지원

## 개발 환경

- Rear Lamp ECU: STM32F103C8T6 · C · STM32CubeIDE
- BCM Simulator / HIL: Arduino UNO Q (STM32U585)
- 통신: Classical CAN (구현 예정), CAN FD (하드웨어 확장 검토)
- 검증: SIL / HIL (예정)

## 진행 현황

- [x] SYS.1 기능 및 동작 정책 결정 (D-01~D-15)
- [ ] SYS.2 시스템 요구사항 분석 — CAN 인터페이스 반영 및 검토 중
- [ ] SYS.3 시스템 아키텍처·회로 설계
- [ ] SWE.1~3 소프트웨어 설계·구현
- [ ] SWE.4~6 SIL 검증
- [ ] SYS.4~5 HIL 검증

## 문서

- [개발 계획](TASK.md)
- [결정 기록](docs/decision-log.md)
- [시스템 요구사항](docs/system-requirements.md)
- [아키텍처 초안](docs/architecture.md)
- [부품 명세](docs/parts.md)
