from playwright.sync_api import sync_playwright
import pandas as pd

URL = "https://www.greenhouse.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        user_agent="Mozilla/5.0"
    )

    page.goto(URL, timeout=60000)
    page.wait_for_timeout(5000)

    job_text = page.inner_text("body")

    data = [{"job_text": job_text}]
    df = pd.DataFrame(data)

    df.to_csv("data/raw/jobs.csv", index=False)

    browser.close()

print("Scraping complete")
