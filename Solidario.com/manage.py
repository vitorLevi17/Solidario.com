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
# 1-(recebedor_inicio 145) cancelado
# 1.1- recebedor_inicio (mostra doacoes_rec com status aberto)
# 1.1-Parametrizar os status e suas visualizações(status aberto)
# Ordenar por urgencia / Localização
# fazer forms para os filtros de recebedores(Doações,Pedidos,Centros)
# fazer forms para os filtros de doadores(Pedidos,Centros)
# 1.1-API para buscar endereço formatado
# 2- Bloquear Views para usuarios diferentes



