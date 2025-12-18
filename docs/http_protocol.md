# Understanding HTTP Protocol

This project relies on HTTP-based communication between client and server.

## HTTP Methods
- GET: Used to retrieve job pages and resources
- POST: Observed in internal API calls used by the frontend

## HTTP Headers
Important headers observed:
- User-Agent: Used by servers to identify clients
- Accept / Accept-Language: Content negotiation
- Cookie: Session and tracking identifiers

## HTTP Status Codes
- 200 OK – Successful request
- 403 Forbidden – Possible bot detection or blocking
- 429 Too Many Requests – Rate limiting
- 301 / 302 – Redirect-based bot control

## HTTPS
All Greenhouse pages enforce HTTPS, ensuring data integrity and confidentiality.
