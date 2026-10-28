import dataclasses

import pytest

from scraping_python_org.domain.event import Event


def test_to_dict_returns_time_and_name() -> None:
    assert Event("2026-11-02", "PyCon").to_dict() == {"time": "2026-11-02", "name": "PyCon"}


def test_event_is_immutable() -> None:
    event = Event("2026-11-02", "PyCon")
    with pytest.raises(dataclasses.FrozenInstanceError):
        event.name = "Other"  # type: ignore[misc]
