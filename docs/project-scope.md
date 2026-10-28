# 개발 범위와 입력 조건

대상: STM32F103C8T6 기반 후방 램프 제어 소프트웨어와 외부 연결 회로.
외부 BCM: Arduino UNO Q의 운전자 입력 해석·램프 상태 명령 송신.
출력: TURN_L/R, TAIL_STOP_L/R, REVERSE_LAMP, CHMSL의 6개 논리 채널.
포함: Classical CAN·방향지시·비상등·미등·제동·후진·시험용 진단.
제외: 전방 조명·AUTO·실제 LED 단선/단락 검출·전체 차량 BCM.

