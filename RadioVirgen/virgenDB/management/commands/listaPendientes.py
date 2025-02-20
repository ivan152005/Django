from django.core.management.base import BaseCommand
from virgenDB.models import Usuario, Podcast, Reproducciones

class Command(BaseCommand):
    help = 'Añade un podcast a la lista de pendientes de un usuario dado su nick'

    def add_arguments(self, parser):
        parser.add_argument('nick', type=str, help='Nick del usuario')
        parser.add_argument('podcast_id', type=int, help='ID del podcast')

    def handle(self, *args, **kwargs):
        nick = kwargs['nick']
        podcast_id = kwargs['podcast_id']
        try:
            usuario = Usuario.objects.get(nick=nick)
            podcast = Podcast.objects.get(id=podcast_id)

            #compruebo si el podcast ya está en la lista de reproducciones del usuario
            if Reproducciones.objects.filter(idUsuario=usuario, idPodcast=podcast).exists():
                self.stdout.write(self.style.WARNING(
                    f'El podcast {podcast_id} ya está en la lista de reproducciones del usuario {nick}'))
            else:
                usuario.podcast_pendientes.add(podcast)
                self.stdout.write(
                    self.style.SUCCESS(f'Podcast {podcast_id} añadido a la lista de pendientes del usuario {nick}'))
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Usuario con nick {nick} no encontrado'))
        except Podcast.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Podcast con ID {podcast_id} no encontrado'))