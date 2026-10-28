"""Capture one screenshot per lecture step into docs/screenshots/.

Run with ``python -m scraping_python_org.presentation.screenshots``.
"""

import html
import logging
from pathlib import Path
from urllib.parse import quote

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from scraping_python_org.application.get_upcoming_events import get_upcoming_events
from scraping_python_org.infrastructure.chrome import chrome_driver
from scraping_python_org.infrastructure.selenium_event_source import (
    EVENT_ITEM_SELECTOR,
    EVENT_WIDGET_SELECTOR,
    SeleniumEventSource,
)
from scraping_python_org.presentation.cli import PYTHON_ORG_URL

logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).resolve().parents[3] / "docs" / "screenshots"
HIGHLIGHT_SCRIPT = (
    "document.querySelectorAll(arguments[0])"
    ".forEach(li => { li.style.outline = '3px solid red'; });"
)
OUTPUT_PAGE = (
    "<html><body style='margin:0;background:#fff'>"
    "<pre style='display:inline-block;font:18px Consolas,monospace;"
    "white-space:pre-wrap;margin:0;padding:24px'>{text}</pre>"
    "</body></html>"
)


def _render_text(driver: WebDriver, text: str, path: Path) -> None:
    """Screenshot ``text`` rendered in a <pre> block."""
    page = OUTPUT_PAGE.format(text=html.escape(text))
    driver.get("data:text/html;charset=utf-8," + quote(page))
    driver.find_element(By.TAG_NAME, "pre").screenshot(str(path))


def capture(output_dir: Path = OUTPUT_DIR) -> list[Path]:
    """Write the four lecture screenshots and return their paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    home = output_dir / "01-python-org-home.png"
    widget = output_dir / "02-event-widget.png"
    highlighted = output_dir / "03-event-list-highlighted.png"
    output = output_dir / "04-output-dictionary.png"
    with chrome_driver() as driver:
        events = get_upcoming_events(SeleniumEventSource(driver, PYTHON_ORG_URL))
        driver.save_screenshot(str(home))
        driver.find_element(By.CSS_SELECTOR, EVENT_WIDGET_SELECTOR).screenshot(str(widget))
        driver.execute_script(HIGHLIGHT_SCRIPT, EVENT_ITEM_SELECTOR)
        driver.find_element(By.CSS_SELECTOR, EVENT_WIDGET_SELECTOR).screenshot(str(highlighted))
        _render_text(driver, str(events), output)
    paths = [home, widget, highlighted, output]
    for path in paths:
        logger.info("wrote %s", path)
    return paths


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    capture()
