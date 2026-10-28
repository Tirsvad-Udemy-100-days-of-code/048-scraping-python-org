"""Chrome WebDriver lifecycle."""

from collections.abc import Iterator
from contextlib import contextmanager

from selenium import webdriver

WINDOW_SIZE = "1280,1000"


@contextmanager
def chrome_driver(headless: bool = True) -> Iterator[webdriver.Chrome]:
    """Yield a Chrome driver (found by Selenium Manager) and always quit it."""
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument(f"--window-size={WINDOW_SIZE}")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
