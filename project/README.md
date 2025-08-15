# Retirement Portfolio Risk Alignment for Elderly Investors
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Many elderly investors are risk-averse and prefer stable, predictable returns to protect retirement savings. Yet their portfolios often contain a larger share of high-volatility assets than they realize, exposing them to drawdowns that can jeopardize spending needs. 

This project frames a stakeholder-centered approach to measure, monitor, and reduce that misalignment. It aims to make sure that the risk level of users' portfolios is within an acceptable range.

## Stakeholder & User
Primary stakeholder: Financial advisors/wealth managers specializing in retirees.  
End users: Elderly or near-retirement investors relying on investment income.  
Context: Advisors review portfolios monthly or after market shocks and need a quick way to flag excessive risk.

## Useful Answer & Decision
- Descriptive: Quantify share of high-volatility assets
- Metric: compute realized volatility, max drawdown, and 1-day/10-day VaR.  
- Artifact: “Investment Risk Alignment Report” (dashboard or md/pdf) that flags breaches and suggests reallocations. It can also visualize the report to help end-users gain a comprehensive understanding of their portfolio.
  
## Assumptions & Constraints
- Data availability: Public price data available for holdings (e.g., Yahoo Finance).  
- Latency: Daily updated stock prices are sufficient for retirees.  
- Capacity: single-machine Python workflow (pandas, numpy).

## Known Unknowns / Risks
- The market risk that can't be easily captured.  
- The correlation risk among different assets within the portfolio.
- Backtest bias; mitigation via walk-forward evaluation.

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Flag misaligned risk → **Stage 01** → Scoping paragraph + stakeholder memo  


## Repo Plan
`/data/` (raw, interim, processed) • `/src/` (metrics, risk buckets, loaders) • `/notebooks/` (EDA & reports) • `/docs/` (memo/slide). Weekly commits; tag milestones.
