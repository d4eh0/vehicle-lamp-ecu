# 펌웨어

| 대상 | 파일 |
|---|---|
| Rear Lamp ECU | [main.c](rear_lamp_ecu/Core/Src/main.c) — CAN 명령 해석·램프 제어 |
| 보드 설정 | [rear_lamp_ecu.ioc](rear_lamp_ecu/rear_lamp_ecu.ioc) |
| 핀 초기화 | [stm32f1xx_hal_msp.c](rear_lamp_ecu/Core/Src/stm32f1xx_hal_msp.c) |
| BCM Simulator | [bcm_simulator.ino](bcm_simulator/bcm_simulator.ino) — 자동 명령 송신 |

STM32 코드는 업로드한 CubeIDE 프로젝트 기준. 주석 처리된 과거 점등 코드만 정리했으며 실행 로직 변경 없음.
UNO Q 스케치는 대화에서 사용한 마지막 송신 코드 기준으로 복원. 실물 연동 디버깅 중인 버전.

## 개발 환경

- STM32F103C8T6, STM32CubeIDE 2.2.0, STM32Cube FW_F1 V1.8.7
- HSE 8MHz → PLL ×9 → SYSCLK 72MHz, APB1 36MHz
- Arduino IDE, UNO Q 보드 패키지에 포함된 CAN 라이브러리
- STM32 HAL·CMSIS 원본 및 라이선스는 Drivers에 포함

## 핀 연결

| STM32 | 용도 |
|---|---|
| PA0 / PA1 | TURN_L / TURN_R |
| PA6 / PA7 | TAIL_STOP_L / TAIL_STOP_R, TIM3 CH1 / CH2 |
| PB0 / PB1 | 후진등 2개 / 보조제동등 3개 |
| PB8 / PB9 | CAN RX / TX → 모듈 CRX / CTX |
| PA9 / PA10 | USART1 TX / RX, 115200 8N1. 진단 명령 미구현 |
| PB12 | 진단 LED 설정. 표시 로직 미구현 |
| PA13 / PA14 | SWDIO / SWCLK |

UNO Q D4 → CTX, D5 → CRX. 각 SN65HVD230 모듈에는 자기 보드의 3.3V와 GND 공급.
모듈 사이 CANH–CANH, CANL–CANL, GND–GND 연결. 두 보드의 3.3V 출력끼리는 연결하지 않음.

UNO Q 측 종단 120Ω, STM32 측 220Ω 두 개 병렬(약 110Ω) 사용.
전원 분리 후 버스 CANH–CANL 약 57Ω 측정. 최종 구성에서는 양 끝 120Ω 사용 예정.

[실물 CAN 배선](../docs/images/can-wiring.jpg) / [램프 출력 회로](../docs/images/lamp-output.jpg)

## 빌드·실행

1. CubeIDE에서 `rear_lamp_ecu`를 Existing Projects into Workspace로 가져오기. 워크스페이스는 프로젝트 폴더와 분리
2. 프로젝트 빌드 후 ST-LINK로 다운로드. 현재 개발 환경에서는 [OpenOCD 설정](../tools/openocd/openocd_clone.cfg)을 이용한 GDB 디버깅 사용
3. OpenOCD는 `openocd -f tools/openocd/openocd_clone.cfg`로 실행. CubeIDE GDB Hardware Debugging에서 localhost:3333과 빌드한 ELF 지정
4. 디버거 연결 후 Resume으로 연속 실행. Step 실행·브레이크포인트 정지 중에는 정상 통신·점멸 확인 불가
5. Arduino IDE에서 `bcm_simulator.ino` 열기 → UNO Q 선택 → Upload. 시리얼 모니터 115200

송신 설정: Classical CAN 500kbps, 표준 ID 0x100, DLC 1, 50ms 주기.
3초씩 좌 → 우 → 비상 → 미등 → 제동 → 후진 → 좌 → 송신 중단 순서 반복.
이 순서는 의도한 동작이며, 현재 CAN 연동 성공 기록은 없음.

## 구현과 설계의 차이

SWE.2의 컴포넌트 분리 구조는 목표 설계. 현재 구현은 `main.c`의 `ReceiveCommand()`와 `UpdateLamps()` 중심.
수신은 인터럽트 큐 대신 메인 루프 폴링으로 처리하며 한 번에 최대 3프레임 처리.
스위치·디바운싱과 UART 진단·로그는 다음 구현 범위.

## 확인 범위

- 개발 중 확인: GPIO 점등, 좌우 400ms 점멸, TIM3 PWM 밝기 변경, 후진등·보조제동등 출력
- CAN HW 확인: 두 모듈 전원 약 3.3V, 종단 합성저항 약 57Ω
- 미해결: UNO Q 송신 실패 반환(-1), STM32 수신 오류. 정상 명령 수신과 통신 두절·복구 실물 확인 전
- cantools 오프라인 검사는 DBC 검사 결과. 이 펌웨어의 SIL·단위·통합 시험 결과와 별개
- 이번 저장소 정리에서는 빌드·실물 시험 재실행 없음
