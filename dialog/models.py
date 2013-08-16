from django.db import models

class Dialog(models.Model):
    text = models.TextField("Text", blank = True, null = True)
    person = models.CharField("Person", max_length = 255, blank = True, null = True)
    image = models.ImageField("Portrait", upload_to = "portraits", blank = True, null = True)
    order = models.IntegerField("Order", blank = True, null = True)

    def __unicode__(self):
        return u"%s" % self.person

    def __str__(self):
        return u"%s" % self.person

