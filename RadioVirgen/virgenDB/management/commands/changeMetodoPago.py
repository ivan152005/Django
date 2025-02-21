from django.core.management.base import BaseCommand, CommandError
from  virgenDB.models import *


class Command(BaseCommand):
    help = 'Comando 3'

    def add_arguments(self, parser):
        parser.add_argument(
            'id_usuario',
            type=int,
            help='Id del usuario'
        )
        parser.add_argument(
            'id_metodo_pago',
            type=int,
            help='ID del metodo de pago'
        )
        parser.add_argument(
            'pago',
            type=str,
            help='Nombre del metodo de pago'
        )

    def handle(self, *args, **options):
        id_usuario = options.get('id_usuario')
        id_metodo_pago = options.get('id_metodo_pago')
        pago = options.get('pago')

        try:
            Usuario.objects.get(id = id_usuario)
        except Usuario.DoesNotExist:
            raise CommandError(f'No se encontró el usuario con id "{id_usuario}"')

        metodos = Metodos_pago.objects.get(id = id_metodo_pago)

        if metodos:
            metodos = Metodos_pago.objects.get(id_usuario = id_usuario)

            if metodos:
                if metodos.pago_con_tarjeta.predeterminado:
                    if pago == 'pago_con_tarjeta':

                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ya es el introducido'
                        ))
                    else:
                        metodos.pago_con_tarjeta.predeterminado = True
                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ha sido cambiado a {pago}'
                        ))

                        if metodos.paypal.predeterminado:
                            metodos.pago_con_tarjeta.predeterminado = False
                            metodos.save()

                        if metodos.transferencia_bancaria.predeterminado:
                            metodos.pago_con_tarjeta.predeterminado = False
                            metodos.save()

                elif metodos.paypal.predeterminado:
                    if pago == 'paypal':

                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ya es el introducido'
                        ))
                    else:
                        metodos.paypal.predeterminado = True
                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ha sido cambiado a {pago}'
                        ))

                        if metodos.transferencia_bancaria.predeterminado:
                            metodos.pago_con_tarjeta.predeterminado = False
                            metodos.save()

                        if metodos.pago_con_tarjeta.predeterminado:
                            metodos.pago_con_tarjeta.predeterminado = False
                            metodos.save()

                elif metodos.transferencia_bancaria.predeterminado:
                    if pago == 'transferencia_bancaria':

                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ya es el introducido'
                        ))
                    else:
                        metodos.transferencia_bancaria.predeterminado = True
                        self.stdout.write(self.style.SUCCESS(
                            f'El metodo de pago predeterminado ha sido cambiado a {pago}'
                        ))

                        if metodos.paypal.predeterminado:
                            metodos.transferencia_bancaria.predeterminado = False
                            metodos.save()

                        if metodos.pago_con_tarjeta.predeterminado:
                            metodos.transferencia_bancaria.predeterminado = False
                            metodos.save()

            else:
                self.stdout.write(self.style.SUCCESS(
                    f'No existen metodos de pago para el usuario con id "{id_usuario}"'
                ))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'No existe el metodo de pago con id "{id_metodo_pago}"'
            ))