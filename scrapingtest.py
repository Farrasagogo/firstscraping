import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the webpage
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the data
# Example: Scrape the masthead text
masthead_text = soup.find('header', class_='masthead').text.strip()

# Similarly, scrape other data as needed

# Create a DataFrame with the scraped data
data = {
    'Masthead': [masthead_text],
    # Add other scraped data here
}

df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
excel_file = 'scraped_data.xlsx'
df.to_excel(excel_file, index=False)

print("Data has been scraped and saved to", excel_file)
