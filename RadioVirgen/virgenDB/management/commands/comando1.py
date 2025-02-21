from django.core.management.base import BaseCommand, CommandError
from virgenDB.models import *

class Command(BaseCommand):
    help = 'Comando 1'

    def handle(self, *args, **options):
        try:
            if not Usuario.objects.exists():
                self.stdout.write(self.style.WARNING('Todavia no hay usuarios en la base de datos'))
            else:
                listaUsuariosActivos = Usuario.objects.filter(fecha_de_baja=None)
                if len(list(listaUsuariosActivos)) == 0:
                    self.stdout.write(self.style.WARNING('No hay usuarios activos en la base de datos'))
                else:
                    usuario = Usuario.objects.get(id = 1)
                    self.stdout.write(self.style.SUCCESS(f'Nombre: {usuario.nombre}'))

                    pago_con_tarjeta = Pago_con_tarjeta.objects.create(
                        numero_tarjeta= 1526544,
                        cvc = 656,
                        nombre_completo = "GLORIA SAUNDERS SAUNDERS"
                    )
                    pago_con_paypal = Paypal.objects.create(
                        correo_electronico="gloriasaunders@gmail.com"
                    )
                    pago_con_transferencia_bancaria = Transferencia_bancaria.objects.create(
                        numero_cuenta = 1524354,
                        nombre_cuenta = "GLORIA SAUNDERS SAUNDERS"
                    )

                    metodo_pago = Metodos_pago.objects.create(
                        id_usuario = usuario,
                        pago_con_tarjeta = pago_con_tarjeta,
                        paypal = pago_con_paypal,
                        transferencia_bancaria = pago_con_transferencia_bancaria
                    )

                    self.stdout.write(self.style.SUCCESS(f'"Usuario y métodos de pago creados correctamente"  {metodo_pago.id_usuario}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))