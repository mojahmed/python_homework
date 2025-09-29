from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# get the chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Loading 
url = "https://owasp.org/www-project-top-ten/"
driver.get(url)
time.sleep(5) 


# Find Top 10 items (title + link)
items = driver.find_elements(By.XPATH, "//a[starts-with(@href,'https://owasp.org/Top10/A')]")
print( len(items), "entries")

results = []
for item in items:
    title = item.text.strip()
    link = item.get_attribute("href")
    if title and link:
        results.append({"Title": title, "Link": link})


# create DataFrame and saveCSV
df = pd.DataFrame(results)
print("\n DataFrame:")
print(df)

df.to_csv("owasp_top_10.csv", index=False)


driver.quit()
