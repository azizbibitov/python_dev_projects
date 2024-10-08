from django import forms

class FeedReaderForm(forms.Form):
    urls = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter URLs, one per line'}),
        help_text="Input multiple URLs, each on a new line."
    )
