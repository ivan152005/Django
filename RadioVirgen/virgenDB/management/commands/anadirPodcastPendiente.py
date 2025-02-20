from django.core.management.base import BaseCommand, CommandError
from virgenDB.models import *

class Command(BaseCommand):
    help = 'Comando que permite recibir como parámetro el nick de un usuario y añadir un podcast a su lista de pendientes de escuchar.'

    def add_arguments(self, parser):
        # Argumento obligatorio: nick del usuario.
        parser.add_argument(
            'nick',
            type=str,
            help='Nick del usuario al que se le añadirá el podcast pendiente'
        )
        # Argumento obligatorio: id del podcast a añadir.
        parser.add_argument(
            '--podcast_id',
            type=int,
            required=True,
            help='ID del podcast a añadir a la lista de pendientes de escuchar'
        )

    def handle(self, *args, **options):
        nick = options.get('nick')
        podcast_id = options.get('podcast_id')

        #Busca al usuario
        try:
            usuario = Usuario.objects.get(nick=nick)
        except Usuario.DoesNotExist:
            raise CommandError(f'No se encontró el usuario con nick "{nick}".')

        #Busca el podcast
        try:
            podcast = Podcast.objects.get(id=podcast_id)
        except Podcast.DoesNotExist:
            raise CommandError(f'No se encontró el podcast con id "{podcast_id}".')

        #Añadimos el podcast a la lista de pendientes de escuchar del usuario
        if usuario.podcast_pendientes.filter(id=podcast_id).exists():
            self.stdout.write(self.style.WARNING(
                f'El podcast "{podcast.nombre}" ya está en la lista de pendientes del usuario "{nick}"'
            ))
        else:
            usuario.podcast_pendientes.add(podcast)
            self.stdout.write(self.style.SUCCESS(
                f'Se ha añadido el podcast "{podcast.nombre}" a la lista de pendientes del usuario "{nick}"'
            ))