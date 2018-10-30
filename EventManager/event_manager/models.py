from django.db import models

# Create your models here.


class Crawl(models.Model):
    """
    Simple model for a crawl.
    """

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateField(null=True, blank=True)


class CrawlStop(models.Model):
    """
    Simple model for a crawl stop.
    """

    crawl_id = models.ForeignKey(Crawl, on_delete=models.CASCADE)
    number = models.IntegerField(null=False, blank=False, unique=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    hosts = models.CharField(max_length=255, null=False, blank=False)
    drink = models.CharField(max_length=255, null=False, blank=True)
