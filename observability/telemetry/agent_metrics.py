import time

from telemetry.tracing import get_tracer

tracer = get_tracer()


def record_agent_start(agent_name):
    span = tracer.start_span(f"{agent_name}_start")
    span.set_attribute("agent.name", agent_name)
    return span


def record_agent_end(span):
    span.end()


def record_execution_time(agent_name, start_time):
    duration = time.time() - start_time

    with tracer.start_as_current_span(
        f"{agent_name}_execution_time"
    ) as span:
        span.set_attribute(
            "execution_time_seconds",
            duration
        )

    return duration


def record_error(agent_name, error):
    with tracer.start_as_current_span(
        f"{agent_name}_error"
    ) as span:
        span.set_attribute(
            "error.message",
            str(error)
        )


def record_retry(agent_name):
    with tracer.start_as_current_span(
        f"{agent_name}_retry"
    ) as span:
        span.set_attribute(
            "retry",
            True
        )


def record_agent_hop(from_agent, to_agent):
    with tracer.start_as_current_span(
        "agent_hop"
    ) as span:
        span.set_attribute(
            "from_agent",
            from_agent
        )
        span.set_attribute(
            "to_agent",
            to_agent
        )


def record_llm_call(agent_name, model_name):
    with tracer.start_as_current_span(
        "llm_call"
    ) as span:
        span.set_attribute(
            "agent",
            agent_name
        )
        span.set_attribute(
            "model",
            model_name
        )


def record_tool_call(agent_name, tool_name):
    with tracer.start_as_current_span(
        "tool_call"
    ) as span:
        span.set_attribute(
            "agent",
            agent_name
        )
        span.set_attribute(
            "tool",
            tool_name
        )