[English](Lecture-Steps) | **Dansk** | [Bahasa Malaysia](Lecture-Steps-ms)

# Lektionens trin

## Trin 1 - Åbn siden

![Forsiden på python.org](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-python-org/raw/branch/main/docs/screenshots/01-python-org-home.png)

`driver.get("https://www.python.org/")` indlæser siden i Chrome.

**Hvad du får ud af det:** driveren er din fjernbetjening til en rigtig browser.
Den skal altid lukkes igen, så den moderne kode bruger `try/finally`.

## Trin 2 - Find widgetten med inspektionsværktøjet

![Widgetten Upcoming Events](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-python-org/raw/branch/main/docs/screenshots/02-event-widget.png)

Højreklik på widgetten og vælg *Inspect*. Begivenhederne ligger i et element med
klassen `event-widget`; hver begivenhed er en `li` med et `time`- og et `a`-tag.

**Hvad du får ud af det:** du lærer at læse HTML-træet og finde den beholder,
der rummer præcis de data, du vil have.

## Trin 3 - Vælg de fem listepunkter med en CSS-selector

![De fem listepunkter markeret med rødt](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-python-org/raw/branch/main/docs/screenshots/03-event-list-highlighted.png)

`driver.find_elements(By.CSS_SELECTOR, ".event-widget li")` returnerer de fem
punkter. En klassebaseret selector er kortere og mere stabil end den lange
XPath, man kopierer fra inspektøren, og den rammer ikke urelaterede links.

**Hvad du får ud af det:** du kender Seleniums locator-strategier og ved,
hvornår CSS-selectors slår XPath.

## Trin 4 - Byg dictionary'en

![Den udskrevne dictionary](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-python-org/raw/branch/main/docs/screenshots/04-output-dictionary.png)

For hvert punkt læser vi `time` og `a` og gemmer dem under punktets indeks, med
`enumerate` i stedet for en manuel tæller.

**Hvad du får ud af det:** du omsætter sideelementer til struktureret data: en
dictionary af dictionaries, klar til brug i resten af et program.
