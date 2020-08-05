import  datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class LuoTulos(models.Model):
    ottelu_pari = models.CharField(max_length=100)
    tulos_koti = models.IntegerField()
    tulos_vieras = models.IntegerField()
    tulos_yksiristikaksi = models.CharField(max_length=10)

    def __str__(self):
        return self.ottelu_pari


class Osallistuja(models.Model):
    nimi = models.CharField(max_length=50)
    ottelu_pari = models.CharField(max_length=100)
    veikkaus_koti = models.IntegerField()
    veikkaus_vieras = models.IntegerField()
    veikkaus_yksiristikaksi = models.CharField(max_length=10)

    def __str__(self):
        return self.nimi
