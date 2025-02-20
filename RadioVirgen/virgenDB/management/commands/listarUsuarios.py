from django.core.management.base import BaseCommand

from  virgenDB.models import Usuario

class Command(BaseCommand):
    help = 'Saca la lista de usuarios'
    def handle (self, *args, **kwargs):
        try:
            if not Usuario.objects.exists():
                self.stdout.write(self.style.WARNING('Todavia no hay usuarios en la base de datos'))
            else:
                listaUsuariosActivos = Usuario.objects.filter(fecha_de_baja=None)
                if len(list(listaUsuariosActivos)) == 0:
                    self.stdout.write(self.style.WARNING('No hay usuarios activos en la base de datos'))
                else:
                    for user in listaUsuariosActivos:
                        self.stdout.write(self.style.SUCCESS(f'ID: {user.id}, Nombre: {user.nombre}, Apellidos: {user.apellido}, Nick: {user.nick}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))


