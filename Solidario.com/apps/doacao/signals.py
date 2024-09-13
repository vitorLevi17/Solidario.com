# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from apps.doacao.models import DoacaoRec
# from django.contrib import messages
#
# @receiver(post_save, sender=DoacaoRec)
# def notificar_doador(sender, instance, **kwargs):
#     # Verifica se o status foi alterado para "andamento"
#     if instance.status == 'andamento':
#         doador = instance.doador
#         # Exibe uma mensagem de notificação para o doador
#         # Você pode também enviar um email ou mensagem de outro tipo aqui.
#         messages.success(doador.usuario, f"A sua doação do item {instance.item.nm_item} foi aceita!")
