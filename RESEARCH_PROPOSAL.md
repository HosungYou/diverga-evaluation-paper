# Research Proposal: Ethical AI Scaffolding in Research Design

## Human Checkpoints as Epistemic Scaffolds: An Educational Design Research Study of AI-Mediated Research Methodology Assistance

---

## 1. 연구 제목 (Title)

**영문:** *Human Checkpoints as Epistemic Scaffolds: An Educational Design Research Study of AI-Mediated Research Methodology Assistance Using Diverga*

**한글:** 인식론적 스캐폴드로서의 Human Checkpoint: Diverga를 활용한 AI 매개 연구 방법론 보조의 교육 설계 연구

---

## 2. 초록 (Abstract)

AI 연구 보조 도구의 급속한 확산에도 불구하고, 이러한 도구가 연구자의 방법론적 의사결정에 미치는 영향에 대한 체계적 연구는 부족하다. 특히, 대부분의 AI 도구가 "mode collapse"—동일한 예측 가능한 추천을 반복하는 현상—를 보이며, 연구자의 비판적 사고를 약화시키는 automation bias를 유발할 수 있다는 우려가 제기되고 있다. 본 연구는 Verbalized Sampling(VS) 방법론과 구조적 Human Checkpoint 시스템을 결합한 AI 연구 보조 플랫폼 Diverga를 대상으로, Educational Design Research(EDR) 방법론과 Activity Theory(AT)의 통합 프레임워크를 통해 다음을 탐구한다: (1) Human Checkpoint가 연구자의 의사결정 자율성을 어떻게 매개하는가, (2) VS 기반 다양성 제안이 이론적 프레임워크 선택에 미치는 영향, (3) AI-assisted 연구 설계 과정에서 연구자가 설정하는 ethical boundary의 양상. 사회과학 분야 박사과정생 15-20명을 대상으로 3차례의 반복적 설계-평가 사이클을 수행하며, 실천적 산출물(design principles)과 이론적 산출물(AI-mediated research에서의 ethical scaffolding 이론)의 이중 기여를 목표로 한다.

---

## 3. 연구의 필요성 (Statement of the Problem)

### 3.1 AI 연구 도구의 확산과 윤리적 공백

2025-2026년 현재, Elicit, Consensus, SciSpace 등 AI 기반 연구 보조 도구가 급속히 확산되고 있다. 이들 도구는 문헌 검색과 데이터 합성에서 효용을 입증했으나, 연구 **설계** 단계에서의 AI 활용에 대한 윤리적 프레임워크는 여전히 미비하다.

EDUCAUSE(2025)는 AI의 교육적 활용에서 공정성, 투명성, 책무성의 중요성을 강조했고, Emerald의 체계적 합성(2024)은 privacy, bias, transparency, accountability, integrity의 5대 핵심 우려를 확인했다. 그러나 이러한 프레임워크들은 AI를 **사용하는** 학습자 또는 교육자를 대상으로 하며, AI를 **연구 설계에 활용하는 연구자**의 맥락은 거의 다루지 않는다.

### 3.2 Mode Collapse: 구조적 문제

범용 AI(ChatGPT, Claude 등)에 연구 방법론 추천을 요청하면, 고도로 예측 가능한 응답이 반복된다: 기술 수용 연구에는 TAM, 질적 연구에는 주제 분석(thematic analysis), 메타분석에는 랜덤 효과 모델. 이를 "mode collapse"라 하며, 그 원인은 학습 데이터의 typicality bias에 있다(arXiv:2510.01171). 즉, 주석자들이 인지심리학적으로 익숙한 텍스트를 체계적으로 선호하여, 모델이 가장 전형적인(modal) 응답으로 수렴하는 것이다.

이 문제는 단순한 불편을 넘어 학술적 위험을 초래한다: 연구자의 이론적 선택이 AI의 modal recommendation에 의해 동질화될 수 있으며, 이는 학문의 다양성과 창의성을 훼손한다.

### 3.3 Automation Bias와 연구자 자율성

Springer Nature의 체계적 리뷰(2025)는 automation bias가 Human-AI 협업에서 심각한 도전임을 확인했다. AI 도구를 사용한 의사결정에서 78%의 에이전트가 독립적 검토 없이 AI 출력을 수용했으며, 51%의 결정이 AI 제안을 맹목적으로 따른 것이었다. Microsoft Research(2025)는 AI 도구 사용 빈도와 비판적 사고 능력 사이에 유의미한 부적 상관을 보고했으며, 이는 인지적 오프로딩(cognitive offloading)에 의해 매개되었다.

이러한 맥락에서, AI 연구 도구에 **구조적 개입 지점(structured intervention points)**을 설계하여 연구자의 비판적 판단을 보존하는 것이 시급한 과제이다.

### 3.4 기존 도구의 한계와 Diverga의 고유성

현존하는 AI 연구 도구와 Diverga의 핵심 차이는 다음과 같다:

| 특성 | 기존 도구 (Elicit, Consensus 등) | Diverga |
|---|---|---|
| 추천 방식 | 단일 최적 추천 (mode collapse) | VS 기반 다중 대안 + T-Score |
| 인간 개입 | 선택적, 비구조적 | 구조적 REQUIRED checkpoint |
| 커버리지 | 문헌 검색/합성 | 연구 전 생애주기 (9 카테고리, 44 에이전트) |
| 감사 추적 | 없음 | Decision Audit Trail (YAML) |
| 투명성 | 출처 제시 수준 | 추천의 전형성(T-Score) 명시 |

