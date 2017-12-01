from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VideoItem
from .forms import VideoAddForm

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def list_videos(request):
    if request.method == "POST":
        form = VideoAddForm(request.POST)
        if form.is_valid():
            video = form.save(commit = False);
            video.video_user_id = request.user;
            video.video_start = 0;
            video.video_end = 0;
            video.save();
            return redirect(list_videos)
    else:
        videos = VideoItem.objects.filter(video_user_id=request.user)
        form = VideoAddForm()
    return render(request, "list_videos.html", {'form':form, 'videos':videos})

#-------------------------------------------------------------------------------
