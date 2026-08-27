import time

from opentelemetry import trace


tracer = trace.get_tracer("multi-agent-observability")


# Store start times for active operations.
_agent_start_times = {}
_model_start_times = {}
_tool_start_times = {}


# ============================================================
# AGENT CALLBACKS
# ============================================================

def before_agent(callback_context):
    agent_name = callback_context.agent_name

    _agent_start_times[agent_name] = time.perf_counter()

    span = tracer.start_span(
        f"agent.{agent_name}"
    )

    span.set_attribute(
        "agent.name",
        agent_name,
    )

    # Store the span in the callback context
    # so the corresponding after callback can end it.
    callback_context.state["_otel_agent_span"] = span

    span.__enter__()

    return None


def after_agent(callback_context):
    agent_name = callback_context.agent_name

    start_time = _agent_start_times.pop(
        agent_name,
        None,
    )

    span = callback_context.state.pop(
        "_otel_agent_span",
        None,
    )

    if start_time is not None:
        duration = time.perf_counter() - start_time

        if span is not None:
            span.set_attribute(
                "agent.latency_ms",
                duration * 1000,
            )

    if span is not None:
        span.__exit__(None, None, None)

    return None


# ============================================================
# MODEL CALLBACKS
# ============================================================

def before_model(callback_context, llm_request):
    agent_name = callback_context.agent_name

    _model_start_times[agent_name] = time.perf_counter()

    span = tracer.start_span("llm.call")

    span.set_attribute(
        "agent.name",
        agent_name,
    )

    model_name = getattr(
        llm_request,
        "model",
        None,
    )

    if model_name:
        span.set_attribute(
            "llm.model",
            str(model_name),
        )

    callback_context.state["_otel_model_span"] = span

    span.__enter__()

    return None


def after_model(callback_context, llm_response):
    agent_name = callback_context.agent_name

    start_time = _model_start_times.pop(
        agent_name,
        None,
    )

    span = callback_context.state.pop(
        "_otel_model_span",
        None,
    )

    if start_time is not None and span is not None:
        duration = time.perf_counter() - start_time

        span.set_attribute(
            "llm.latency_ms",
            duration * 1000,
        )

    # Capture token usage when available.
    usage = getattr(
        llm_response,
        "usage_metadata",
        None,
    )

    if usage is not None and span is not None:

        for attribute, field in [
            (
                "llm.input_tokens",
                "prompt_token_count",
            ),
            (
                "llm.output_tokens",
                "candidates_token_count",
            ),
            (
                "llm.total_tokens",
                "total_token_count",
            ),
        ]:
            value = getattr(
                usage,
                field,
                None,
            )

            if value is not None:
                span.set_attribute(
                    attribute,
                    int(value),
                )

    if span is not None:
        span.__exit__(None, None, None)

    return None


def on_model_error(
    callback_context,
    llm_request,
    error,
):
    agent_name = callback_context.agent_name

    span = callback_context.state.pop(
        "_otel_model_span",
        None,
    )

    if span is not None:
        span.record_exception(error)
        span.set_status(
            trace.Status(
                trace.StatusCode.ERROR,
                str(error),
            )
        )
        span.__exit__(
            type(error),
            error,
            error.__traceback__,
        )

    _model_start_times.pop(
        agent_name,
        None,
    )

    return None


# ============================================================
# TOOL CALLBACKS
# ============================================================

def before_tool(tool, tool_args, callback_context):
    agent_name = callback_context.agent_name
    tool_name = getattr(
        tool,
        "name",
        str(tool),
    )

    key = f"{agent_name}:{tool_name}"

    _tool_start_times[key] = time.perf_counter()

    span = tracer.start_span(
        f"tool.{tool_name}"
    )

    span.set_attribute(
        "agent.name",
        agent_name,
    )

    span.set_attribute(
        "tool.name",
        tool_name,
    )

    callback_context.state[
        f"_otel_tool_span_{tool_name}"
    ] = span

    span.__enter__()

    return None


def after_tool(
    tool,
    tool_args,
    callback_context,
    tool_response,
):
    agent_name = callback_context.agent_name
    tool_name = getattr(
        tool,
        "name",
        str(tool),
    )

    key = f"{agent_name}:{tool_name}"

    start_time = _tool_start_times.pop(
        key,
        None,
    )

    span = callback_context.state.pop(
        f"_otel_tool_span_{tool_name}",
        None,
    )

    if start_time is not None and span is not None:
        duration = time.perf_counter() - start_time

        span.set_attribute(
            "tool.latency_ms",
            duration * 1000,
        )

    if span is not None:
        span.__exit__(None, None, None)

    return None


def on_tool_error(
    tool,
    tool_args,
    callback_context,
    error,
):
    tool_name = getattr(
        tool,
        "name",
        str(tool),
    )

    span = callback_context.state.pop(
        f"_otel_tool_span_{tool_name}",
        None,
    )

    if span is not None:
        span.record_exception(error)
        span.set_status(
            trace.Status(
                trace.StatusCode.ERROR,
                str(error),
            )
        )

        span.__exit__(
            type(error),
            error,
            error.__traceback__,
        )

    return None