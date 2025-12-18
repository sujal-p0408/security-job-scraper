import requests

URL = "https://boards.greenhouse.io"

resp = requests.get(URL)
headers = resp.headers

security_headers = {
    "Content-Security-Policy": "❌ Missing",
    "Strict-Transport-Security": "❌ Missing",
    "X-Frame-Options": "❌ Missing",
    "X-Content-Type-Options": "❌ Missing",
    "Referrer-Policy": "❌ Missing"
}

for h in security_headers:
    if h in headers:
        security_headers[h] = "✅ Present"

print("Security Header Assessment:\n")
for k, v in security_headers.items():
    print(f"{k}: {v}")
