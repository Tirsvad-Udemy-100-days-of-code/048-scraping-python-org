"""Command line entry point and composition root."""

from scraping_python_org.application.get_upcoming_events import get_upcoming_events
from scraping_python_org.infrastructure.chrome import chrome_driver
from scraping_python_org.infrastructure.selenium_event_source import SeleniumEventSource

PYTHON_ORG_URL = "https://www.python.org/"


def main() -> int:
    """Scrape the upcoming events from python.org and print them."""
    with chrome_driver() as driver:
        source = SeleniumEventSource(driver, PYTHON_ORG_URL)
        events = get_upcoming_events(source)
    print(events)
    return 0
