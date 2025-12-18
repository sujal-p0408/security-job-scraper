# DOM & JavaScript Rendering

Greenhouse career pages use a JavaScript-heavy frontend.

## Static vs Dynamic Content
- Static scrapers retrieve raw HTML
- Job descriptions are injected into the DOM after JavaScript execution

## DOM Lifecycle
1. Initial HTML load
2. JavaScript execution
3. API calls (XHR / Fetch)
4. DOM updates

## Implication for Scraping
Traditional scraping tools fail because:
- Content does not exist at initial load
- Requires a real browser environment

Playwright was used to execute JavaScript and extract rendered DOM content.
