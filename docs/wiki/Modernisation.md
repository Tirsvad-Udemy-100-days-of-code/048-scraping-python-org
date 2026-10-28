**English** · [Dansk](Modernisation-da) · [Bahasa Malaysia](Modernisation-ms)

# Modernisation

| Original solution | Modern solution | Why |
| --- | --- | --- |
| One `main.py` | Layers in `src/scraping_python_org` (domain, application, infrastructure, presentation) | Business rules do not depend on Selenium; the use case is tested with a fake |
| Long absolute XPath | CSS selector `.event-widget li` | Short, readable, survives layout changes |
| Manual counter `c` | `enumerate` | Less code, no off-by-one risk |
| `detach=True` followed by `driver.quit()` | Headless Chrome in a context manager that always quits | No stray browser windows, runs without a desktop |
| Unpinned `selenium` in `requirements.txt` | `pyproject.toml` with minimum versions | Reproducible installs |
| No tests | Unit tests plus a headless browser test on a saved page | Changes are safe |
| No type hints | `mypy --strict`, `ruff` | Errors found before running |

**What you gain:** a scraper you can change with confidence, the same idea
as the lecture but built the way a real project is.
