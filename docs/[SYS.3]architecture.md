# 시스템 아키텍처 (SYS.3 설계 초안)

## 1. 시스템 블록

![SYS.3 시스템 정적 아키텍처](../diagrams/%5BSYS.3%5Dstatic-architecture.svg)

[draw.io 편집 원본](../diagrams/%5BSYS.3%5Dstatic-architecture.drawio)

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

## 3. 상세 설계 항목

| 구분 | 설계할 내용 |
|---|---|
| CAN 인터페이스 | `LAMP_COMMAND` ID·DLC·비트 배치·비트레이트 |
| 회로 | CAN 트랜시버, 종단, 실제 보드 핀배치·전원 |
| 램프 출력 | LED 전류 제한·드라이버·GPIO·Timer/PWM 배정 |
| HIL | UNO Q CAN 송신 및 출력 파형 계측 방법 |
| 시험 진단 | UART 고장 주입 명령 형식, 진단 LED 점멸 간격 |

전송 주기 50ms, 통신 두절 200ms 및 램프 오류 대응은 [시스템 요구사항](%5BSYS.2%5Dsystem-requirements.md)에 정의한다.

기능 요구사항은 [SYS.1](%5BSYS.1%5Dstakeholder-requirements.md), 수치 기준과 검증 항목은 [SYS.2](%5BSYS.2%5Dsystem-requirements.md)를 따른다.

## 4. 동적 아키텍처

[draw.io 편집 원본 — 4페이지](../diagrams/%5BSYS.3%5Ddynamic-architecture.drawio)

| 흐름 | 관련 요구사항 | 주요 설계 조건 |
|---|---|---|
| 정상 명령 처리 | SYS-001~014, SYS-021~024 | 변경 즉시·50ms 주기 송신, 메시지 전체 검사 후 적용. 정상 신규 요청의 유효 수신→출력 변경은 10ms 이내, 물리 입력→출력은 50ms 이내를 목표로 한다. |
| 통신 두절·복구 | SYS-016, SYS-022~023, SYS-026~027 | 무효 명령은 마지막 유효 수신 시각을 갱신하지 않는다. 200ms 무수신 시 전체 OFF, 유효 명령으로 복구한다. 가상 고장 채널은 OFF를 유지한다. |
| ECU 재부팅·재동기화 | SYS-015, SYS-020, SYS-025~026 | BCM 입력 상태는 유지한다. ECU RAM 기록·가상 고장은 초기화하며 최초 유효 명령 전까지 OFF를 유지한다. |
| 시험용 채널 고장·해제 | SYS-017~020 | 지정 채널만 OFF로 유지하고 CLEAR 후 최신 명령을 재평가한다. 통신 두절 중에는 CLEAR 이후에도 전체 OFF다. |

관련 요구사항은 흐름의 참조 범위이며 전체 추적성 검토 완료를 뜻하지 않는다. 그림의 시간 수치는 설계 목표이며 실물 측정 결과가 아니다. 진단 LED 점멸은 메시지 수신·복구를 지연시키지 않도록 설계한다. RAM 이벤트는 최근 16건을 유지한다. 리셋 중 출력 회로의 기본 OFF 조건과 구체적인 핀·구동 회로는 후속 설계에서 확정한다.

### 정상 명령 처리

![SYS.3 정상 명령 처리](../diagrams/%5BSYS.3%5Ddynamic-01.png)

### 통신 두절·복구

![SYS.3 통신 두절·복구](../diagrams/%5BSYS.3%5Ddynamic-02.png)

### ECU 재부팅·재동기화

![SYS.3 ECU 재부팅·재동기화](../diagrams/%5BSYS.3%5Ddynamic-03.png)

### 시험용 채널 고장·해제

![SYS.3 시험용 채널 고장·해제](../diagrams/%5BSYS.3%5Ddynamic-04.png)
