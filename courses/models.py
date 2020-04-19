from django.db import models


class CoursesManage(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(name__icontains=query)


class Courses(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    create_at = models.DateTimeField('Criado em ', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em ', auto_now=True)

    objects = CoursesManage()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ('courses:details', (), {'slug' : self.slug})

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering=['name']