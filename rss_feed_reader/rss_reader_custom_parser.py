import requests
import xml.etree.ElementTree as ET

# Ask for the RSS feed URL
rss_url = input("Enter the RSS feed URL: ")

# Fetch the RSS feed
response = requests.get(rss_url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch RSS feed.")
    exit()

# Parse the XML content
root = ET.fromstring(response.content)

# Helper function to get text from XML element
def get_text_or_default(elem, default=""):
    return elem.text if elem is not None else default

# Find the channel element (the main container for the feed)
channel = root.find('channel')

# Extract and print feed title and description
feed_title = get_text_or_default(channel.find('title'))
feed_description = get_text_or_default(channel.find('description'))

print(f"\nFeed Title: {feed_title}")
print(f"Feed Description: {feed_description}")

# Extract and print each item (article) in the feed
print("\nArticles:")
for item in channel.findall('item'):
    title = get_text_or_default(item.find('title'))
    description = get_text_or_default(item.find('description'))
    link = get_text_or_default(item.find('link'))

    print(f"\nTitle: {title}")
    print(f"Description: {description}")
    print(f"Link for Aziz: {link}")
