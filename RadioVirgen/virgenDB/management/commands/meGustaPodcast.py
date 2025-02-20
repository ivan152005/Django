from django.core.management.base import BaseCommand, CommandError
from  virgenDB.models import *


class Command(BaseCommand):
    help = 'Comando para añadir un "me gusta" a un podcast. Si se pasa como parámetro el id del podcast, deben listarse todos los podcasts que le gustan al usuario.'

    def add_arguments(self, parser):
        parser.add_argument(
            'nick',
            type=str,
            help='Nick del usuario al que se le añadirá el "me gusta"'
        )
        #Parámetro opcional: id del podcast, para agregar el podcast al usuario
        parser.add_argument(
            '--podcast_id',
            type=int,
            help='ID del podcast al que se le añadirá el "me gusta"'
        )

    def handle(self, *args, **options):
        nick = options.get('nick')
        podcast_id = options.get('podcast_id')

        try:
            usuario = Usuario.objects.get(nick=nick)
        except Usuario.DoesNotExist:
            raise CommandError(f'No se encontró el usuario con nick "{nick}"')

        #Si se proporciona el id del podcast, se añade el "me gusta"
        if podcast_id is not None:
            try:
                podcast = Podcast.objects.get(id=podcast_id)
            except Podcast.DoesNotExist:
                raise CommandError(f'No se encontró el podcast con id "{podcast_id}".')

            #Añadimos el podcast a la relación many-to-many de "me gusta"
            usuario.me_gusta_podcast.add(podcast)
            self.stdout.write(self.style.SUCCESS(
                f'Se ha añadido un "me gusta" al podcast "{podcast.nombre}" (ID: {podcast_id}) para el usuario "{nick}"'
            ))

        #Se listan todos los podcasts a los que el usuario ha dado "me gusta"
        try:
            liked_podcasts = usuario.me_gusta_podcast.all()
        except Exception as e:
            raise CommandError(f'Error al recuperar los podcasts "me gusta": {str(e)}')

        if liked_podcasts.exists():
            self.stdout.write(self.style.SUCCESS(f'Podcasts que le gustan al usuario "{nick}":'))
            for p in liked_podcasts:
                self.stdout.write(f'ID: {p.id} - Nombre: {p.nombre}')
        else:
            self.stdout.write(self.style.WARNING(f'El usuario "{nick}" no tiene podcasts marcados con "me gusta"'))