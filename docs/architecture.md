# Vehicle Lamp ECU — 아키텍처 (초안)

## 구성

```text
[물리 스위치]           [BCM 시뮬레이터]             [Rear Lamp ECU]          [후방 램프]
 IGN/레버/비상등  ──►  Arduino UNO Q ──CAN──► STM32F103C8T6 ──PWM/GPIO──► LED 구동회로
 미등/브레이크/R            │                          │                      │
                          └── 스위치 처리             ├─ CAN 명령 수신·검사       ├─ TURN_L / TURN_R
                              ·디바운싱               ├─ 우선순위·점멸 제어       ├─ TAIL_STOP_L/R
                              ·비상등 토글            ├─ PWM 제어              ├─ REVERSE_LAMP
                              ·CAN 송신               └─ 오류 상태·기록         └─ CHMSL
```

- **BCM 시뮬레이터:** 차량 BCM 전체가 아닌 램프 관련 입력·명령만 모사한다.
- **Rear Lamp ECU:** STM32 MCU, 전원/입출력, CAN 트랜시버, LED 구동회로 및 펌웨어로 구성하는 시제품이다.
- **HIL:** UNO Q가 BCM 시뮬레이터 역할과 테스트 장비 역할을 겸한다. 실제 GPIO 출력 계측 연결은 SYS.3에서 결정한다.
- **진단:** 현재 D-14의 시험용 UART 가상 고장 주입은 CAN 정상 명령과 별도 경로로 유지한다.

## 통신 범위

| 항목 | 1차 구현 | 확장 검토 |
|---|---|---|
| 버스 | Classical CAN | CAN FD |
| UNO Q | STM32U585 FDCAN을 Classical CAN 모드로 사용 | FDCAN 모드 및 펌웨어 지원 확인 |
| 후방 ECU | STM32F103 내장 bxCAN | MCP2518FD 등 SPI 외장 FD 컨트롤러 또는 FDCAN MCU |
| 물리 계층 | 각 노드에 CAN 트랜시버 1개, CANH/CANL, 종단저항·GND | CAN FD 비트레이트에 적합한 트랜시버 |
| 메시지 | IGN·레버·비상등·미등·제동·후진 상태 | 64바이트 프레임 및 고속 데이터 구간 검증 |
| 검증 | 실제 송수신·출력·오류 처리 | FD 가능 노드 2대 구성 후 별도 검증 |

> **현재 결정 사항:** 1차 목표는 Classical CAN 기반 동작 완성. CAN FD는 반드시 하드웨어·소프트웨어 조건을 확인한 뒤 실행 범위를 확정한다. CAN FD Light는 별도의 경량 프로토콜로 이번 구현 대상으로 확정하지 않았다.

## SYS.2에서 정할 인터페이스

1. CAN 메시지 ID·데이터 필드, 전송 주기와 방향
2. 잘못된 명령·메시지 누락·통신 타임아웃에 대한 램프 출력 정책
3. ECU 리셋 후 UNO Q와 상태 동기화(비상등 토글 포함)
4. 스위치 변화 → CAN 전달 → 첫 LED 출력의 총 응답시간 기준
5. UART 고장 주입과 CAN 명령 사이 테스트 책임 분리

실제 회로·핀맵·브레드보드 배선·CAN 속도는 아직 확정하지 않았다.