이러한 차별점은 연구적으로 흥미로운 질문을 제기한다: **구조적 Human Checkpoint와 VS 기반 다양성 제안의 결합이 실제로 automation bias를 완화하고 연구자의 방법론적 추론을 활성화하는가?**

---

## 4. 연구 질문 (Research Questions)

| RQ | 질문 | 유형 |
|---|---|---|
| **RQ1** | Diverga의 Human Checkpoint 시스템은 연구자의 방법론적 의사결정 자율성(methodological decision autonomy)을 어떻게 매개하는가? | 탐색적 (QUAL 중심) |
| **RQ2** | VS 기반 다양성 제안(T-Score 포함)은 연구자의 이론적 프레임워크 선택 다양성에 어떤 영향을 미치는가? | 확인적 (QUAN + QUAL) |
| **RQ3** | AI-assisted 연구 설계 과정에서 연구자는 ethical boundary를 어디에, 어떻게 설정하는가? | 탐색적 (QUAL 중심) |
| **RQ4** | Diverga의 어떤 설계 특성(design features)이 연구자의 methodological reasoning을 활성화 또는 억제하는가? | 설계 지향적 (EDR) |

---

## 5. 이론적 프레임워크 (Theoretical Framework)

### 5.1 삼층 프레임워크 구조

본 연구는 세 수준의 프레임워크를 통합한다:

```
┌─────────────────────────────────────────────────────────┐
│  Level 1: Methodology                                    │
│  Educational Design Research (McKenney & Reeves, 2019)  │
│  → 연구의 전체 구조와 반복 논리                            │
├─────────────────────────────────────────────────────────┤
│  Level 2: Theoretical Lens                               │
│  Activity Theory (Engeström, 2015)                       │
│  → 무엇을 분석하고 어떻게 해석할 것인가                     │
├─────────────────────────────────────────────────────────┤
│  Level 3: Data Strategy                                  │
│  Mixed Methods (Creswell & Plano Clark, 2018)           │
│  → 각 phase 내에서의 수집/분석 방법                        │
└─────────────────────────────────────────────────────────┘
```

### 5.2 Educational Design Research (EDR)

McKenney & Reeves(2019)의 EDR Generic Model을 채택한다. EDR은 "실천적이고 복잡한 교육 문제에 대한 해결책의 반복적 개발이 경험적 탐구의 맥락을 제공하며, 이를 통해 타인의 작업에 도움이 되는 이론적 이해를 산출하는 연구 장르"로 정의된다.

EDR의 세 핵심 단계:
1. **Analysis & Exploration** — 문제 확인 및 문헌/실무자 협업을 통한 이해
2. **Design & Construction** — 아이디어의 점진적 정교화, 가지치기, 조작화
3. **Evaluation & Reflection** — 설계 아이디어와 프로토타입의 경험적 조사 및 성찰

EDR의 채택 근거:
- **이중 산출물(dual outcome)**: 성숙해가는 중재(Diverga의 checkpoint 설계 개선) + 이론적 이해(ethical scaffolding 이론)
- **반복성(iterative nature)**: Diverga가 v8~v10으로 진화 중인 시스템이므로, "평가하면서 개선한다"는 EDR 철학에 부합
- **실무자 협업(practitioner collaboration)**: 연구자가 단순 피험자가 아닌 공동 설계자로 참여

#### Conjecture Mapping (Sandoval, 2014)

EDR의 체계성을 강화하기 위해 Sandoval의 Conjecture Mapping 기법을 통합한다. Conjecture Map은 학습 환경 설계를 통한 추측(conjecture)을 매핑하는 기법으로, 설계가 어떻게 기능해야 하는지에 대한 추측(design conjectures)과 그 기능이 어떻게 의도된 결과를 산출하는지에 대한 이론적 추측(theoretical conjectures)을 구분한다.

**본 연구의 Conjecture Map:**

