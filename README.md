# Vehicle Lamp ECU

STM32F103C8T6 기반 후방 램프 제어 소프트웨어와 외부 연결 회로.
Arduino UNO Q는 운전자 입력·CAN 명령 송신용 BCM 시뮬레이터.

| 대상 | 범위 |
|---|---|
| 소프트웨어 | 방향지시·비상등·미등·제동등·후진등·CHMSL, 통신 장애·가상 고장 처리 |
| 하드웨어 | 개발보드·CAN 트랜시버·LED 구동부·전원 연결. 커스텀 PCB 제외 |
| 개발 기준 | Automotive SPICE 4.0의 SWE.1~6 및 HWE.1~2 일부 활동 참고 |
| 시험 환경 | PC SIL, 실물 보드, HIL 구성 계획 |

| 도구 | 산출물·상태 |
|---|---|
| diagrams.net | 환경 구성도·기존 동작 흐름 보존, SW 모듈 구조·시퀀스 검토 초안 |
| SavvyCAN / cantools | CAN DBC 검토·오프라인 검사 완료 |
| STM32CubeMX / CubeIDE | 핀·클럭·CAN·UART·PWM 설정 및 C 코드 예정 |
| KiCad | 외부 연결 회로도·BOM·ERC 예정 |
| Wokwi | 지원 범위 내 LED·GPIO·PWM 보조 시뮬레이션 예정 |
| C·Python 시험 도구 | SW 단위·통합·요구사항 시험 예정 |

[작업 목록](TASK.md) · [문서 목차](docs/README.md)

현재 상태: 요구사항·SW 설계 검토 초안. 램프 펌웨어·회로도·SIL/HIL 결과 미완료.
공식 프로세스 심사·적합성 평가 범위 제외.
