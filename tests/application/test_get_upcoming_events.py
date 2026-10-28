from scraping_python_org.application.get_upcoming_events import get_upcoming_events
from scraping_python_org.domain.event import Event


class FakeEventSource:
    def __init__(self, events: list[Event]) -> None:
        self._events = events

    def fetch_events(self) -> list[Event]:
        return self._events


def _events(count: int) -> list[Event]:
    return [Event(f"11-{i:02d}", f"Event {i}") for i in range(count)]


def test_get_upcoming_events_numbers_events_from_zero() -> None:
    result = get_upcoming_events(FakeEventSource(_events(2)))

    assert result == {
        0: {"time": "11-00", "name": "Event 0"},
        1: {"time": "11-01", "name": "Event 1"},
    }


def test_get_upcoming_events_limits_to_five_by_default() -> None:
    assert list(get_upcoming_events(FakeEventSource(_events(8)))) == [0, 1, 2, 3, 4]


def test_get_upcoming_events_honours_custom_limit() -> None:
    assert len(get_upcoming_events(FakeEventSource(_events(8)), limit=3)) == 3


def test_get_upcoming_events_returns_empty_dict_without_events() -> None:
    assert get_upcoming_events(FakeEventSource([])) == {}
