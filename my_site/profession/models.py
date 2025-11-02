from django.db import models
from django.urls import reverse


class Profession(models.Model):
    title=models.CharField(max_length=200,verbose_name='название')
    url_content=models.CharField(max_length=200, verbose_name="ссылка на видео",blank=True, default='')
    img_static=models.ImageField(upload_to='professions/', blank=True, default='')
    slug=models.SlugField(max_length=200, db_index=True, unique=True)
    dp_index_prof = models.CharField(max_length=100, blank=True, null=True, verbose_name='Доп индекс для этапа')
    termin=models.TextField(blank=True, default='', verbose_name='Определение')
    img_history=models.ImageField(upload_to='professions/history_prof/', blank=True, verbose_name='Фото истории')
    tekst_history=models.TextField(blank=True, verbose_name='Текст истории')
    img_functions=models.ImageField(upload_to='professions/functions_prof/', blank=True, verbose_name='Фото функций')
    img_spec=models.ImageField(upload_to='professions/spec_prof/', blank=True, verbose_name='Фото специализаций')
    img_skils=models.ImageField(upload_to='professions/skils_prof/', blank=True, verbose_name='Фото навыков')
    tekst_vostreb=models.TextField(blank=True, verbose_name='Текст востребованности')
    img_otrasl=models.ImageField(upload_to='professions/otrasl_prof/', blank=True, verbose_name='Фото отраслей')
    tekst_learn=models.TextField(blank=True, verbose_name='Текст образования')
    img_rebus=models.ImageField(upload_to='professions/rebus_prof/', blank=True, verbose_name='Фото ребусов')
    img_otvet=models.ImageField(upload_to='professions/otvet_prof/', blank=True, verbose_name='Фото ответов на ребусы')




    class Meta:
        verbose_name = "Професcия"
        verbose_name_plural = 'Профеcсии'

    def get_absolute_url(self):
        return reverse('post_professions', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title

class Presentations(models.Model):
    title=models.CharField(max_length=200)
    file=models.FileField(upload_to='presentations/pres_prof', verbose_name="Презентация по профессии")
    file_met=models.FileField(upload_to='presentations/metod_prof', verbose_name="Файл по методическим пособиям", blank=True)

    class Meta:
        verbose_name = "Презентиция"
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return self.title

class EngineeringProcessesAtaps(models.Model):
    title_ataps=models.CharField(max_length=200)
    dp_index=models.CharField(max_length=100, blank=True, default='',  verbose_name='Индекс для процессов и этапов')
    opisanie=models.TextField()
    img=models.ImageField(upload_to='engineering_processes/', blank=True, default='')
    slug=models.SlugField(max_length=200, db_index=True, unique=True)
    dp_index_prof = models.CharField(max_length=100, blank=True, default='', verbose_name='доп индекс для профессии')

    class Meta:
        verbose_name = "Инженерный_этап"
        verbose_name_plural = 'Инженерные_этапы'

    def get_absolute_url(self):
        return reverse('post_engineering', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title_ataps

class EngineeringProcessesTitle(models.Model):
    title = models.CharField(max_length=200)
    dp_index = models.CharField(max_length=100, blank=True, default='', verbose_name='Индекс для процессов и этапов')

    class Meta:
        verbose_name = "Инженерный_процесс"
        verbose_name_plural = 'Инженерные_процессы'

    def __str__(self):
        return self.title
