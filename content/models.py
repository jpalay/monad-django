from django.db import models
from adminsortable.models import Sortable

class Page(Sortable):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.CharField(max_length=200)

    @property
    def associated_media(self):
        return Media.objects.filter(page=self)

    def __unicode__(self):
        return self.title

    class Meta(Sortable.Meta):
        pass

class Media(models.Model):
    IMAGE = "IMAGE"
    VIDEO = 'YOUTUBEVIDEO'
    TYPE_CHOICES = (
        (IMAGE, 'Image'),
        (VIDEO, 'YouTubeVideo')
    )

    identifier = models.CharField(max_length=200)
    media_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=IMAGE)
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.identifier
    
    def render(self):
        if self.media_type == "IMAGE":
            return '<img src="{0}">'.format(self.identifier)
        elif self.media_type == "VIDEO":
            return '<iframe width="420" height="315" src="//www.youtube.com/embed/{0}" frameborder="0" allowfullscreen></iframe>'.format(self.identifier)