```
High-Level Conjecture:
"AI 연구 도구에 구조적 Human Checkpoint와 VS 기반 다양성 제안을
결합하면, 연구자의 방법론적 추론이 활성화되고
automation bias가 완화된다"
          │
          ▼
┌─────────────────────────────────────────────────────────┐
│                    EMBODIMENT                             │
│                                                          │
│  도구/자료:          과제 구조:        참여자 구조:         │
│  - Diverga 플랫폼   - 가상 연구       - 개인 작업          │
│  - T-Score 시각화     시나리오 2개    - Think-Aloud         │
│  - VS 대안 제시     - Pre/Post 설계    세션                 │
│  - 3 REQUIRED CP   - Checkpoint      - 사후 인터뷰         │
│  - Decision Log      통과 과제       - 연구자 저널          │
│                                                          │
│  담화 실천:                                               │
│  - T-Score에 대한 연구자 해석 토론                          │
│  - Checkpoint에서의 자기 정당화(self-justification)         │
└─────────────────────────────────────────────────────────┘
          │
          ▼  Design Conjectures
┌─────────────────────────────────────────────────────────┐
│              MEDIATING PROCESSES                          │
│                                                          │
│  - 연구자가 modal recommendation을 비판적으로 평가          │
│  - T-Score를 통해 자신의 선택의 전형성을 인식               │
│  - Checkpoint에서 일시 멈춤이 성찰적 사고를 촉발            │
│  - 대안 탐색이 기존 지식과의 연결을 활성화                   │
│  - Decision Log 작성이 자기 정당화를 요구                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
          │
          ▼  Theoretical Conjectures
┌─────────────────────────────────────────────────────────┐
│                   OUTCOMES                                │
│                                                          │
│  - 이론적 프레임워크 선택의 다양성 증가                     │
│  - 방법론적 추론의 질 향상                                 │
│  - Automation bias 감소                                   │
│  - Ethical boundary에 대한 명시적 인식 형성                 │
│  - 연구 설계 관행의 확장적 학습(expansive learning)          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 5.3 Activity Theory (AT)

Engeström(2015)의 3세대 Activity Theory를 이론적 렌즈로 채택한다. AT의 채택 근거:

1. **도구 매개(tool mediation)**: Diverga가 연구자와 연구 설계 사이를 매개하는 방식을 분석하는 데 적합
2. **모순(contradiction) 분석**: Diverga 사용 과정에서 발생하는 긴장과 갈등을 체계적으로 포착
3. **확장적 학습(expansive learning)**: Checkpoint를 통한 연구자의 관행 변화를 이론화

**Diverga Activity System 모델:**

```
                    Tool: Diverga
               ┌─── (44 agents + VS + Checkpoints) ───┐
               │                                        │
               │    ┌─ T-Score 기반 다중 대안 제시       │
               │    ├─ REQUIRED Checkpoint (강제 정지)   │
               │    ├─ Decision Audit Trail             │
               │    └─ 3-Layer Memory System            │
               │                                        │
    Subject ───┴────────────────────────────▶ Object ──▶ Outcome
    (사회과학                                 (연구       (완성된
     박사과정생)                               설계)       연구 계획)
         │                                     │
         │                                     │
    Rules ├──── Community ────┤ Division of Labor
    │                │                    │
    ├ 학문적 규범     ├ 동료 연구자         ├ AI: 대안 생성,
    ├ IRB 기준       ├ 지도교수             │   typicality 계산,
    ├ 표절 규정      ├ 학회 커뮤니티        │   문헌 검색
    ├ AI 사용 정책   └ IRB                 └ Human: 선택, 정당화,
    └ Checkpoint                              윤리적 판단,
      통과 조건                                최종 결정
```

**분석 대상 모순(Contradictions):**

| 모순 수준 | 내용 | 연구 질문 연결 |
|---|---|---|
| **Primary** (도구 내부) | Diverga의 "창의적 대안 제시"와 "학술적으로 검증된 방법론 추천" 사이의 긴장 | RQ2 |
| **Secondary** (구성요소 간) | Subject의 자율성 ↔ Tool의 추천 권위 | RQ1 |
| **Tertiary** (활동 체계 간) | 학문 공동체의 "검증된 이론 사용" 규범 ↔ Diverga의 "낮은 T-Score 탐색" 권유 | RQ3 |
| **Quaternary** (인접 활동 간) | AI 사용에 대한 IRB/학회 정책 ↔ Diverga의 설계 철학 | RQ3 |

### 5.4 Automation Bias 완화 메커니즘으로서의 Human Checkpoint

본 연구의 핵심 이론적 주장은 다음과 같다:

> **Conjectured Theory:** AI 연구 도구에서 human checkpoint는 단순한 승인 메커니즘(approval mechanism)이 아니라, 연구자의 methodological reasoning을 활성화하는 **인식론적 스캐폴드(epistemic scaffold)**로 기능한다. 이 효과는 세 가지 조건이 동시에 충족될 때 극대화된다: (a) 다중 대안의 동시 제시, (b) 각 대안의 전형성(typicality) 가시화, (c) 시간 제한 없는 숙고 여유.

이 주장은 다음의 선행 연구에 기반한다:
- ScienceDirect의 연구에서 선택 자율성(choice autonomy)과 통제 자율성(control autonomy) 메커니즘이 알고리즘 회피(algorithm aversion)를 감소시키는 것으로 확인됨
- Buçinca et al.(2021)의 인지적 강제 기능(cognitive forcing functions)이 부정확한 AI 추천에 대한 의존을 유의미하게 감소시킴
- ScienceDirect의 연구에서 인터페이스 경고 넛지(warning nudge)가 automation bias 효과를 완화하고 사용자 성능을 거의 두 배로 향상시킴

Diverga의 checkpoint는 이러한 메커니즘을 통합적으로 구현한다:
- **다중 대안 제시** = Cognitive Forcing Function (선택을 강제)
- **T-Score 시각화** = Warning Nudge (modal recommendation에 대한 경고)
- **REQUIRED 정지** = Choice Autonomy (AI가 아닌 인간이 결정)

---

## 6. 연구 방법 (Methodology)

### 6.1 연구 설계 개요

```
                    McKenney & Reeves EDR Generic Model

  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │  Phase 1        │    │  Phase 2        │    │  Phase 3        │
  │  Analysis &     │───▶│  Design &       │───▶│  Evaluation &   │
  │  Exploration    │    │  Construction   │    │  Reflection     │
  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
           │                      │                      │
           ▼                      ▼                      ▼
  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │ AT Lens:        │    │ AT Lens:        │    │ AT Lens:        │
  │ Activity System │    │ Contradiction   │    │ Transformation  │
  │ Mapping         │    │ Identification  │    │ & Expansive     │
  │                 │    │ & Design        │    │ Learning        │
  │                 │    │ Principle 도출   │    │                 │
  └─────────────────┘    └─────────────────┘    └─────────────────┘
           │                      │                      │
           ▼                      ▼                      ▼
    Implementation & Spread (점진적 확대)  ──────────────────▶
