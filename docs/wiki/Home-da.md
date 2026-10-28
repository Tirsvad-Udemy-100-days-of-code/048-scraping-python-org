[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Dag 48 – Scraping af python.org med Selenium

I denne lektion bruger vi Selenium til at læse de fem kommende begivenheder på
[python.org](https://www.python.org/) og samle dem i en dictionary:

```python
{0: {"time": "2026-10-29", "name": "PyConFR 2026"}, 1: {...}, ...}
```

## Sider

- [Lektionens trin](Lecture-Steps-da): de fire trin, hver med et skærmbillede og hvad du får ud af det.
- [Modernisering](Modernisation-da): hvad der er ændret i forhold til den oprindelige løsning, og hvorfor.

## Hvad du får ud af denne lektion

- Du læser en websides HTML-struktur med browserens inspektionsværktøj.
- Du vælger locators (`By.CSS_SELECTOR`, `By.TAG_NAME`), der er korte og stabile.
- Du omsætter scrapede elementer til ren, struktureret Python-data.
