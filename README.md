# Vehicle Lamp ECU

STM32F103C8T6 기반 후방 램프 제어 시스템.

후방 방향지시등, 비상등, 미등·제동등, 후진등, 중앙 보조제동등(CHMSL)을 제어한다. 기능별 요구사항을 정의하고 Embedded C로 구현한 뒤 SIL과 HIL로 검증한다.

## 주요 기능

- 좌·우 방향지시등 및 비상등 제어
- PWM 기반 미등·제동등 밝기 전환
- 후진등 및 중앙 보조제동등 제어
- 시동 상태에 따른 출력 제어
- 테스트용 가상 고장 주입 및 오류 기록

## 개발 환경

- MCU: STM32F103C8T6
- Language: C
- IDE: STM32CubeIDE
- SIL: PC 네이티브 테스트 (예정)
- HIL: Arduino UNO Q + STM32 (예정)

## 진행 현황

- [x] SYS.1 요구사항 도출
- [ ] SYS.2 시스템 요구사항 분석 (초안 작성)
- [ ] SYS.3 시스템 아키텍처 설계
- [ ] SWE.1~3 SW 설계 및 구현
- [ ] SWE.4~6 SIL 검증
- [ ] SYS.4~5 HIL 검증

## 문서

- [TASK](TASK.md)
- [Decision Log](docs/decision-log.md)
- [System Requirements](docs/system-requirements.md)
