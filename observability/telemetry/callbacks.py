import time

from .agent_metrics import (
    record_agent_start,
    record_agent_end,
    record_execution_time,
    record_error,
)

# Temporary in-memory storage
_active_spans = {}
_start_times = {}


def before_agent(callback_context):
    agent = callback_context.agent_name

    _active_spans[agent] = record_agent_start(agent)
    _start_times[agent] = time.time()


def after_agent(callback_context):
    agent = callback_context.agent_name

    start_time = _start_times.pop(agent, None)
    span = _active_spans.pop(agent, None)

    if start_time is not None:
        record_execution_time(agent, start_time)

    if span is not None:
        record_agent_end(span)


def on_model_error(callback_context, request, error):
    record_error(
        callback_context.agent_name,
        error,
    )

    return None