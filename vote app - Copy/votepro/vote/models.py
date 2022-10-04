from django.db import models

# Create your models here.


class Votetitle(models.Model):
    title = models.CharField(max_length=100)


class Voting(models.Model):
    text = models.TextField(blank=True, default=True)
    choice1 = models.CharField(default=True, blank=True, max_length=100)
    choice2 = models.CharField(default=True, blank=True, max_length=100)
    choice3 = models.CharField(default=True, blank=True, max_length=100)
    choice1_count = models.IntegerField(default=0)
    choice2_count = models.IntegerField(default=0)
    choice3_count = models.IntegerField(default=0)

    def total(self):
        return self.choice1_count + self.choice2_count + self.choice3_count
