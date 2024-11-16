import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the Artemis site
base_url = "https://artemis.bm"

# URL of the main directory page
directory_url = f"{base_url}/deal-directory/"

# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Step 1: Fetch the main directory page and extract the first 5 links
response = requests.get(directory_url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch the main page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

# Find the table in the main page
table = soup.find("table")  # Ensure this is the correct selector

# Extract the first 5 links from the table
rows = table.find_all("tr")[1:]  # Skip the header row
bond_links = [row.find("a")["href"] for row in rows if row.find("a")][:100]

print(f"Found {len(bond_links)} bond links: {bond_links}")

# Step 2: Visit each link and extract data from the 'info-box' div
all_bond_data = []
for link in bond_links:
    print(f"Scraping data from: {link}")
    detail_response = requests.get(link, headers=headers)

    if detail_response.status_code != 200:
        print(f"Failed to fetch details from {link}")
        continue

    detail_soup = BeautifulSoup(detail_response.content, "html.parser")

    # Find the div with id "info-box"
    info_box = detail_soup.find("div", id="info-box")
    if not info_box:
        print(f"No info-box found on {link}")
        continue

    # Extract the <ul> and its <li> values inside the info-box
    ul = info_box.find("ul")
    if not ul:
        print(f"No <ul> found in info-box on {link}")
        continue

    li_values = [li.text.strip() for li in ul.find_all("li")]

    # Save the data
    all_bond_data.append({"url": link, "details": li_values})

# Step 3: Save the data to a CSV
df = pd.DataFrame(all_bond_data)
df.to_csv("info_box_bond_data.csv", index=False)

print("Data scraping complete. Saved to info_box_bond_data.csv.")
