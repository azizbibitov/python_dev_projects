import requests
import xml.etree.ElementTree as ET

# Helper function to get text from XML element
def get_text_or_default(elem, default=""):
    return elem.text if elem is not None else default

def parse_rss_feed(rss_url):
    # Fetch the RSS feed
    response = requests.get(rss_url)

    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch RSS feed from {rss_url}")

    # Parse the XML content
    root = ET.fromstring(response.content)

    # Find the channel element (the main container for the feed)
    channel = root.find('channel')

    # Extract feed title and description
    feed_title = get_text_or_default(channel.find('title'))
    feed_description = get_text_or_default(channel.find('description'))

    # Extract each item (article) in the feed
    articles = []
    for item in channel.findall('item'):
        title = get_text_or_default(item.find('title'))
        description = get_text_or_default(item.find('description'))
        link = get_text_or_default(item.find('link'))

        articles.append({
            'title': title,
            'description': description,
            'link': link
        })

    # Return the parsed feed data
    return {
        'title': feed_title,
        'description': feed_description,
        'entries': articles
    }
