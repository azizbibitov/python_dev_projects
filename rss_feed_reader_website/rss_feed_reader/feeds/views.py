from django.shortcuts import render
from .forms import FeedReaderForm
from .utils import parse_rss_feed  # Import your custom RSS parser

def feed_reader(request):
    form = FeedReaderForm()
    all_feeds = []  # Store all parsed feeds here

    if request.method == 'POST':
        form = FeedReaderForm(request.POST)
        if form.is_valid():
            # Get the URLs from the form, split them into a list
            urls = form.cleaned_data['urls'].splitlines()

            # Loop through the list of URLs, parsing each one
            for url in urls:
                try:
                    feed = parse_rss_feed(url)  # Using your custom RSS parser
                    all_feeds.append(feed)  # Append the parsed feed
                except Exception as e:
                    # Handle parsing or network errors here
                    print(f"Error parsing {url}: {str(e)}")
                    continue

    return render(request, 'feed_reader.html', {'form': form, 'feeds': all_feeds})
