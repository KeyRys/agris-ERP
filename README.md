# AgroLogix ERP

AgroLogix is a backend-first ERP system designed to model an agribusiness
operation with production, inventory, logistics, and accounting.

## Scope

- Production batches and harvest cycles
- Inventory valuation (average cost)
- Logistics and delivery cost allocation
- Double-entry accounting
- Simulation layer for stress testing business logic

## Non-Goals

- Game mechanics
- Visual storytelling
- Payroll, tax, depreciation
- Over-engineered accounting

## Architecture

Simulation consumes the ERP.
ERP does not depend on simulation.
Accounting is authoritative.

## Status

Initialization phase.