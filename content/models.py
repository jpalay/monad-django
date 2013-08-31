from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.CharField(max_length=200)
    order = models.PositiveIntegerField()

    @property
    def associated_media(self):
        return Media.objects.filter(page=self)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Media(models.Model):
    identifier = models.CharField(max_length=200)
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.url
    
    def render(self):
        raise NotImplementedException

class Image(Media):
    """
    identifier is URL of Image
    """
    def render(self):
        return '<img src="{0}">'.format(self.identifier)

class YoutubeVideo(Media):
    """
    identifier is video id
    """
    def render(self):
        return '<iframe width="420" height="315" src="//www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'.format(self.identifier)
