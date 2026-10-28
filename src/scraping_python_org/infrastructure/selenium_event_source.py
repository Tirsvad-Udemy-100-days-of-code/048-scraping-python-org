"""Selenium adapter for the EventSource port."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from scraping_python_org.domain.event import Event

EVENT_WIDGET_SELECTOR = ".event-widget"
EVENT_ITEM_SELECTOR = f"{EVENT_WIDGET_SELECTOR} li"


class SeleniumEventSource:
    """Reads the events from the event widget of a page."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Remember the driver and the page to read."""
        self._driver = driver
        self._url = url

    def fetch_events(self) -> list[Event]:
        """Open the page and return one Event per widget list item."""
        self._driver.get(self._url)
        items = self._driver.find_elements(By.CSS_SELECTOR, EVENT_ITEM_SELECTOR)
        return [
            Event(
                time=item.find_element(By.TAG_NAME, "time").text,
                name=item.find_element(By.TAG_NAME, "a").text,
            )
            for item in items
        ]
