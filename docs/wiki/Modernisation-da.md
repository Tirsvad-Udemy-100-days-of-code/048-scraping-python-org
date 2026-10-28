[English](Modernisation) | **Dansk** | [Bahasa Malaysia](Modernisation-ms)

# Modernisering

| Oprindelig løsning | Moderne løsning | Hvorfor |
| --- | --- | --- |
| Én `main.py` | Lag i `src/scraping_python_org` (domain, application, infrastructure, presentation) | Forretningsreglerne afhænger ikke af Selenium; use casen testes med en fake |
| Lang absolut XPath | CSS-selector `.event-widget li` | Kort, læsbar, tåler ændringer i layoutet |
| Manuel tæller `c` | `enumerate` | Mindre kode, ingen fejl med off-by-one |
| `detach=True` efterfulgt af `driver.quit()` | Headless Chrome i en context manager, der altid lukker | Ingen efterladte browservinduer, kører uden skrivebord |
| `selenium` uden version i `requirements.txt` | `pyproject.toml` med minimumsversioner | Reproducerbare installationer |
| Ingen tests | Enhedstests og en headless browsertest på en gemt side | Ændringer er trygge |
| Ingen typeannotationer | `mypy --strict`, `ruff` | Fejl findes før kørsel |

**Hvad du får ud af det:** en scraper, du kan ændre med ro i sindet; samme idé
som i lektionen, men bygget som et rigtigt projekt.
