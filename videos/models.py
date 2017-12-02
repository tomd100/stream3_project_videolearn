from django.db import models

# Create your models here.
#-------------------------------------------------------------------------------

class VideoItem(models.Model):
    video_user_id = models.ForeignKey('auth.User')
    video_title = models.CharField(max_length=500, blank=False)
    video_url = models.URLField(max_length=500, blank=False)
    video_start = models.FloatField(default = 0)
    video_end = models.FloatField(default = 0)
    
    def __str__(self):
        return self.video_title;
        
#-------------------------------------------------------------------------------

class SnippetItem(models.Model):
    video_id = models.ForeignKey(VideoItem, on_delete=models.CASCADE)
    snippet_title = models.CharField(max_length=500, blank=False)
    snippet_start = models.FloatField(default = VideoItem().video_start)
    snippet_end = models.FloatField(default = VideoItem().video_end)
    
    def __str__(self):
        return self.snippet_title;
        
#-------------------------------------------------------------------------------        