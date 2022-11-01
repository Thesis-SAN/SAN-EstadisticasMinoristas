from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    login = models.OneToOneField(User, verbose_name='Usuario', null=False, blank=False, on_delete=models.CASCADE,
                                 related_name='domain_user')
    nombre = models.CharField(verbose_name='Nombre', max_length=250)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=250)
    email = models.EmailField(verbose_name='Correo Electrónico')

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return str(self.login)

    def activo_status(self):
        if self.activo:
            return 'Sí'
        else:
            return 'No'