```

### 6.2 Phase 1: Analysis & Exploration (약 4주)

**목적:** 문제 공간의 체계적 이해, 현재 연구자들의 AI 활용 실태와 ethical boundary 파악

**활동:**

| 활동 | 방법 | 데이터 | AT 분석 초점 |
|---|---|---|---|
| 문헌 분석 | Mode collapse, VS, HITL, automation bias 선행연구 검토 | 문헌 매트릭스 | 기존 AI 도구의 activity system 구조 |
| 도구 비교 분석 | Diverga vs. Elicit, Consensus, SciSpace, ASReview 기능 비교 | 비교 매트릭스 | 도구별 Division of Labor 차이 |
| 탐색적 인터뷰 | 5-8명 사회과학 박사과정생 반구조화 인터뷰 | 전사, 메모 | Subject-Tool 관계의 현재 tension |
| 맥락 분석 | 참여자의 연구 설계 습관, AI 사용 이력, 윤리 인식 조사 | 설문, 인터뷰 | Community-Rules 관계 |

**Phase 1 핵심 질문:**
- 연구자들은 현재 AI 도구를 연구 설계에 어떻게 사용하고, 어디서 ethical 불편함을 느끼는가?
- 기존 AI 도구에서 mode collapse를 경험한 적 있는가? 그 영향은?
- Human checkpoint 없는 AI 추천에 대해 어떤 수준의 신뢰를 갖는가?

**Phase 1 산출물:**
- Baseline Activity System Diagram (Diverga 사용 전)
- 요구 분석 보고서
- Phase 2를 위한 refined problem statement

### 6.3 Phase 2: Design & Construction (약 4주)

**목적:** Phase 1 발견에 기반한 pilot intervention 설계, tentative design principles 도출

**Intervention 설계:**

| 구성 요소 | 기존 Diverga | Pilot 조정 | 근거 |
|---|---|---|---|
| Checkpoint 수준 | 4 REQUIRED + 다수 RECOMMENDED | 3개 핵심 CP 집중 (CP_RESEARCH_DIRECTION, CP_THEORY_SELECTION, CP_METHODOLOGY_APPROVAL) | 인지 부하 최소화 |
| VS T-Score 제시 | 모든 에이전트에서 활성 | T-Score 의미 설명 scaffolding 추가 | Phase 1 인터뷰 기반 |
| 과제 시나리오 | 오픈 엔드 | 구조화된 가상 시나리오 2개 (익숙/새로운 주제) | 통제된 비교 가능 |
| 에이전트 범위 | 44개 전체 | A1(연구질문), A2(이론), A5(패러다임), C1/C2(설계) 위주 | 연구 초기 단계 집중 |
| 사용 환경 | CLI 자율 사용 | 연구자 워크스테이션 + 화면/음성 녹화 | 데이터 수집 통합 |

**Tentative Design Principles:**

| DP | 원칙 | 이론적 근거 | 검증 방법 |
|---|---|---|---|
| **DP1** | REQUIRED checkpoint에서 최소 3개 이상의 VS 대안을 T-Score와 함께 제시해야 한다 | Cognitive Forcing Functions (Buçinca et al., 2021); VS의 다양성 효과 (arXiv:2510.01171) | 선택 다양성 지수(Shannon entropy) 측정 |
| **DP2** | Checkpoint에서의 deliberation은 시간 제한 없이 연구자에게 위임해야 한다 | Human-in-power 개념 (PMC); Choice autonomy와 algorithm aversion 감소 | Think-aloud에서 deliberation 질 분석 |
| **DP3** | AI의 추천 근거(T-Score 산출 논리)를 투명하게 공개해야 한다 | AI ethics literacy의 핵심 (Nature Scientific Reports, 2025); XAI와 trust calibration | 참여자의 근거 이해도 인터뷰 |
| **DP4** | Checkpoint는 연구자의 기존 지식을 무효화하지 않고 확장하는 방향이어야 한다 | AT의 tool mediation — 도구는 역량을 대체하지 않고 매개; Expansive learning | Pre-post 연구 설계 비교, AT contradiction 분석 |

**AT Contradiction 분석과 Design Principles의 관계:**

```
  Primary Contradiction (도구 내부):
  ┌─────────────────────────────────────────────────────────┐
  │  Diverga의 "창의적 대안 제시" ↔ "검증된 방법론 추천"      │
  │  → DP1: T-Score로 이 긴장을 가시화하여 연구자가 인식       │
  └─────────────────────────────────────────────────────────┘

  Secondary Contradiction (구성요소 간):
  ┌─────────────────────────────────────────────────────────┐
  │  Subject(연구자 자율성) ↔ Tool(AI 추천의 권위)            │
  │  → DP2: Checkpoint에서 시간 제한 없는 숙고                │
  │  → DP4: 확장적 scaffold — 대체가 아닌 매개                │
  └─────────────────────────────────────────────────────────┘

  Tertiary Contradiction (활동 체계 간):
  ┌─────────────────────────────────────────────────────────┐
  │  학문 공동체의 "검증된 이론" 규범 ↔ "낮은 T-Score 탐색"   │
  │  → DP3: 투명한 근거 제시로 학술적 방어 가능성 확보         │
  └─────────────────────────────────────────────────────────┘
