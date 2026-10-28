**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Day 48 – Scraping python.org with Selenium

In this lecture we use Selenium to read the five upcoming events from
[python.org](https://www.python.org/) and organise them in a dictionary:

```python
{0: {"time": "2026-10-29", "name": "PyConFR 2026"}, 1: {...}, ...}
```

## Pages

- [Lecture steps](Lecture-Steps): the four steps, each with a screenshot and what you gain from it.
- [Modernisation](Modernisation): what changed from the original solution and why.

## What you gain in this lecture

- You read a web page's HTML structure with the browser's inspector.
- You choose locators (`By.CSS_SELECTOR`, `By.TAG_NAME`) that are short and stable.
- You turn scraped elements into clean, structured Python data.
