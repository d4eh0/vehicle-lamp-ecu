# CAN 인터페이스

외부 계약: BCM_SIM → REAR_LAMP_ECU, Classical CAN 표준 11비트, 500 kbit/s.
메시지: LAMP_COMMAND / ID `0x100` / DLC 1.
[DBC](../can/vehicle-lamp.dbc) · 연결: SWR-001~003,013~014.

| 신호 | 시작 비트 | 길이 | 값 |
|---|---:|---:|---|
| IGN | 0 | 1 | 0 OFF / 1 ON |
| TURN | 1 | 2 | 0 OFF / 1 LEFT / 2 RIGHT / 3 무효 |
| HAZARD | 3 | 1 | 0 OFF / 1 ON |
| TAIL | 4 | 1 | 0 OFF / 1 ON |
| BRAKE | 5 | 1 | 0 RELEASED / 1 PRESSED |
| REVERSE | 6 | 1 | 0 NOT_R / 1 R |
| RESERVED | 7 | 1 | 0 필수, 1 수신 시 메시지 전체 무효 |

형식: unsigned / Intel / scale 1 / offset 0.
BCM 송신 조건: 입력 변경 즉시 + 50 ms 주기.
ECU 수신 조건: 메시지 전체 검사, 무효 시 마지막 정상 수신 시각 유지.
통신 두절: 마지막 유효 수신 후 200 ms, 전체 OFF. 복구 시 첫 유효 현재 상태 적용.

선정 이유: 6개 입력 표현에 7비트, 한 프레임의 일관된 상태 전달.
HAZARD: 토글 이벤트가 아닌 현재 ON/OFF. TURN 보존으로 해제 후 재평가.
ID: 프로젝트 내부 메시지 식별자. 수신 장치 주소·표준 지정값 아님.
DBC 주기·속도 속성: 설정 메타데이터. 실제 송신·컨트롤러 설정은 펌웨어 책임.

## 도구 검토

![SavvyCAN 비트 배치](../diagrams/savvycan-review.png)

SavvyCAN: 메시지·신호 배치 검토, 수신 노드 지정·저장.
캡처: 수신 노드 수정 전 화면. 저장본의 최종 수신 노드: 전 신호 REAR_LAMP_ECU.
저장본 일부 설명·버스 속성 누락으로 텍스트 DBC를 기준 파일로 유지.
cantools 45.1.2: 정상 96조합 인코딩·디코딩, 데이터 256개 분류, 오류 프레임 조건 9개 참조 검사.
실제 CAN 통신·펌웨어 타임아웃·출력 시험: 미실시.

```sh
python3 -m pip install -r can/can-design-requirements.txt
python3 can/check_can_interface.py
```

[검사 코드](../can/check_can_interface.py) · [검사 결과](../can/CAN-interface-check-results.json)
