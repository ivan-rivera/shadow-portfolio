# Agentic Portfolio Manager (Paper Trading)

## Overview

This project is an **agentic portfolio management system** that autonomously researches markets, proposes trades, applies risk controls, and executes trades on a **paper trading account**. It operates on a scheduled basis (e.g., daily or intraday), with optional **human-in-the-loop approval** for higher-risk decisions.

The system is designed to simulate the behavior of a **disciplined portfolio manager**, combining:
- Deterministic risk and portfolio rules
- LLM-driven market research and trade reasoning
- Automated execution via broker APIs
- Persistent memory and evaluation for continuous improvement

Primary goals:
- Explore agentic decision-making in trading
- Build a realistic, auditable portfolio management workflow
- Evaluate decision quality beyond raw PnL
- Serve as a research + engineering sandbox for LLM-driven finance

---

## High-Level Workflow

1. **Scheduler triggers a run** (cron or task queue)
2. **Market & portfolio data ingestion**
3. **LLM-based research & synthesis**
4. **Trade proposal generation**
5. **Deterministic risk & constraint filtering**
6. **Execution OR escalation for human approval**
7. **Logging, memory storage, and evaluation**

---

## System Architecture

### Core Components

**Execution & Orchestration**
- Python-based service
- Dockerized deployment
- Cron or task scheduler (e.g., cron, Celery Beat, Temporal)

**LLM Layer**
- Market research summaries
- Trade thesis generation
- Risk and confidence estimation
- Structured trade proposal output (JSON)

**Broker / Paper Trading**
- Primary candidate: Alpaca Paper Trading
- Alternative: IBKR Paper Trading
- Optional: Custom simulated paper broker

**Storage & Memory**
- PostgreSQL (portfolio state, trades, logs)
- Mem0 (long-term agent memory / episodic recall)

**Evaluation & Monitoring**
- BrainTrust (decision evaluation, outcome analysis)
- Custom analytics for:
  - Performance metrics
  - Decision quality
  - Risk adherence
  - Behavioral patterns

**Human-in-the-Loop Interface**
- Telegram bot for:
  - Trade approvals
  - Overrides
  - Alerts
  - Audit trail

**Visualization**
- TradingView integration (if supported)
- Optional custom dashboard (Streamlit / Next.js)

---

## Trading Logic & Safety Model

### LLM Responsibilities
- Market summary
- Asset-level bull / bear thesis
- Confidence estimation
- Trade proposal generation

### Deterministic (Non-LLM) Controls
Hard constraints enforced outside the model:
- Max position size per asset
- Max sector exposure
- Max portfolio drawdown
- Volatility limits
- Correlation limits
- Liquidity constraints
- Trade frequency limits

### Trade Decision Flow

```text
LLM Proposal
    ↓
Risk Engine (Hard Rules)
    ↓
Safe → Execute Automatically
Borderline → Request Human Approval (Telegram)
Unsafe → Reject & Log
```

### Example Trade Proposal Schema

```json
{
  "symbol": "AAPL",
  "action": "BUY",
  "position_size_pct": 0.06,
  "reason": "Earnings momentum and improving margins",
  "confidence": 0.72,
  "risk_level": "medium",
  "expected_upside_pct": 4.5,
  "worst_case_loss_pct": 2.3,
  "time_horizon_days": 14
}
```


## Evaluation Metrics

### Portfolio Performance

- CAGR
- Sharpe / Sortino
- Max drawdown
- Hit rate
- Profit factor

### Decision Quality

- Thesis vs outcome alignment
- Confidence calibration
- Regret analysis (missed vs taken trades)
- Timing efficiency

### Behavioral Signals (Agent Profiling)

- Overtrading frequency
- Risk rule violations
- Late exits / early exits
- Human override rate
- Bias pattern detection
