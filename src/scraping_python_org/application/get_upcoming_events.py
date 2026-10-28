"""Use case: list the upcoming events as a numbered dictionary."""

from scraping_python_org.application.event_source import EventSource

DEFAULT_LIMIT = 5


def get_upcoming_events(
    source: EventSource, limit: int = DEFAULT_LIMIT
) -> dict[int, dict[str, str]]:
    """Return up to ``limit`` events as ``{index: {"time": ..., "name": ...}}``."""
    events = source.fetch_events()[:limit]
    return {index: event.to_dict() for index, event in enumerate(events)}
