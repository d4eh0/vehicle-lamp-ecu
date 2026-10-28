# Vehicle Lamp ECU

STM32F103C8T6 기반 **후방 통합 램프 ECU** 학습·포트폴리오 프로젝트.

방향지시등, 비상등, 미등·제동등 공용 PWM, 후진등, 중앙 보조제동등(CHMSL)을 구현하고 **PC SIL 및 STM32 + Arduino UNO Q Custom HIL**로 기능과 출력 시간을 검증할 계획이다.

## 진행 상태

- **완료:** D-01~D-14 사전 기능·타이밍·오류 처리 정책 확정
- **진행 중:** SYS.2 시스템 요구사항 초안 검토
- **미완료:** 하드웨어 설계, 펌웨어 구현, SIL/HIL 테스트 및 실측

## 문서

- [개발 체크리스트](TASK.md)
- [설계 결정 기록](docs/decision-log.md)
- [시스템 요구사항 초안](docs/system-requirements.md)

> Automotive SPICE의 프로세스 구조를 학습용으로 참고하며, 정식 평가·인증, AUTOSAR 또는 ISO 26262 준수를 주장하지 않는다.
