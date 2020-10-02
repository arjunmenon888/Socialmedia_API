from django.db import models
from django.contrib.auth.models import User


TAGS = (
    ('a','a'),
    ('b','b'),
    ('c','c')
)
class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(blank=True, null=True, max_length=240)
    image = models.FileField(blank=True, null=True)
    image1 = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    Likes = models.ManyToManyField(User, related_name='post_likes', null=True, blank=True)
    Unlikes = models.ManyToManyField(User, related_name='post_unlikes', null=True, blank=True)
    tag = models.CharField(choices=TAGS,  max_length=1, null=True, blank=True)

    def __str__(self):
        return str(self.user)
 
    def total_likes(self):
        return self.Likes.count()

    def total_unlikes(self):
        return self.Unlikes.count()
