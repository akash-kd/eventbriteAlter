from django import forms
import datetime

class postForm(forms.Form):
    event_name = forms.CharField(max_length=200)
    data = forms.CharField(max_length=200)
    # location = forms.PointField()
    date = forms.DateTimeField()
    image = forms.ImageField()
    is_liked = forms.BooleanField()