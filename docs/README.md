# 설계 산출물

프로젝트 단계별 산출물과 참조 문서를 모아 둔다. 상세 구현·시험 결과가 아직 없는 항목은 완료된 것으로 표시하지 않는다.

| 단계 | 주요 산출물 | 상태 |
|---|---|---|
| SYS.1 | [\[SYS.1\]stakeholder-requirements.md](%5BSYS.1%5Dstakeholder-requirements.md) — 이해관계자 요구사항 및 개발 범위 | 명세 완료 |
| SYS.1 | 시스템 컨텍스트 — [SVG](../diagrams/%5BSYS.1%5Dsystem-context.svg) · [편집 원본](../diagrams/%5BSYS.1%5Dsystem-context.drawio) | 작성 완료 |
| SYS.2 | [\[SYS.2\]system-requirements.md](%5BSYS.2%5Dsystem-requirements.md) — 시스템 요구사항·성능 기준 | 명세 완료 |
| SYS.2 | [\[SYS.2\]traceability.md](%5BSYS.2%5Dtraceability.md) — STK↔SYS 대응, 향후 시험 케이스 연결 | STK↔SYS 연결 완료 / TC 미정 |
| SYS.3 | [\[SYS.3\]architecture.md](%5BSYS.3%5Darchitecture.md) — 시스템 아키텍처 설계 | 설계 초안 |
| SYS.3 | 정적 아키텍처 — [SVG](../diagrams/%5BSYS.3%5Dstatic-architecture.svg) · [편집 원본](../diagrams/%5BSYS.3%5Dstatic-architecture.drawio) | 검토본 반영 |
| SYS.3 | 동적 아키텍처 4종 — [설명·미리보기](%5BSYS.3%5Darchitecture.md#4-동적-아키텍처) · [편집 원본](../diagrams/%5BSYS.3%5Ddynamic-architecture.drawio) | 검토본 반영 |
| SYS.3 | CAN 인터페이스 — [명세·도구 검토](%5BSYS.3%5Dcan-interface.md) · [DBC](../can/vehicle-lamp.dbc) | 오프라인 검사 완료 / 실통신 미검증 |
| 공통 | [parts.md](parts.md) — 장비·부품 목록 | 계속 보완 |

## 추가할 산출물

- SYS.2: Mermaid 상태도·시퀀스·제어 흐름도 (`.mmd`, `.svg`)
- SWE.2~3: CubeMX 설정 및 소프트웨어 설계·구현
- HWE.1~2: 외부 회로 요구사항·KiCad 회로도

작업 순서와 완료 기준은 루트의 [TASK.md](../TASK.md)를 따른다.

