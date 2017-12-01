from django import forms
from .models import VideoItem

#-------------------------------------------------------------------------------

class VideoAddForm(forms.ModelForm):
    video_title = forms.CharField(
        label = 'Video Title',
        widget = forms.TextInput(
            attrs = {'class': 'field_input'}
        )
    )
    video_url = forms.CharField(
        label = 'Video Url',
        widget = forms.TextInput(
            attrs = {'class': 'field_input'}
        )
    )        
    class Meta:
        model = VideoItem
        fields = ['video_title', 'video_url']

#-------------------------------------------------------------------------------