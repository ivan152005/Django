from django.core.management.base import BaseCommand
from virgenDB.models import Autor, Programa, Plan, Familia, Podcast, Usuario, Reproducciones

class Command(BaseCommand):
    help = 'Borrar datos de las tablas'

    def handle(self, *args, **kwargs):
        try:
            Autor.objects.all().delete()
            Programa.objects.all().delete()
            Plan.objects.all().delete()
            Familia.objects.all().delete()
            Podcast.objects.all().delete()
            Usuario.objects.all().delete()
            Reproducciones.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Datos borrados exitosamente de las tablas'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))