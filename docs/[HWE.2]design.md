# HWE.2 외부 회로 설계

상태: 설계 항목 초안. KiCad 회로도·BOM·ERC 미생성.
입력: [HW 요구사항]([HWE.1]requirements.md), [HW/SW 인터페이스](hardware-software-interface.md).

| 회로 블록 | 설계 항목 | 연결 요구사항 |
|---|---|---|
| 전원·GND | 공급원·보드 전원 입력·공통 GND·전류 예산 | HWR-001~002 |
| CAN | 트랜시버 전원·TX/RX·CANH/CANL·양 끝 종단 | HWR-002~003 |
| 램프 구동 | 6채널·LED 전류 제한·필요 드라이버·PWM·리셋 기본 OFF | HWR-004~006 |
| 디버깅·진단 | SWD·UART·진단 LED·계측 접점 | HWR-007 |

예정 산출물: KiCad `.kicad_sch`, 실제 사용 부품 BOM, 선정·계산 근거, ERC 결과·미해결 항목.
보유 부품 전체 목록과 실제 회로 BOM의 구분. PCB 레이아웃·제조 데이터는 이번 범위 제외.
[기존 장치 구성도](../diagrams/hardware-overview.drawio)는 연결 개요이며 회로 상세 설계 완료 근거가 아님.
