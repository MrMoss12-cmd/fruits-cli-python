from random import choice
from typing import Any
from django.core.management.base import BaseCommand
import questionary
from colorama import Fore, Style
import emoji

class Command(BaseCommand):
    help = 'Manu principal con colores, emojis y seleccion interactiva'

    def handle(self, *args, **kwargs):
        while True:
            #Imprimir cabecera con color y emoji
            self.stdout.write(str(Fore.BLUE) + emoji.emojize(":rocket: Bienvenido al Menú principal :rocket:") + str(Style.RESET_ALL))  

            #Menu interactivo
            choice = questionary.select(
                "Seleccione una opcion:",
                choices = [
                    emoji.emojize("1. :wave: Saludame"),
                    emoji.emojize("0. :door: Salir")
                ]
            ).ask()

            if choice == "1. 👋 Salúdame":
                #esto ejecuta el modulo saludame
                from fruits_cli.menu.management.commands.saludame import Command as SaludaCommand
                saluda = SaludaCommand()
                saluda.handle()
            elif choice == "0. 🚪 Salir":
                self.stdout.write(str(Fore.GREEN) + "!Hasta luego!" + str(Style.RESET_ALL))
                break
            else:
                self.stdout.write(str(Fore.RED) + "Opcion no valida. intente nuevamente." + str(Style.RESET_ALL))
