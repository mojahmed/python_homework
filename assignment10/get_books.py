from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import os

# Start the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

# Wait until the book entries are loaded (up to 10 seconds)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.cp-search-result-item"))
    )
except Exception as e:
    print("Error: page did not load properly:", e)

# Find all book entries
entries = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
print(len(entries), "entries")

results = []

for entry in entries:
    # Title
    try:
        title_elem = entry.find_element(By.CSS_SELECTOR, "h2.cp-title a span.title-content")
        title = title_elem.text.strip()
    except Exception as e:
        print("Error fetching title:", e)
        title = "N/A"

    # Authors
    try:
        author_elems = entry.find_elements(By.CSS_SELECTOR, "span.cp-author-link a.author-link")
        if author_elems:
            author = "; ".join([a.text.strip() for a in author_elems])
        else:
            author = "N/A"
    except Exception as e:
        print("Error fetching author:", e)
        author = "N/A"

    # Format and Year
    try:
        fy_elem = entry.find_element(By.CSS_SELECTOR, "span.display-info-primary")
        format_year = fy_elem.text.strip()
    except Exception as e:
        print("Error fetching format/year:", e)
        format_year = "N/A"

    # Append to results list
    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

# Create DataFrame
df = pd.DataFrame(results)
print("\nDataFrame:")
print(df)

# Save files in same folder as script
base_folder = os.path.dirname(os.path.abspath(__file__))  
csv_path = os.path.join(base_folder, "get_books.csv")
json_path = os.path.join(base_folder, "get_books.json")

# Write CSV
df.to_csv(csv_path, index=False)

# Write JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"\nFiles saved in:\n- {csv_path}\n- {json_path}")

driver.quit()
