# [SYS.2] 후방 램프 ECU 시스템 요구사항

## 1. 시스템 개요

```text
물리 스위치 → Arduino UNO Q (BCM 시뮬레이터)
                            │ LAMP_COMMAND / Classical CAN
                            ▼
                       STM32F103C8T6 (Rear Lamp ECU)
                            │ GPIO / PWM
                            ▼
                       후방 램프 6개 출력
```

개발 대상은 **Rear Lamp ECU**이다. UNO Q는 외부 BCM 시뮬레이터로 사용하며, ECU는 수신한 조작 상태에 따라 램프를 제어한다.

| 구분 | 내용 |
|---|---|
| CAN 입력 | IGN, TURN, HAZARD, TAIL, BRAKE, REVERSE |
| 램프 출력 | TURN_L, TURN_R, TAIL_STOP_L, TAIL_STOP_R, REVERSE_LAMP, CHMSL |
| 통신 | Classical CAN |
| 검증 | PC SIL · 실물 HIL |

## 2. CAN 인터페이스

### LAMP_COMMAND

| 신호 | 정상 값 |
|---|---|
| IGN | 0=OFF, 1=ON |
| TURN | 0=OFF, 1=LEFT, 2=RIGHT |
| HAZARD | 0=OFF, 1=ON |
| TAIL | 0=OFF, 1=ON |
| BRAKE | 0=해제, 1=제동 |
| REVERSE | 0=NOT R, 1=R |

`TURN=3` 및 정의되지 않은 값은 유효하지 않은 명령으로 처리한다. 유효성 검사를 통과한 **메시지 전체의 상태**를 적용하며, 일부 필드만 갱신하지 않는다.

BCM 인터페이스 입력 조건: **상태 변경 즉시 전송 + 50ms 주기 전송**. CAN ID·DLC·신호의 비트 위치와 통신 속도는 인터페이스 상세 설계에서 지정한다.

### CAN 및 상태 동기화 요구사항

| ID | 시스템 요구사항 | 상위 요구 |
|---|---|---|
| SYS-021 | ECU는 `LAMP_COMMAND`의 여섯 상태 신호를 수신하여 램프 제어에 반영해야 한다. | STK-001, STK-014 |
| SYS-022 | ECU는 수신 CAN ID, DLC 및 신호 값을 검사해야 한다. 유효하지 않은 메시지 전체를 무시하고 마지막 유효 수신 시각을 갱신하지 않아야 한다. | STK-001, STK-011, STK-013 |
| SYS-023 | 마지막 유효 `LAMP_COMMAND` 수신 후 200ms 동안 유효한 메시지가 없으면 ECU는 통신 두절로 판정하고 후방 램프 6개 출력을 OFF해야 한다. | STK-013 |
| SYS-024 | ECU는 BCM이 상태 변경 시 즉시, 평상시 50ms 간격으로 보내는 동일한 상태 메시지를 처리해야 한다. | STK-001, STK-014 |
| SYS-025 | ECU는 부팅 중 및 최초 유효 CAN 메시지 수신 전 모든 램프 출력을 OFF로 유지해야 한다. | STK-010 |
| SYS-026 | ECU는 통신 복구 또는 재부팅 후 첫 유효 CAN 메시지를 수신하면 그 상태를 적용하여 램프 제어를 재개해야 한다. | STK-009, STK-010, STK-013 |

