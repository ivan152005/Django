import random
from datetime import timedelta, datetime

from faker import Faker
from django.core.management.base import BaseCommand
from virgenDB.models import Autor, Programa, Podcast, Usuario, Reproducciones, Plan, Familia

class Command(BaseCommand):
    help = 'Carga datos iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # creacion
        programas = []
        for i in range(6):  # creacion de 6 programas con entre 1 y 5 autores
            programa = Programa.objects.create(nombre=f'Programa {i+1}')
            programas.append(programa)

        for i in range(30): #º creacion de 30 autores
            programa = random.choice(programas)
            if Autor.objects.filter(programa=programa).count() < programa.numMaxAutores:
                Autor.objects.create(nombre=fake.name(), programa=programa)

        # creacion de 300 podcast
        for i in range(300):
            podcast = Podcast.objects.create(
                nombre=f'Podcast {i+1}',
                categoria=random.choice(['Educativo', 'Comedia', 'Formacion']),
                likes=random.randint(0, 1000),
                numReproducciones=random.randint(0, 10000),
                urlDrive=f'www.drive{i+1}.com',
                programa=random.choice(programas)# asignacion de un programa aleatorio
            )
            # asiganacion de autores a cada podcast
            authors = Autor.objects.filter(programa=podcast.programa)
            podcast.autores.set(random.sample(list(authors), random.randint(1, list(authors).__len__())))
        # creacion  familia
        Familia.objects.create(nombre='Familia 1')
        Familia.objects.create(nombre='Familia 2')
        Familia.objects.create(nombre='Familia 3')



        Plan.objects.create(nombre='Individual', precio=3)
        Plan.objects.create(nombre='Jubilado', precio=2)
        Plan.objects.create(nombre='Estudiante', precio=1.5)
        Plan.objects.create(nombre='Familiar', precio=2)

        # creacion de 10 usuarios
        for i in range(10):
            nick = fake.user_name()
            familia = Familia()
            listaPlanes = list(Plan.objects.all())
            plan = random.choice(listaPlanes)
            hayFamiliaDisponible = False
            if plan.nombre == 'Familiar':
                listaFamilias = list(Familia.objects.all())
                for fam in listaFamilias:
                    numUsuarios = Usuario.objects.filter(familia=fam).count()
                    if numUsuarios < fam.max_miembros:
                        hayFamiliaDisponible = True
                        familia = fam
                        break
                if not hayFamiliaDisponible:
                    familia = Familia.objects.create(nombre=f'Familia de {nick}')
            else:
                familia = None
            usuario = Usuario.objects.create(
                nick=nick,
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                email=fake.email(),
                password=fake.password(),
                fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=80),
                fecha_de_alta=fake.date_between(start_date=datetime.today()-timedelta(days=365), end_date=datetime.today()),
                plan=plan,
                familia=familia
            )

            # creacion de entre 20 y 70 reproducciones para cada usuario
            for _ in range(random.randint(20, 70)):
                podcast = random.choice(Podcast.objects.all())
                Reproducciones.objects.create(
                    idUsuario=usuario,
                    idPodcast=podcast,
                    numReproducciones=random.randint(1, 10)  # numero de reproducciones de cada podcast
                )

        self.stdout.write(self.style.SUCCESS('exito al cargar datos iniciales en la base de datos'))