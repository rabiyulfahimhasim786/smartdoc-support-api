from django.db import models

# Create your models here.

class Pdf(models.Model):
    pdffile = models.FileField(null=False, blank=False,  upload_to='async-kv-table')
    pdfdescription = models.TextField()

    def __str__(self):
        return "%s %s" % (self.pdffile, self.pdfdescription)
    
class Outputtext(models.Model):
    csvfile = models.URLField(max_length=255, null=False, blank=False,)
    csvdescription = models.TextField()

    def __str__(self):
        return "%s %s" % (self.csvfile, self.csvdescription)
