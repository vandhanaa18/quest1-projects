# AI Observability Platform

## Overview

This project implements observability for a multi-agent workflow.

## Architecture

Planner Agent
↓
Research Agent
↓
Code Generator Agent
↓
Reviewer Agent
↓
Test Agent

## Agents

- Planner Agent
- Research Agent
- Code Generator Agent
- Reviewer Agent
- Test Agent

## Workflow

Task → Planner → Research → Code Generator → Reviewer → Test

## Shared Memory

WorkflowData is used as shared memory between agents.

## Retry Mechanism

Agents are executed using retry logic.

## Error Handling

Errors are stored in workflow.errors.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```