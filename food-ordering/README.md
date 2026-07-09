# Food Ordering System

## Overview

The Food Ordering System is a rule-based multi-agent application developed using Google ADK. It simulates the complete food ordering workflow through multiple specialized agents.

## Project Structure

```
food-ordering/
├── food_ordering_app/
├── order_management_agent/
├── payment_verification_agent/
├── restaurant_recommendation_agent/
├── delivery_tracking_agent/
├── shared/
├── main.py
└── requirements.txt
```

## Agents

- Restaurant Recommendation Agent – Recommends restaurants based on user preferences.
- Order Management Agent – Handles order creation and management.
- Payment Verification Agent – Verifies payment status.
- Delivery Tracking Agent – Tracks delivery updates.

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```