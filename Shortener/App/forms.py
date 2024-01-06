from django import forms
from .models import URLShortener


class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortener
        fields = '__all__' #['original_url','short_url','created_at','click_count']
