# Vehicle Lamp ECU

STM32F103C8T6 기반 후방 램프 제어 소프트웨어·외부 연결 회로.
운전자 입력: Arduino UNO Q의 BCM 시뮬레이터. 전달: Classical CAN.
제어: 방향지시·비상등·미등·제동등·후진등·CHMSL의 6개 논리 출력.

개발 범위: SWE.1~6, 외부 회로 HWE.1~2 활동 참고.
공식 프로세스 평가·적합성 주장 제외.

[개발 계획](TASK.md) · [문서 목차](docs/README.md)

DBC·SavvyCAN·cantools: 오프라인 검토 완료. 램프 펌웨어·실물 CAN·SIL/HIL 결과 미완료.
