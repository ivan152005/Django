from django.core.management.base import BaseCommand
from virgenDB.models import Usuario, Reproducciones

class Command(BaseCommand):
    help = 'Comando 3 Lista las reproducciones de un usuario dado su nick'

    def add_arguments(self, parser):
        parser.add_argument('nick', type=str, help='Nick del usuario')

    def handle(self, *args, **kwargs):
        nick = kwargs['nick']
        try:
            usuario = Usuario.objects.get(nick=nick)
            reproducciones = Reproducciones.objects.filter(idUsuario=usuario)
            if reproducciones.exists():
                for reproduccion in reproducciones:
                    self.stdout.write(str(reproduccion))
            else:
                self.stdout.write(self.style.WARNING(f'No se encontraron reproducciones para el usuario con nick: {nick}'))
        except Usuario.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Usuario con nick {nick} no encontrado'))