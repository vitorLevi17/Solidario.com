#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

#Corrigir messagessssssssssssssssss
#Calenario e relogio
# Cores de urgencia(Chat gpt)
# DOADOR e Rece(PERFIL  /Configurações) DO-Buscar por item e por recebedor / RE ver_doacao e receber_doacao

#OPCIONAIS
# filtros de recebedores(Doações,Pedidos,Centros) https://github.com/vitorLevi17/PyDj/blob/main/PyDj/apps/galeria/views.py
# filtros de doadores(Pedidos,Centros) https://github.com/vitorLevi17/PyDj/blob/main/PyDj/apps/galeria/views.py
# Ordenar por urgencia / Localização https://github.com/vitorLevi17/PyDj/blob/main/PyDj/apps/galeria/views.py



