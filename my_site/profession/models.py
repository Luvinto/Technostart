from django.db import models
from django.urls import reverse


class Profession(models.Model):
    title=models.CharField(max_length=200,verbose_name='название')
    url_content=models.CharField(max_length=200, verbose_name="ссылка",blank=True, null=True)
    img_static=models.ImageField(upload_to='professions/', blank=True, null=True)
    slug=models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        verbose_name = "Професcия"
        verbose_name_plural = 'Профеcсии'

    def get_absolute_url(self):
        return reverse('post_professions', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title

class Presentations(models.Model):
    title=models.CharField(max_length=200)
    file=models.FileField(upload_to='presentations/', verbose_name="Файл")

    class Meta:
        verbose_name = "Презентиция"
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return self.title

class EngineeringProcessesAtaps(models.Model):
    title_ataps=models.CharField(max_length=200)
    dp_index=models.CharField(max_length=100, blank=True, null=True)
    opisanie=models.TextField()
    img=models.ImageField(upload_to='engineering_processes/', blank=True, null=True)
    slug=models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = "Инженерный_этап"
        verbose_name_plural = 'Инженерные_этапы'

    def get_absolute_url(self):
        return reverse('post_engineering', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title_ataps

class EngineeringProcessesTitle(models.Model):
    title = models.CharField(max_length=200)
    dp_index = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Инженерный_процесс"
        verbose_name_plural = 'Инженерные_процессы'

    def __str__(self):
        return self.title
