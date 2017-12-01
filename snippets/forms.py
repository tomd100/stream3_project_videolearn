from django import forms
from videos.models import SnippetItem

#-------------------------------------------------------------------------------

class SnippetAddForm(forms.ModelForm):
    snippet_title = forms.CharField(
        label = 'Title',
        widget = forms.TextInput(
            attrs = {'class': 'field_input'}
        )
    )

    class Meta:
        model = SnippetItem
        fields = ['snippet_title']
        
#-------------------------------------------------------------------------------        