from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)

# Service information
SERVICE_NAME = "observability"
SERVICE_VERSION = "1.0.0"

# Define the resource for this service
resource = Resource.create(
    {
        "service.name": SERVICE_NAME,
        "service.version": SERVICE_VERSION,
    }
)

# Create and configure the Tracer Provider
provider = TracerProvider(resource=resource)

# Export spans immediately to the terminal
processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Register the provider globally (only once)
try:
    trace.set_tracer_provider(provider)
except Exception:
    # Tracer provider is already registered
    pass

# Shared tracer instance
tracer = trace.get_tracer(SERVICE_NAME)


def get_tracer():
    """
    Returns the shared tracer instance.
    """
    return tracer


def shutdown_tracing():
    """
    Flushes any pending spans and shuts down the tracer provider.
    """
    provider.shutdown()