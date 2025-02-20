from datetime import date, timedelta

from django.core.management.base import BaseCommand

from virgenDB.models import *

class Command(BaseCommand):
    help = 'Comando que permite recibir como parámetro el nick de un usuario y ver a que plan esta suscrito, y los miembros de el plan familia si es familiar'

    def add_arguments(self, parser):
        parser.add_argument(
            'meses',
            type=int,
            help='Numero de meses hasta hoy que quieres saber los ingresos'
        )


    def handle(self, *args, **options):
        meses = options.get('meses')
        totalIngresos = 0
        if Usuario.objects.exists():
            usuarios = Usuario.objects.all()
            for usuario in usuarios:
                inicio = date.today() - timedelta(days=30*meses)

                if usuario.fecha_de_alta > inicio:
                    inicioPagos = usuario.fecha_de_alta
                else:
                    inicioPagos = inicio

                if usuario.fecha_de_baja:
                    finalPagos = usuario.fecha_de_baja
                else:
                    finalPagos = date.today()

                if inicioPagos < finalPagos:
                    mesesPagados = 0
                    mesActual = inicioPagos.replace(day=1)  # Primer día del mes de inicio
                    while mesActual < finalPagos:
                        mesesPagados += 1
                        mesActual += timedelta(days=30)
                    totalIngresos += mesesPagados*usuario.plan.precio
            self.stdout.write(self.style.SUCCESS(f'Los ingresos de los ultimos {meses} meses son: {totalIngresos}$'))




