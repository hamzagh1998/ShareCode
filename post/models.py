from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

categories = (("python", "python"), ("php", "php"),
              ("java", "java"), ("c/c++", "c/c++"),
              ("web", "web"), ("gui", "gui"),
              ("AI", "AI"), ("DSA", "DSA"),
              ("other", "other"))

def imageUploadLocation(instance, filename):
    file_path = "posts/{user_id}/{username}-{filename}".format(user_id=instance.author.id,
                                                               username=instance.author.username,
                                                               filename=filename)
    return file_path

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    post_image = models.ImageField(default="post.png", upload_to=imageUploadLocation)
    category = models.CharField(max_length=50, blank=False, null=False, choices=categories)
    body = models.TextField(blank=False, help_text='You can include html tags!')
    url = models.URLField(blank=True)
    likes = models.ManyToManyField(User, related_name="Likes", blank=True)
    slug = models.SlugField(unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def summary(self):
        return self.body[:100]+'...'

    def __str__(self):
        return "%s-%s"%(self.title, self.author.username)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000, verbose_name="Add Comment")
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

class CommentReplie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000, blank=True, verbose_name="Reply")

    def __str__(self):
        return self.author.username
