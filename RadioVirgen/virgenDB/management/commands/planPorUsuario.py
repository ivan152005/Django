from django.core.management.base import BaseCommand, CommandError

from virgenDB.models import *

class Command(BaseCommand):
    help = 'Comando que permite recibir como parámetro el nick de un usuario y ver a que plan esta suscrito, y los miembros de el plan familia si es familiar'

    def add_arguments(self, parser):
        parser.add_argument(
            'nick',
            type=str,
            help='Nick del usuario'
        )


    def handle(self, *args, **options):
        nick = options.get('nick')

        try:
            usuario = Usuario.objects.get(nick=nick)
            self.stdout.write(self.style.SUCCESS(f'El plan del usuario "{usuario.nick}" es: "{usuario.plan.nombre}"'))

            if (usuario.plan.nombre == 'Familiar'):
                familiares = Usuario.objects.filter(familia= usuario.familia)
                self.stdout.write(
                    self.style.SUCCESS('Los usuarios de esta familia son:'))
                for familiar in familiares:
                    self.stdout.write(self.style.SUCCESS(f'- {familiar.nick}'))

        except Usuario.DoesNotExist:
            raise CommandError(f'No se encontró el usuario con nick "{nick}".')

