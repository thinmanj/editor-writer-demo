from django.urls import reverse
from django.conf import settings
from django.db import models
from django_choice_object import Choice


class Article(models.Model):

    class StatusChoice(Choice):
        OPEN = 1
        ASSIGNED = 2
        FOR_REVIEW = 3
        APPROVED = 4

    editor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='editors', null=True, blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='writers', null=True, blank=True)
    document = models.URLField(max_length=1000, default='', blank=True)
    status = models.IntegerField(choices=StatusChoice,
                                 default=StatusChoice.OPEN)
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='', blank=True)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
