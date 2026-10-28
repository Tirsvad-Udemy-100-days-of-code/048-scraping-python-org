"""Port for anything that can supply upcoming events."""

from typing import Protocol

from scraping_python_org.domain.event import Event


class EventSource(Protocol):
    """Supplies upcoming events in page order."""

    def fetch_events(self) -> list[Event]:
        """Return the upcoming events."""
        ...
