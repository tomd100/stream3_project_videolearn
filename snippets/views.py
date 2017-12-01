from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from videos.models import SnippetItem
from .forms import SnippetAddForm

# Create your views here.

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def list_snippets(request):
    if request.method == "POST":
        form = SnippetAddForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit = False);
            snippet.snippet_user_id = request.user;
            snippet.snippet_start = 0;
            snippet.snippet_end = 0;
            snippet.save();
            return redirect(list_snippets)
    else:
        snippets = SnippetItem.objects.filter(video_user_id=request.user)
        form = SnippetAddForm()
    return render(request, "list_snippets.html", {'form':form, 'snippets':snippets})

#-------------------------------------------------------------------------------