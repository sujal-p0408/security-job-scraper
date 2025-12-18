import pandas as pd
from collections import Counter
import re

# Load scraped job data
df = pd.read_csv("data/raw/jobs.csv")

text = df["job_text"].iloc[0].lower()

# Clean text
words = re.findall(r"\b[a-zA-Z]+\b", text)

keywords = Counter(words)

# Security-focused keywords
security_terms = [
    "python", "linux", "aws", "docker", "kubernetes",
    "network", "tcp", "http", "security", "cloud",
    "bash", "sql", "api", "automation"
]

filtered = {k: v for k, v in keywords.items() if k in security_terms}

print("Top Security Keywords:\n")
for k, v in filtered.items():
    print(f"{k}: {v}")
