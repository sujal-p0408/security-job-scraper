import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

df = pd.read_csv("data/raw/jobs.csv")

text = " ".join(df["job_text"]).lower()
words = re.findall(r"\b[a-zA-Z]+\b", text)

skills = [
    "python", "linux", "aws", "docker", "kubernetes",
    "security", "network", "http", "cloud", "automation"
]

counts = Counter(word for word in words if word in skills)

plt.figure(figsize=(8,4))
plt.bar(counts.keys(), counts.values())
plt.title("Most Requested Security Skills (Greenhouse Jobs)")
plt.ylabel("Frequency")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
