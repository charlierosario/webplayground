from django.db import models
from ckeditor.fields import RichTextField
# esto esta modificado , null=True, blank=True

msj="Cómo obtener las coordenadas de un lugar <br> 1. ir a www.latlong.net <br> 2. Introducir la direccion: ej. Rioja 2045, Rosario, Santa Fe<br>3.Dar al boton Find <br> 4. Aparecera una marca azul en el mapa si ve que no esta exactamente haga doble click en la localizacion exacta<br>5. Listo copie la latitud y longitud tal cual.<br><br>En el campo de localizacion debe introducir de esta forma esos datos incluidos las llaves:<br>{lat: -32.952917, lng: -60.655833}";


class Page(models.Model):
    headerimg = models.ImageField(verbose_name="Imagen", upload_to="projects", null=True, blank=True, help_text="ATENCION!! ASEGURARSE QUE LA IMAGEN NO SUPERA LOS 710px DE ALTURA PARA GUARDAR LA PROPORCIONALIDAD.")
    title = models.CharField(verbose_name="Título", max_length=200)
    codigo = models.CharField(verbose_name="Código", max_length=8)
    fechacurso = models.DateField(verbose_name="Fecha")
    horacurso = models.CharField(verbose_name="Horario", max_length=200,)
    content = RichTextField(verbose_name="Organizan")
    disertantescurso = RichTextField(verbose_name="Disertantes")
    arancelcurso= models.DecimalField(verbose_name="Arancel $", max_digits=6, decimal_places=2, help_text="Solo 2 decimales si corresponde y usar la coma no el punto")
    localizacioncurso= models.CharField(verbose_name="Localizacion (Coordenadas)", max_length=400, help_text=msj)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:

        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['-fechacurso']

    def __str__(self):
        return self.title
