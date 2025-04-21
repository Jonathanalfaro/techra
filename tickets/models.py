from django.db import models

# Create your models here.
class Ticket(models.Model):

    ticket = models.CharField(max_length=10, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    prioridad = models.CharField(max_length=100, blank=True, null=True)
    zona = models.CharField(max_length=100, blank=True, null=True)
    tecnico = models.CharField(max_length=100, blank=True, null=True)
    area_atencion = models.CharField(max_length=100, blank=True, null=True)
    serie = models.CharField(max_length=100, blank=True, null=True)
    clave_cliente = models.IntegerField(null=True)
    cliente = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    contacto_1_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_1_email = models.CharField(max_length=100, blank=True, null=True)
    contacto_1_telefono = models.CharField(max_length=100, blank=True, null=True)
    contacto_2_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_2_email = models.CharField(max_length=100, blank=True, null=True)
    contacto_2_telefono = models.CharField(max_length=100, blank=True, null=True)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    distancia = models.IntegerField(null=True)
    fecha_nota = models.DateTimeField(blank=True, null=True)
    id_tipo_prioridad = models.IntegerField(null=True)
    tipo_prioridad = models.CharField(max_length=100, blank=True, null=True)
    id_color = models.IntegerField(null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    minutos_alertamiento = models.IntegerField(null=True)
    id_puesto_escalamiento = models.IntegerField(null=True)
    mensaje_alerta = models.CharField(max_length=100, blank=True, null=True)
    alertar_despues_fecha = models.DateTimeField(null=True)
    estatus_nota_alertamiento = models.CharField(max_length=100, blank=True, null=True)
    tiempo_duracion = models.CharField(max_length=100, blank=True, null=True)
    unidad_medida_duracion = models.CharField(max_length=100, blank=True, null=True)
    fecha_hora_inicio = models.DateTimeField(null=True)
    check_in = models.CharField(max_length=100, blank=True, null=True)
    check_out = models.CharField(max_length=100, blank=True, null=True)
    check_in_programado = models.CharField(max_length=100, blank=True, null=True)
    check_out_programado = models.CharField(max_length=100, blank=True, null=True)
    id_ultimo_estado = models.IntegerField(null=True)

    def serie_as_list(self):
        if self.serie:
            return self.serie.split(',')
        else:
            return []


