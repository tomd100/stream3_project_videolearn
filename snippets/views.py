from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from videos.models import VideoItem, SnippetItem
from .forms import SnippetAddForm

# Create your views here.

#-------------------------------------------------------------------------------

def play_snippets(request, id):
    video = get_object_or_404(VideoItem, pk=id)
    snippets = SnippetItem.objects.filter(video = video);
    form = SnippetAddForm()
    return render(request, "play_snippets.html", {"video": video, "snippets": snippets, "form": form})

#-------------------------------------------------------------------------------