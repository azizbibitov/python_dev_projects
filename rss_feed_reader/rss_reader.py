import feedparser

# Get multiple RSS feed URLs
rss_urls = input("Enter the RSS feed URLs (separated by commas): ").split(',')

for rss_url in rss_urls:
    rss_url = rss_url.strip()
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
