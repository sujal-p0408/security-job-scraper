# Anti-Scraping & Bot-Defense Mechanisms

This project analyzes common anti-scraping mechanisms observed while scraping
Greenhouse-hosted career pages.

## 1. JavaScript Rendering Requirement
Greenhouse career pages are heavily JavaScript-driven.
Static HTTP requests return incomplete HTML where job descriptions are not present.

This acts as a soft anti-scraping layer against basic bots.

## 2. Rate Limiting
Multiple rapid requests can trigger HTTP 429 (Too Many Requests).
This indicates server-side rate limiting.

Mitigation:
- Requests are intentionally throttled.
- Scraping is performed at low frequency.

## 3. User-Agent Filtering
Requests with missing or default User-Agent headers may return incomplete or blocked responses.

Mitigation:
- Browser-like User-Agent is used.

## 4. CAPTCHA Detection
CAPTCHA challenges may be introduced if abnormal traffic is detected.

⚠️ This project does NOT attempt to bypass CAPTCHA mechanisms.
If CAPTCHA is encountered, scraping is halted.

## 5. IP-Based Controls
Repeated automated access from a single IP may trigger temporary blocking.

Mitigation:
- Limited scraping scope
- Single-session execution
