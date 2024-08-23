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

#direcionar usuario pelo ID (if ID_user = ID_doador return redirect DOADOR), nome(if nome_user = nome_doador return redirect DOADOR), pelo grupo

# 2-Criar o models(Recebedor)
#3-Validators(Doador,Recebedor)
# 3-Refazer o forms(sistema,rec)
# 4-Refazer views e templates
# 4-Criar Views
# 5-Criar validação de redirecionamento(sistema Recebedor)
