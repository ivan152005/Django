from django.core.management.base import BaseCommand, CommandError
from virgenDB.models import *

class Command(BaseCommand):
    help = 'Comando que permite recibir como parámetro el nick de un usuario y añadir un podcast a su lista de pendientes de escuchar.'

    def add_arguments(self, parser):
        # Argumento obligatorio: id del usuario.
        parser.add_argument(
            'id',
            type=int,
            help='Nick del usuario al que se le añadirá el podcast pendiente'
        )


    def handle(self, *args, **options):
        id = options.get('id')

        #Busca al usuario
        try:
            usuario = Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            raise CommandError(f'No se encontró el usuario con id "{id}".')

        #Busca metodos de pago
        try:
            metodos_pago = Metodos_pago.objects.get(id_usuario=id)

            self.stdout.write(self.style.SUCCESS(
                f'Metodos de pago encontrados para el usuario {id}'
            ))
            if metodos_pago.pago_con_tarjeta:
                self.stdout.write(self.style.SUCCESS(
                    f'El usuario {id} tiene pago con tarjeta activo'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'{metodos_pago.pago_con_tarjeta}'
                ))


            if metodos_pago.paypal:
                self.stdout.write(self.style.SUCCESS(
                    f'El usuario {id} tiene pago con paypal'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'{metodos_pago.paypal}'
                ))


            if metodos_pago.transferencia_bancaria:
                self.stdout.write(self.style.SUCCESS(
                    f'El usuario {id} tiene pago con transferencia bancaria'
                ))
                self.stdout.write(self.style.SUCCESS(
                    f'{metodos_pago.transferencia_bancaria}'
                ))


        except Podcast.DoesNotExist:
            raise CommandError(f'No se encontraron métodos de pago para id "{id}".')