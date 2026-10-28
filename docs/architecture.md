# 시스템 아키텍처 (SYS.3 설계 전 구성안)

## 1. 시스템 블록

    [운전자 스위치]         [BCM 시뮬레이터]         [후방 램프 ECU]        [후방 LED]
    IGN / 레버 / 비상등 ──► Arduino UNO Q ──CAN──► STM32F103C8T6 ──► LED 드라이버
    미등 / 브레이크 / R      ├─ 디바운싱           ├─ CAN 수신·검사        ├─ TURN_L / R
                            ├─ 비상등 토글        ├─ 상태머신·우선순위    ├─ TAIL_STOP_L / R
                            └─ CAN 명령 송신      ├─ PWM / 점멸          ├─ REVERSE_LAMP
                                                 └─ 진단·기록           └─ CHMSL

- BCM 시뮬레이터는 램프 관련 명령만 모사한다. 실제 차량의 BCM 전체 기능은 포함하지 않는다.
- Rear Lamp ECU는 MCU 단독이 아니라 CAN 트랜시버, LED 구동회로, 전원, 펌웨어를 포함하는 제어장치 시제품이다.
- UNO Q는 BCM 시뮬레이터와 시험 장비 역할을 겸한다. HIL에서 GPIO·PWM을 어떤 방식으로 계측할지는 SYS.3에서 확인한다.

## 2. 통신과 확장

| 항목 | 기본 구현 | CAN FD 확장 |
|---|---|---|
| 프로토콜 | Classical CAN | CAN FD |
| UNO Q | STM32U585의 FDCAN을 Classical CAN 모드로 활용 예정 | FDCAN 및 실제 펌웨어 동작 검증 필요 |
| STM32F103 | 내장 bxCAN | 내장 CAN FD 미지원; SPI 외장 FD 컨트롤러 또는 MCU 교체 필요 |
| 물리 계층 | 노드당 호환 CAN 트랜시버·종단저항 | CAN FD 전송조건에 적합한 트랜시버 |
| 검증 | 실물 명령 송수신 및 출력·통신 장애 | CAN FD 가능한 2개 노드 구성 후 별도 검증 |

CAN FD Light는 일반 CAN FD와 다른 경량 통신 방식으로, 현재 프로젝트의 CAN FD 확장 대상으로 선정하지 않았다.

## 3. SYS.2/3 미결 사항

| 구분 | 결정할 내용 |
|---|---|
| 네트워크 | CAN ID·비트레이트·데이터 정의·전송 주기·수신 타임아웃 |
| 오류 처리 | 통신 두절·데이터 오류·ECU 재부팅에 대한 채널별 정책 |
| 회로 | CAN 트랜시버, 종단, 실제 보드 핀배치·전원 |
| 출력 | LED 전류제한·구동방식·GPIO/Timer/PWM 배정 |
| HIL | UNO Q CAN 송신과 GPIO 계측의 동시 실현 방법 |
| 시험 진단 | UART 가상 고장 주입과 정상 CAN 기능 분리 |

기능 요구사항은 [SYS.1](stakeholder-requirements.md), 수치 기준과 검증 항목은 [SYS.2](system-requirements.md)를 따른다.
