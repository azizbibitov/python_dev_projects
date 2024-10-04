import feedparser

# Ask for RSS feed URL
rss_url = input("Enter the RSS feed URL: ")

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Display feed title and description
print(f"\nFeed Title: {feed.feed.title}")
print(f"Feed Description: {feed.feed.description}")

# Display all the feed entries
print("\nArticles:")
for entry in feed.entries:
    print(f"\nTitle: {entry.title}")
    print(f"Description: {entry.description}")
    print(f"Link: {entry.link}")
