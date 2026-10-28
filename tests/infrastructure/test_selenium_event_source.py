from collections.abc import Iterator
from pathlib import Path

import pytest
from selenium import webdriver

from scraping_python_org.infrastructure.chrome import chrome_driver
from scraping_python_org.infrastructure.selenium_event_source import SeleniumEventSource

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "python_org_events.html"


@pytest.fixture(scope="module")
def driver() -> Iterator[webdriver.Chrome]:
    with chrome_driver() as chrome:
        yield chrome


@pytest.mark.browser
def test_fetch_events_reads_widget_items_only(driver: webdriver.Chrome) -> None:
    events = SeleniumEventSource(driver, FIXTURE.as_uri()).fetch_events()

    assert [event.name for event in events] == [
        "PyCon Alpha",
        "PyData Beta",
        "Django Gamma",
        "EuroPython Delta",
        "PyLadies Epsilon",
    ]
    assert events[0].time == "2026-11-02"
