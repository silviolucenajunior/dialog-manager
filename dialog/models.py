from django.db import models

class Dialog(models.Model):
    conversation = models.ForeignKey("Conversation", blank = True, null = True)
    text = models.TextField("Text", blank = True, null = True)
    person_of = models.ForeignKey("Person", blank = True, null = True, related_name = "person_of")
    person_to = models.ForeignKey("Person", max_length = 255, blank = True, null = True, related_name = "person_to")
    image = models.ImageField("Portrait", upload_to = "portraits", blank = True, null = True)
    order = models.IntegerField("Order", blank = True, null = True)

    def __unicode__(self):
        return u"%s" % self.conversation

    def __str__(self):
        return u"%s" % self.conversation

class Person(models.Model):
    category = models.ForeignKey("Category", blank = True, null = True)
    name = models.CharField("Name", max_length = 128, blank = False, null = True)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return u"%s" % self.name

class Conversation(models.Model):
    category = models.ForeignKey("Category", blank = True, null = True)
    title = models.CharField("Title", max_length = 128, blank = True, null = True)
    triggers = models.ManyToManyField("Trigger", blank = True, null = True)

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return u"%s" % self.title

class Trigger(models.Model):
    name = models.CharField("Name", max_length = 128, blank = True, null = True)
    enabled = models.BooleanField("Enabled")

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return u"%s" % self.title


class Category(models.Model):
    title = models.CharField("Title", max_length = 128, blank = True, null = True)

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return u"%s" % self.title