```

### 6.4 Phase 3: Evaluation & Reflection (약 8주)

**목적:** Design principles 검증, activity system 변화 분석, refined principles 도출

#### 6.4.1 참여자

| 항목 | 내용 |
|---|---|
| 대상 | 사회과학 분야(교육학, 심리학, 경영학, 사회학, HRD, 커뮤니케이션) 박사과정생 |
| 인원 | 15-20명 (QUAN + QUAL 통합) |
| 선정 기준 | (1) 연구 방법론 수업 1과목 이상 이수, (2) AI 도구 사용 경험 있음, (3) CLI 환경 기본 이해 |
| 제외 기준 | (1) Diverga 사전 사용 경험자, (2) 컴퓨터 과학/공학 전공자 |
| 모집 | 대학원 연구방법론 수업에서 게스트 워크숍 형태 |

#### 6.4.2 과제 설계

**시나리오 A (익숙한 주제):** "K-12 교육에서의 AI 도구 활용이 학생의 학업 성취에 미치는 영향"에 대한 연구를 설계하시오. 이론적 프레임워크, 연구 방법, 데이터 수집 계획을 포함하시오.

**시나리오 B (새로운 주제):** "원격 근무 환경에서의 AI 기반 협업 도구가 팀 창의성에 미치는 영향"에 대한 연구를 설계하시오. 이론적 프레임워크, 연구 방법, 데이터 수집 계획을 포함하시오.

**절차:**
1. Pre-task: Diverga **없이** 시나리오 A에 대한 연구 설계 (30분)
2. 도구 소개: Diverga 기능 및 checkpoint 시스템 설명 (20분)
3. Post-task: Diverga **사용하여** 시나리오 B에 대한 연구 설계 (60분, Think-Aloud)
4. Post-task: Diverga **사용하여** 시나리오 A 재설계 (40분, Think-Aloud)
5. 반구조화 인터뷰 (30분)

#### 6.4.3 데이터 수집

| 데이터 원천 | 수집 방법 | 분석 목적 | 유형 |
|---|---|---|---|
| **Checkpoint 로그** | Diverga `research/decision-log.yaml` 자동 기록 | 선택 패턴, deliberation time, T-Score별 선택 빈도 | QUAN |
| **연구 설계 산출물** | Pre/Post 연구 설계 문서 | 이론적 프레임워크 선택 다양성, 설계 질 변화 | QUAN+QUAL |
| **Think-Aloud** | Checkpoint 통과 시 실시간 사고 구술 (화면+음성 녹화) | Checkpoint가 촉발하는 인지 과정의 질적 분석 | QUAL |
| **반구조화 인터뷰** | Pilot 완료 후 개인 인터뷰 | Ethical boundary 인식, 도구 신뢰, 개선 제안 | QUAL |
| **연구자 저널** | 사용 기간 중 성찰 기록 (선택적) | 종단적 태도 변화 | QUAL |
| **Pre-Post 설문** | Decision Autonomy Scale, AI Ethics Literacy, Trust in AI Checkpoint | 양적 변화 측정 | QUAN |
| **화면 녹화** | 전체 사용 과정 | 행동 패턴 분석, T-Score 확인 행동 | QUAN+QUAL |

#### 6.4.4 분석 방법

**양적 분석:**
- 이론적 프레임워크 선택 다양성: Shannon Entropy Index (pre vs. post)
- T-Score별 선택 빈도 분포: 기술 통계
- Checkpoint deliberation time: 기술 통계, 패턴 분석
- Pre-Post 설문: Wilcoxon signed-rank test (소표본)

**질적 분석:**
- Think-Aloud 전사: Thematic Analysis (Braun & Clarke, 2006)
- 인터뷰 전사: 이론적 코딩 (AT의 구성요소를 선험적 코드로 활용)
- AT 기반 3수준 분석:
  1. **Activity System 변화**: Diverga 사용 전/후 activity system diagram 비교
  2. **Contradiction 분석**: Design principles가 contradiction을 해소/심화했는지
  3. **Expansive Learning 증거**: 연구자가 checkpoint를 통해 연구 설계 관행을 재개념화한 증거

**통합 분석:**
- Joint Display: 양적 패턴(T-Score 선택 분포)과 질적 해석(선택 이유)의 병렬 제시
- Conjecture Map 수정: 데이터 기반으로 design conjectures와 theoretical conjectures 업데이트

---

## 7. Tentative Design Principles의 검증 계획

각 Design Principle의 검증은 다음과 같이 operationalize된다:

### DP1: 다중 대안 + T-Score 제시

| 검증 기준 | 측정 방법 | 지지 근거 | 기각 근거 |
|---|---|---|---|
| 선택 다양성 증가 | Shannon Entropy (pre > post) | entropy 유의미 증가 | entropy 변화 없음 |
| Modal recommendation 회피 | T>0.8 선택 비율 감소 | 비율 유의미 감소 | 비율 변화 없음 |
| T-Score 참조 행동 | 화면 녹화에서 T-Score 확인 빈도 | 빈번한 확인 | 무시 또는 혼란 |

### DP2: 시간 제한 없는 숙고

| 검증 기준 | 측정 방법 | 지지 근거 | 기각 근거 |
|---|---|---|---|
| Deliberation 질 | Think-Aloud의 reasoning 깊이 코딩 | 다면적 고려 증거 | 즉각적/피상적 선택 |
| 시간과 질의 관계 | Deliberation time × reasoning quality 상관 | 정적 상관 | 무상관 또는 부적 상관 |

### DP3: T-Score 근거 투명성

| 검증 기준 | 측정 방법 | 지지 근거 | 기각 근거 |
|---|---|---|---|
| 근거 이해도 | 인터뷰에서 T-Score 설명 정확도 | 정확한 설명 | 오해 또는 무이해 |
| 선택 정당화 질 | Decision Log의 근거 기술 분석 | 구체적, 맥락적 근거 | "AI가 추천해서" 수준 |

### DP4: 확장적 scaffold

| 검증 기준 | 측정 방법 | 지지 근거 | 기각 근거 |
|---|---|---|---|
| 기존 지식 활용 | Think-Aloud에서 선행 학습 참조 빈도 | 빈번한 연결 | AI 추천에만 의존 |
| AT expansive learning | Pre/Post 설계 비교 (관행 변화) | 새로운 접근 시도 + 학술적 정당화 | 기존 관행 유지 또는 AI 무비판적 수용 |

---

## 8. 반복 계획 (Iteration Plan)

### Cycle 1: 본 연구 (Pilot)

```
┌──────────────────────────────────────┐
│  N = 15-20                           │
│  대상: 사회과학 박사과정생             │
│  과제: 가상 시나리오 2개              │
│  Checkpoint: 3개 핵심 CP             │
│  기간: 약 16주 (4+4+8)              │
│                                      │
│  산출물:                             │
│  - Refined Design Principles         │
│  - AT Contradiction 분석 결과        │
│  - Conjectured Theory 수정/지지      │
│  - Diverga 개선 권고                 │
└──────────────────────────────────────┘
```

### Cycle 2: 후속 연구 (Validation)

```
┌──────────────────────────────────────┐
│  N = 30-40                           │
│  대상: 초기경력 연구자               │
│  과제: 실제 연구 프로젝트 적용        │
│  Checkpoint: 전체 CP                │
│                                      │
│  산출물:                             │
│  - Validated Design Principles       │
│  - AT Expansive Learning Model       │
│  - 다학문 비교 분석                  │
└──────────────────────────────────────┘
```

### Cycle 3: 확장 연구 (Generalization)

```
┌──────────────────────────────────────┐
│  Multi-site                          │
│  대상: 다학문 연구자                 │
│  과제: 실제 프로젝트 + 종단 추적      │
│                                      │
│  산출물:                             │
│  - Generalized Theory               │
│  - Implementation & Spread 가이드    │
│  - 정책 제언                         │
└──────────────────────────────────────┘
```

---

## 9. 연구의 강점과 한계 (Strengths & Limitations)

### 9.1 강점

**방법론적 강점:**
1. **EDR + AT + Conjecture Mapping의 통합**: 단순 도구 평가를 넘어, 설계 원리의 체계적 도출과 이론적 기여를 동시에 추구하는 rigorous한 프레임워크
2. **Mixed Methods 통합**: 양적(선택 다양성, deliberation time)과 질적(Think-Aloud, 인터뷰)의 상보적 결합으로 현상의 복합적 이해
3. **내장된 데이터 수집**: Diverga의 Decision Audit Trail이 연구 데이터 수집 인프라로 기능하여 생태학적 타당도 향상
4. **반복적 설계**: EDR의 iterative cycle이 design principles의 점진적 정교화를 보장

**이론적 강점:**
1. **Automation bias 완화 메커니즘의 실증**: 기존 연구가 주로 의료/법률 분야에서 다루었던 automation bias를 학술 연구 설계 맥락으로 확장
2. **Mode collapse의 학술적 영향 최초 검증**: VS 방법론이 연구 추천 맥락에서 실제로 다양성을 증가시키는지에 대한 첫 번째 사용자 연구
3. **Epistemic scaffold 개념의 도입**: Human checkpoint를 단순 승인 메커니즘이 아닌 인식론적 스캐폴드로 재개념화

**실천적 강점:**
1. **오픈소스 투명성**: Diverga의 코드가 공개되어 메커니즘의 완전한 검토 가능
2. **직접적 설계 개선**: 연구 결과가 Diverga의 checkpoint 설계에 즉시 반영 가능
3. **전이 가능한 design principles**: Diverga 특화이지만, 다른 AI 연구 도구 설계에도 적용 가능

### 9.2 한계

**방법론적 한계:**
1. **소표본**: 15-20명으로 양적 일반화에 한계. EDR의 특성상 일반화보다 이론적 전이를 목표로 하나, 이를 명시적으로 인정해야 함
2. **가상 시나리오**: 실제 연구 설계가 아닌 가상 과제를 사용하므로 생태학적 타당도의 제약. Cycle 2에서 실제 연구 적용으로 보완 예정
3. **참여자 편향**: CLI 환경 사용 가능자로 제한되어, 기술 리터러시가 높은 집단에 편중. 이는 Diverga의 현실적 사용자 프로파일을 반영하나, 일반화를 제약
4. **Hawthorne 효과**: Think-Aloud 과제 자체가 비판적 사고를 촉진할 수 있어, checkpoint의 순수 효과를 과대 추정할 가능성

**이론적 한계:**
1. **개발자-연구자 이중 역할**: Diverga 개발자가 연구를 수행하는 경우, 확증 편향(confirmation bias)의 위험. 외부 연구자 참여 또는 독립적 검증이 필요
2. **T-Score의 타당성**: T-Score가 실제 학술적 전형성을 정확히 반영하는지에 대한 독립적 검증 미비. 본 연구에서는 T-Score를 "주어진 도구 특성"으로 취급하고, 그 자체의 타당도 검증은 범위 외
3. **단일 도구 연구**: Diverga만을 대상으로 하여, checkpoint와 VS의 효과를 분리하기 어려움. 향후 component analysis 필요

**실천적 한계:**
1. **플랫폼 종속**: Claude Code 환경 필수로, 다른 LLM 사용자에게 확장 불가
2. **학습 곡선**: 44개 에이전트 시스템의 복잡성이 초기 사용 장벽. Pilot에서 에이전트를 제한하여 완화
3. **API 비용**: Claude API 사용 비용이 참여자에게 전가될 수 있음. 연구 예산에서 API 크레딧 제공 계획 필요

### 9.3 한계에 대한 대응 전략

| 한계 | 대응 전략 |
|---|---|
| 소표본 | EDR의 이론적 전이(theoretical transferability) 논리 명시; Cycle 2에서 표본 확대 |
| 가상 시나리오 | Within-subjects 설계로 개인차 통제; Cycle 2에서 실제 연구 적용 |
| 개발자-연구자 이중 역할 | 외부 연구 협력자의 독립적 코딩 검증; 반성적 연구자 저널 유지; 부정적 사례(negative cases) 적극 보고 |
| Hawthorne 효과 | 화면 녹화의 비침습적 행동 데이터와 Think-Aloud 데이터의 삼각화 |
| T-Score 타당성 | T-Score를 독립변수가 아닌 도구 특성으로 위치시키고, 참여자의 T-Score 해석에 초점 |
| Component analysis 부재 | AT의 contradiction 분석을 통해 checkpoint와 VS의 상호작용을 질적으로 분해 |

---

## 10. IRB/윤리적 고려사항

### 10.1 참여자 보호

| 이슈 | 대응 |
|---|---|
| **AI 생성 연구 설계의 학술적 정직성** | Diverga는 설계를 생성하지 않고 제안함 — checkpoint 로그가 human decision의 증거; 동의서에 명시 |
| **데이터 프라이버시** | Claude API로 전송되는 연구 데이터 범위를 동의서에 명시; 가상 시나리오 사용으로 실제 연구 아이디어 노출 방지 |
| **AI 의존성 형성 가능성** | Post-study debriefing에서 critical AI literacy 교육 포함; automation bias에 대한 자료 제공 |
| **참여자 부담** | 전체 참여 시간 약 3시간으로 제한; 중단 자유 보장 |
| **API 비용** | 연구 예산에서 API 크레딧 제공; 참여자에게 비용 전가 없음 |

### 10.2 연구자 윤리

| 이슈 | 대응 |
|---|---|
| **개발자-연구자 이중 역할** | 연구 방법 섹션에 역할 갈등(role conflict) 명시; 외부 검증자 참여 |
| **긍정적 결과 편향** | 부정적 사례(negative cases) 적극 보고; design principle의 기각 가능성 명시 |
| **도구 홍보 의도** | 연구 목적이 "도구 검증"이 아닌 "설계 원리 도출"임을 명확히; 한계를 솔직히 보고 |

---

## 11. 예상 기여 (Expected Contributions)

### 11.1 이론적 기여

1. **Epistemic Scaffold Theory**: AI 연구 도구의 human checkpoint를 인식론적 스캐폴드로 개념화하는 이론적 프레임워크 제안
2. **Mode Collapse의 학술적 영향**: VS 방법론이 연구 추천 맥락에서 다양성을 증가시키는 메커니즘의 경험적 이해
3. **AT의 AI-Mediated Research 적용**: Activity Theory를 AI-mediated research design 맥락에 적용한 프레임워크

### 11.2 실천적 기여

1. **Design Principles**: 다른 AI 연구 도구 개발자가 참조할 수 있는 경험적으로 검증된 설계 원리
2. **Checkpoint Granularity 가이드라인**: 얼마나 많은, 어떤 수준의 checkpoint가 효과적인지에 대한 근거
3. **Diverga 개선**: 연구 결과의 직접적 반영을 통한 시스템 개선

### 11.3 방법론적 기여

1. **EDR + AT + Conjecture Mapping 통합 모델**: AI 교육 도구 연구를 위한 방법론적 청사진
2. **Decision Audit Trail 활용**: AI 도구의 내장 로그를 연구 데이터로 활용하는 방법론적 선례

---

## 12. 연구 일정 (Timeline)

| 기간 | Phase | 활동 |
|---|---|---|
| 1-4주 | Phase 1: Analysis & Exploration | 문헌 분석, 도구 비교, 탐색적 인터뷰 |
| 5-8주 | Phase 2: Design & Construction | Intervention 설계, DP 도출, Conjecture Map 작성 |
| 9-10주 | Phase 3 준비 | 참여자 모집, IRB 승인, 파일럿 테스트 |
| 11-14주 | Phase 3: Evaluation & Reflection (데이터 수집) | Pre-task → 도구 소개 → Post-task → 인터뷰 |
| 15-18주 | Phase 3: Evaluation & Reflection (분석) | 양적/질적 분석, AT 분석, DP 검증 |
| 19-20주 | 종합 | Refined DP 도출, 논문 집필, Cycle 2 계획 |

---

## 13. 참고 문헌 (References)

### 이론적 프레임워크
- Engeström, Y. (2015). *Learning by expanding: An activity-theoretical approach to developmental research* (2nd ed.). Cambridge University Press.
- McKenney, S., & Reeves, T. C. (2019). *Conducting educational design research* (2nd ed.). Routledge.
- Sandoval, W. (2014). Conjecture mapping: An approach to systematic educational design research. *Journal of the Learning Sciences, 23*(1), 18-36. https://doi.org/10.1080/10508406.2013.778204
- Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and conducting mixed methods research* (3rd ed.). SAGE.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77-101.

### AI 윤리와 교육
- EDUCAUSE. (2025). AI ethical guidelines. https://library.educause.edu/resources/2025/6/ai-ethical-guidelines
- Guiding the future: Developing an ethical framework for generative AI use in education. (2024). *International Journal of Information and Learning Technology*. https://doi.org/10.1108/IJILT-06-2024-0113
- AI ethics literacy framework. (2025). *Scientific Reports*. https://doi.org/10.1038/s41598-025-21977-5

### Mode Collapse과 Verbalized Sampling
- Verbalized sampling: How to mitigate mode collapse and unlock LLM diversity. (2025). *arXiv:2510.01171*. https://arxiv.org/abs/2510.01171

### Human-in-the-Loop
- Human-in-the-loop systems for ethical AI. (2025). *ResearchGate*. https://www.researchgate.net/publication/393802734
- From human-in-the-loop to human-in-power. (2024). *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC11384285/
- Human in the loop: Interpretive and participatory AI in research. (2025). CUNY. https://gcdi.commons.gc.cuny.edu/2025/10/10/human-in-the-loop-interpretive-and-participatory-ai-in-research/

### Automation Bias
- Exploring automation bias in human-AI collaboration: A review and implications for explainable AI. (2025). *AI & Society*. https://doi.org/10.1007/s00146-025-02422-7
- AI tools in society: Impacts on cognitive offloading and the future of critical thinking. (2025). *Societies, 15*(1), 6. https://doi.org/10.3390/soc15010006
- Mitigating automation bias in generative AI through nudges. (2025). *ScienceDirect*. https://doi.org/10.1016/j.procs.2025.01.004
- Let me decide: Increasing user autonomy increases recommendation acceptance. (2024). *Computers in Human Behavior*. https://doi.org/10.1016/j.chb.2024.108122

### Activity Theory와 Human-AI Collaboration
- Exploring contradictions in human-AI collaboration in HEIs using activity theory. (2025). *AMCIS 2025 Proceedings*. https://aisel.aisnet.org/amcis2025/sig_aiaa/sig_aiaa/11/
- Rethinking the evaluation of educational intervention effectiveness through activity theory. (2025). *Frontiers in Education*. https://doi.org/10.3389/feduc.2025.1532376
- A model for using activity theory in educational design. *ERIC*. https://files.eric.ed.gov/fulltext/ED593834.pdf

### AI 연구 도구
- AI anxiety and adoption intention in higher education based on extended TAM-UTAUT. (2026). *Scientific Reports*. https://doi.org/10.1038/s41598-026-35823-9
- Extending TAM: Subjective norms, ethics, and trust in AI tool adoption. (2025). *Computers & Education: Artificial Intelligence*. https://doi.org/10.1016/j.caeai.2025.100190
- ASReview LAB v.2: Open-source text screening with multiple agents. (2025). *Cell Reports Methods*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12416088/
- Human-in-the-loop AI system for systematic literature review. (2025). *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12552804/

### Design-Based Research
- Educational design research for relevant and robust scholarship. (2025). *Journal of Computing in Higher Education*. https://doi.org/10.1007/s12528-025-09456-2
- Design-based research: A framework for participation and action. (2025). *SAGE*. https://doi.org/10.1177/19408447251387997
- Design and assessment of AI-based learning tools in higher education. (2025). *International Journal of Educational Technology in Higher Education*. https://doi.org/10.1186/s41239-025-00540-2

### 도구 비교
- Assessing the effectiveness of AI tools in literature review and research. (2026). *Canadian Journal of Information and Library Science, 49*(1). https://ojs.lib.uwo.ca/index.php/cjils/article/view/23075
- A scoping study of evaluation practices for responsible AI tools. (2024). *CHI Conference*. https://doi.org/10.1145/3613904.3642398

---

*이 연구 제안서는 2026년 2월 27일의 연구 설계 토론에 기반하여 작성되었으며, DISCUSSION 폴더의 RAW 토론 기록을 참조한다.*
