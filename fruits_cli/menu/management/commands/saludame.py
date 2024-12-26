from django.core.management.base import BaseCommand
from colorama import Fore, Style
import emoji

class Command(BaseCommand):
    help = 'Saluda al usuario'

    def handle(self, *args, **kwargs):
        self.stdout.write(str(Fore.BLUE) + emoji.emojize(":wave: Hola! Bienvenido al programa 'Saludame' :wave:") + str(Style.RESET_ALL))
        name = input(str(Fore.GREEN) + "Por favor, ingrese su nombre: " + str(Style.RESET_ALL))
        self.stdout.write(str(Fore.YELLOW) + emoji.emojize(f"Hola, {name}! :smile:") + str(Style.RESET_ALL))