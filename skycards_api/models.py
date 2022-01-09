from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='cards',
                             related_query_name='card')
    text = models.CharField(max_length=1023, null=True, blank=True)
    place = models.CharField(max_length=255, null=True, blank=True)
    date = models.CharField(max_length=255, null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    card_url = models.CharField(max_length=1023, null=True, blank=True)
    bg_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "cards"
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
