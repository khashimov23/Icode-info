from django.db import models
from django.urls import reverse

class Student(models.Model):

    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    telfon = models.CharField(max_length=9)
    yonalish = models.CharField(max_length=250)
    grant = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ism} {self.familya}'

    class Meta:
        # ordering = ('ism',)
        verbose_name_plural = 'Talabalar'
    

class Teacher(models.Model):

    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    telfon = models.CharField(max_length=9)
    fan = models.CharField(max_length=20)
    rasm = models.ImageField(upload_to='teachers')

    def __str__(self):
        return f'{self.ism} {self.familya} {self.yosh}'

    class Meta:
        verbose_name_plural = "O'qituvchilar"

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[self.id])



class Xona(models.Model):

    raqam = models.PositiveIntegerField()
    egasi = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="xonalar")
    parta_soni = models.PositiveIntegerField()
    stul_soni = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.raqam} - {self.egasi.fan}'

    class Meta:
        verbose_name_plural = 'Xonalar'